"""Cloudflare R2 (S3 API): загрузка, скачивание, список, presigned URL.

Endpoint: https://<R2_ACCOUNT_ID>.r2.cloudflarestorage.com, регион "auto".
Если установлен boto3 — используется он (multipart для больших файлов).
Иначе — встроенный минимальный клиент S3 (подпись AWS SigV4 на requests),
одиночный PUT (лимит R2 для одиночного PUT ~5 ГБ — для серий достаточно).

    from pipeline import storage
    storage.upload("output/ep01.mp4", "episodes/ep01.mp4")
    storage.download("episodes/ep01.mp4", "/tmp/ep01.mp4")
    url = storage.presigned_url("episodes/ep01.mp4", expires=3600)
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import hmac
import mimetypes
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote

from . import config

REGION = "auto"
SERVICE = "s3"
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()

try:  # pragma: no cover - зависит от окружения
    import boto3  # type: ignore
    from botocore.config import Config as _BotoConfig  # type: ignore
    HAVE_BOTO3 = True
except ImportError:
    HAVE_BOTO3 = False


def endpoint_url(account_id: str | None = None) -> str:
    return f"https://{account_id or config.get('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com"


def _creds() -> tuple[str, str, str]:
    v = config.require("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY")
    return v["R2_ACCOUNT_ID"], v["R2_ACCESS_KEY_ID"], v["R2_SECRET_ACCESS_KEY"]


def bucket() -> str:
    return config.get("R2_BUCKET")  # type: ignore[return-value]


# ===================================================== SigV4 (без boto3) ===

def _hmac(key: bytes, msg: str) -> bytes:
    return hmac.new(key, msg.encode(), hashlib.sha256).digest()


def _signing_key(secret: str, date: str, region: str, service: str) -> bytes:
    k = _hmac(("AWS4" + secret).encode(), date)
    k = _hmac(k, region)
    k = _hmac(k, service)
    return _hmac(k, "aws4_request")


def _uri_encode_path(path: str) -> str:
    return quote(path, safe="/-_.~")


def _canonical_query(params: dict[str, str]) -> str:
    return "&".join(f"{quote(k, safe='-_.~')}={quote(str(v), safe='-_.~')}"
                    for k, v in sorted(params.items()))


def sign_v4(method: str, host: str, path: str, query: dict[str, str], headers: dict[str, str],
            payload_hash: str, access_key: str, secret_key: str, now: dt.datetime,
            region: str = REGION, service: str = SERVICE) -> dict[str, str]:
    """Вернуть заголовки с Authorization (AWS Signature Version 4)."""
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date = now.strftime("%Y%m%d")
    hdrs = {k.lower(): str(v).strip() for k, v in headers.items()}
    hdrs["host"] = host
    hdrs["x-amz-date"] = amz_date
    hdrs["x-amz-content-sha256"] = payload_hash
    signed = sorted(hdrs)
    canonical_headers = "".join(f"{k}:{hdrs[k]}\n" for k in signed)
    signed_headers = ";".join(signed)
    canonical_request = "\n".join([method, _uri_encode_path(path), _canonical_query(query),
                                   canonical_headers, signed_headers, payload_hash])
    scope = f"{date}/{region}/{service}/aws4_request"
    string_to_sign = "\n".join(["AWS4-HMAC-SHA256", amz_date, scope,
                                hashlib.sha256(canonical_request.encode()).hexdigest()])
    signature = hmac.new(_signing_key(secret_key, date, region, service), string_to_sign.encode(),
                         hashlib.sha256).hexdigest()
    hdrs["authorization"] = (f"AWS4-HMAC-SHA256 Credential={access_key}/{scope}, "
                             f"SignedHeaders={signed_headers}, Signature={signature}")
    del hdrs["host"]  # requests выставит Host сам (то же значение)
    return hdrs


def presign_v4(method: str, host: str, path: str, access_key: str, secret_key: str,
               now: dt.datetime, expires: int = 3600, region: str = REGION,
               service: str = SERVICE) -> str:
    """Presigned URL (query-string SigV4)."""
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date = now.strftime("%Y%m%d")
    scope = f"{date}/{region}/{service}/aws4_request"
    q = {"X-Amz-Algorithm": "AWS4-HMAC-SHA256", "X-Amz-Credential": f"{access_key}/{scope}",
         "X-Amz-Date": amz_date, "X-Amz-Expires": str(expires), "X-Amz-SignedHeaders": "host"}
    canonical_request = "\n".join([method, _uri_encode_path(path), _canonical_query(q),
                                   f"host:{host}\n", "host", "UNSIGNED-PAYLOAD"])
    sts = "\n".join(["AWS4-HMAC-SHA256", amz_date, scope,
                     hashlib.sha256(canonical_request.encode()).hexdigest()])
    q["X-Amz-Signature"] = hmac.new(_signing_key(secret_key, date, region, service), sts.encode(),
                                    hashlib.sha256).hexdigest()
    return f"https://{host}{_uri_encode_path(path)}?{_canonical_query(q)}"


class _MiniS3:
    """Минимальный S3-клиент для R2 (path-style: /<bucket>/<key>)."""

    def __init__(self) -> None:
        self.account, self.ak, self.sk = _creds()
        self.host = f"{self.account}.r2.cloudflarestorage.com"

    def _req(self, method: str, path: str, query: dict | None = None, data: bytes | None = None,
             headers: dict | None = None, stream: bool = False, file_path: Path | None = None):
        from .net import request
        query = query or {}
        if file_path is not None:
            h = hashlib.sha256()
            with file_path.open("rb") as f:
                for chunk in iter(lambda: f.read(1 << 20), b""):
                    h.update(chunk)
            payload_hash = h.hexdigest()
        else:
            payload_hash = hashlib.sha256(data or b"").hexdigest()
        hdrs = sign_v4(method, self.host, path, query, headers or {}, payload_hash, self.ak, self.sk,
                       dt.datetime.now(dt.timezone.utc))
        url = f"https://{self.host}{_uri_encode_path(path)}"
        if query:
            url += "?" + _canonical_query(query)
        if file_path is not None:
            with file_path.open("rb") as f:
                hdrs["content-length"] = str(file_path.stat().st_size)
                return request(method, url, service="r2", headers=hdrs, data=f, retries=1,
                               timeout=(10, 1800))
        return request(method, url, service="r2", headers=hdrs, data=data, stream=stream)

    def upload(self, local: Path, key: str, content_type: str) -> None:
        self._req("PUT", f"/{bucket()}/{key}", headers={"content-type": content_type}, file_path=local)

    def download(self, key: str, local: Path) -> None:
        resp = self._req("GET", f"/{bucket()}/{key}", stream=True)
        tmp = local.with_suffix(local.suffix + ".part")
        with tmp.open("wb") as f:
            for chunk in resp.iter_content(1 << 20):
                f.write(chunk)
        tmp.replace(local)

    def list(self, prefix: str, max_keys: int) -> list[dict]:
        resp = self._req("GET", f"/{bucket()}", query={"list-type": "2", "prefix": prefix,
                                                     "max-keys": str(max_keys)})
        ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
        root = ET.fromstring(resp.content)
        return [{"key": c.findtext("s3:Key", namespaces=ns),
                 "size": int(c.findtext("s3:Size", "0", namespaces=ns))}
                for c in root.findall("s3:Contents", ns)]

    def delete(self, key: str) -> None:
        self._req("DELETE", f"/{bucket()}/{key}")

    def presigned(self, key: str, expires: int) -> str:
        return presign_v4("GET", self.host, f"/{bucket()}/{key}", self.ak, self.sk,
                          dt.datetime.now(dt.timezone.utc), expires)


class _Boto:
    def __init__(self) -> None:
        account, ak, sk = _creds()
        self.s3 = boto3.client("s3", endpoint_url=endpoint_url(account), aws_access_key_id=ak,
                               aws_secret_access_key=sk, region_name=REGION,
                               config=_BotoConfig(signature_version="s3v4", retries={"max_attempts": 5}))

    def upload(self, local: Path, key: str, content_type: str) -> None:
        self.s3.upload_file(str(local), bucket(), key, ExtraArgs={"ContentType": content_type})

    def download(self, key: str, local: Path) -> None:
        self.s3.download_file(bucket(), key, str(local))

    def list(self, prefix: str, max_keys: int) -> list[dict]:
        r = self.s3.list_objects_v2(Bucket=bucket(), Prefix=prefix, MaxKeys=max_keys)
        return [{"key": o["Key"], "size": o["Size"]} for o in r.get("Contents", [])]

    def delete(self, key: str) -> None:
        self.s3.delete_object(Bucket=bucket(), Key=key)

    def presigned(self, key: str, expires: int) -> str:
        return self.s3.generate_presigned_url("get_object", Params={"Bucket": bucket(), "Key": key},
                                              ExpiresIn=expires)


def client():
    return _Boto() if HAVE_BOTO3 else _MiniS3()


# ============================================================= API модуля ===

def upload(local_path: str | Path, key: str | None = None) -> str:
    """Загрузить файл; возвращает ключ объекта."""
    p = Path(local_path)
    key = (key or p.name).lstrip("/")
    ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    client().upload(p, key, ctype)
    return key


def download(key: str, local_path: str | Path) -> Path:
    p = Path(local_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    client().download(key.lstrip("/"), p)
    return p


def list_objects(prefix: str = "", max_keys: int = 1000) -> list[dict]:
    return client().list(prefix, max_keys)


def delete(key: str) -> None:
    client().delete(key.lstrip("/"))


def presigned_url(key: str, expires: int = 3600) -> str:
    """Временная ссылка на чтение (например, чтобы передать картинку в fal)."""
    return client().presigned(key.lstrip("/"), expires)


def _cli() -> None:
    ap = argparse.ArgumentParser(description="Cloudflare R2")
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("upload")
    u.add_argument("local")
    u.add_argument("key", nargs="?")
    d = sub.add_parser("download")
    d.add_argument("key")
    d.add_argument("local")
    ls = sub.add_parser("ls")
    ls.add_argument("prefix", nargs="?", default="")
    pr = sub.add_parser("url")
    pr.add_argument("key")
    pr.add_argument("--expires", type=int, default=3600)
    args = ap.parse_args()
    if args.cmd == "upload":
        print(upload(args.local, args.key))
    elif args.cmd == "download":
        print(download(args.key, args.local))
    elif args.cmd == "ls":
        for o in list_objects(args.prefix):
            print(f"{o['size']:>12}  {o['key']}")
    else:
        print(presigned_url(args.key, args.expires))


if __name__ == "__main__":
    _cli()

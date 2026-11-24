# STYLE_BASE_C — stylised 3D animated-feature volume

Status: v1, 2026-11-24, concept artist. Investor choice: style C. The code source of truth is
`studio/art/style_c/style_base_c.py` (this file mirrors it). The visual bible (§1, §2, §10) is the director's.
Until it is updated, this text replaces the "ink outlines, flat fills" lines of STYLE_BASE for every new image.

## 1. STYLE_BASE_C (append to every image prompt)

```
Stylized 3D CG animated feature film frame, original character and world design. Characters are sculpted 3D models that keep exactly the stylized proportions and facial design of the reference sheets: slightly enlarged eyes and heads, simplified noses, clean graphic silhouettes, translated into soft rounded volumes with clear planes that turn in the light. Skin is soft and matte with gentle subsurface scattering: warm translucency in ears, nose tip and fingertips, warmer cheeks, cooler jaw and temples, freckles painted into the texture, no visible pores. Eyes have a real spherical volume: layered iris colour, a soft shadow from the upper lid, a moist but not glassy surface, one or two soft catchlights, focused gaze. Hair as sculpted grouped locks with fine strand breakup only at the edges and soft back-light through the tips. Lighting is soft global illumination from motivated sources: a large soft key from the window or lantern, warm bounce light from wood and floor filling the shadows, soft contact and ambient-occlusion shadows, a subtle rim light separating figures from the set. Materials use hand-painted simplified textures with tactile breakup: tarred oilskin with matte worn edges, knitted wool, worn linen, wet weathered wood, rope; all surfaces mostly matte, specular highlights small and soft, only wet things shine. Cinematic lens: shallow depth of field, gentle atmospheric haze and depth fog, softer and cooler in the distance. Muted desaturated palette with deep teal-black shadows and cool violet-blue shadows, grounded epic fantasy, subtle film grain.
```

## 2. NEGATIVE_C (image prompts, after "Avoid:")

```
photorealism, photographic skin, realistic skin pores, wrinkles on young faces, uncanny realistic face, glossy plastic look, plastic toy, vinyl figure, shiny waxy skin, porcelain doll, doll eyes, glassy dead eyes, oversaturated colours, neon colours, chibi proportions, bobblehead, video-game cutscene look, low-poly, clay stop-motion, comic book look, ink outlines, black outlines, flat cel shading, hard two-tone shadows, halftone, crosshatching, 2D painting, brush strokes, stiff frontal pose, plain empty background, text, letters, captions, watermark, logo, signature, extra fingers, fused hands, extra limbs, accessories switching sides, mirrored image, magical glow, extra people
```
Per shot, also add the canon side rules as negatives, e.g. `braid on the left side of the picture, two braids,
tag on the jacket, earring in both ears, cap on the boy`.

## 3. Motion (Kling 2.5 TP image-to-video)

Prompt pattern: `Static camera (or one slow move). <2-4 small natural actions, one per character>. <ambient:
dust, breath, hair strands>. Must NOT change: <faces, anchors by side of picture, outfit, room, light>.
No morphing, no face changes, no new objects/people, no cut.`

Negative prompt (`negative_prompt`):
```
morphing, face morphing, identity change, face distortion, melting, warping, flicker, shimmer, plastic sheen, waxy skin, extra limbs, extra fingers, extra people, braid switching sides, accessories appearing or disappearing, costume change, camera cut, fast motion, blur, low quality
```
Tested prompts: `studio/art/style_c/gen_style_c.py` (MOTION dict), results in the 2026-11-24 report.

## 4. How to get real 3D out of NB2 (the important part)

NB2 copies the rendering of its reference images more than it follows the text. 2D Tidemark sheets as refs
pull every result back to 2D (style_alive §3.1). Recipe that worked (`C_final_pell_r1`):

1. **Image 1 = a frame already in style C** (the 3D style anchor). Today: `refs/STYLE_ALIVE/C_final_house.jpg`
   (full set) and `C_final_pell_r1.jpg` (portrait).
2. **Images 2-3 = the 2D identity sheets**, labelled in the prompt "use only to keep identity".
3. Prompt: "match the 3D rendering of image 1 ... build her as the same kind of 3D character model ... render
   a NEW <shot>". Then the subject text with the canon anchors by side of the picture, then STYLE_BASE_C, then
   "Avoid:" + NEGATIVE_C.
4. Once the C masters exist, they replace the 2D sheets as identity refs, and the 2D sheets retire from
   prompts (keep them in the repo as design history).

A conversion edit of an existing frame ("convert image 1 to 3D") is safe for staging but gives only a partial
step toward 3D (`C_final_pell` vs `C_pell`). Use it for staging, not for masters.

## 5. Rules for C masters

- Master = 3/4 view, natural lit (soft key + bounce + rim), simple neutral set; plus a flat-lit **ID sheet**
  (front / 3/4 / profile / back on mid-grey) for identity. Never a plastic-white studio look.
- Skin is matte; specular only on eyes and wet surfaces. Freckles in texture, no pores.
- Keep the 2D design proportions: young faces stay young (C tends to age and thicken faces: check every take).
- Eye colour: Pell sea-grey, never clear blue (C drifts to blue; put "sea-grey, not blue" in the prompt).
- Hair colour: Pell rust-brown, not orange (C drifts to orange under warm light).

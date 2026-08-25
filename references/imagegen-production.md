# Imagegen References and Production Assets

Use this reference after official/supplied asset inventory and before implementation.

## 1. Routing

### Imagegen Frontend Web

Run only when `policy-matrix.md` resolves it on. Typical signals are visual ambiguity, image-led direction, requested concepts, or insufficient approved assets. Typography-led greenfield pages and asset-rich redesigns may skip it with a recorded rationale.

Follow its contract:

- announce the selected section count;
- generate one separate horizontal reference per selected section;
- keep one brand world across all references;
- vary composition, background mode, density, and image-to-text balance;
- inspect every reference and regenerate weak or drifting sections.

Do not flatten generated website comps into production sections. They are design references, not the final website.

### Imagegen Frontend Mobile

Never use it to design the website’s responsive breakpoint. Separate three cases: verified real screenshots; deterministic UI mockups built from approved product specifications; and clearly labelled conceptual app visuals. Imagegen Mobile is allowed only for the conceptual case or approved product-screen concepts. Never imply generated screens are verified functionality.

### Production image generation

Use the available image-generation capability or `media-use` after art direction is locked to create actual website assets: photography, backgrounds, product scenes, illustrations, textures, isolated objects, and app/product visuals.

## 2. Image opportunity pass

For each section decide: preserve, extract, generate, license, or omit. Generate only when it materially improves comprehension, emotion, credibility, product demonstration, or brand recall.

Judge asset coverage by narrative utility, visible repetition, brand specificity, and page balance rather than quotas. Typography-only and asset-rich restrained directions are valid when deliberate. Reject accidental text-heavy, repeated-crop, or stock-generic outcomes.

## 3. Prompt contract for production assets

Specify:

- asset job and section;
- subject, environment, camera/crop, lighting, mood, palette, material treatment;
- exact aspect ratio and expected display size;
- desktop/mobile crop strategy;
- explicit text-safe region where required;
- continuity with the project brand guide;
- exclusions: no words, logos, buttons, cards, charts, signatures, watermarks, or invented products/claims. UI is excluded except for the narrowly routed, clearly labelled conceptual-app-screen case.

Generate one asset per call when independent control matters. Preserve the strongest approved style anchor when the tool supports references.

## 4. Hard integrity rules

Never generate or alter:

- client logos or partner marks;
- identity-critical portraits when likeness cannot be preserved;
- real product details that must remain accurate;
- conceptual or deterministic mockups presented as actual product state; label them clearly and never imply verified functionality;
- charts, metrics, testimonials, certifications, awards, or credentials;
- regulated evidence or before/after outcomes.

Use supplied originals when identity or factual geometry matters.

## 5. Production compositing

Generated imagery is visual material, not a finished interface. Add exact copy, logos, UI, CTA, data, diagrams, and accessibility text deterministically in code/design software.

Do not rescue a busy image by covering it with arbitrary blur cards or dark rectangles. Regenerate/reframe/crop the source so the text-safe region is naturally usable.

## 6. QA every asset

Inspect at full resolution and final display size:

- anatomy, faces, hands, products, architecture, perspective;
- fake text, fake UI, watermarks, signatures;
- brand palette and image grade;
- subject crop and text collision;
- desktop/mobile crop quality;
- resolution, compression, noise, banding, and sharpness;
- consistency with other page imagery.

Reject weak assets. Do not accept the first render merely because it exists.

## 7. Optimisation and delivery

- retain original generation/source;
- create intentional crops rather than relying on accidental `object-fit`;
- export WebP/AVIF or appropriate compressed formats;
- reserve width/height or aspect ratio to prevent layout shift;
- preload the LCP hero when appropriate;
- lazy-load below-fold media;
- write alt text from the final image, not the prompt;
- record prompt/intent, provider/tool, source path, dimensions, crop use, final path, and provenance in the manifest.

## 8. Failure path

If image generation is unavailable or blocked, use verified official assets or properly licensed photography and report the gap. Never substitute CSS blobs, fake screenshots, random nearby files, or invented brand art.
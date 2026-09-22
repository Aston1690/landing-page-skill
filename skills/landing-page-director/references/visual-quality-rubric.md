# Visual quality rubric

Score each category from 0 to 2 after inspecting the real rendered page.

- **0 — Fails:** material defect, generic/unresolved design, or missing requirement
- **1 — Passes:** competent and usable but has visible weaknesses
- **2 — Premium:** intentional, coherent, distinctive, and well executed

## Categories

### 1. Strategic clarity

The page communicates who it is for, what it offers, and what action to take without relying on invented proof.

### 2. Visual concept

The selected direction is recognisable across the entire page. The design has a project-specific idea beyond “modern and clean”.

### 3. Typography

Font choice, scale, weight, line length, wrapping, and hierarchy support the brand and remain readable at every width. Display type feels intentional at normal viewing size and does not crowd the first viewport.

### 4. Colour and surfaces

Colour roles are controlled, accessible, and brand-relevant. Borders, radii, shadows, and surfaces form one system.

### 5. Composition and rhythm

Sections vary purposefully while maintaining continuity. Density and whitespace create hierarchy rather than emptiness. Numbers, rules, borders, icons, and adjacent copy have deliberate optical clearance.

### 6. Imagery and iconography

Images are relevant, high resolution, well cropped, and consistently treated. Icons belong to one visual family.

### 7. Conversion path

The primary action is visible at the right moments, copy supports user readiness, and controls actually work. The final conversion section has distinct visual weight and does not read like an unfinished text block.

### 8. Responsive behaviour

Desktop, tablet, and mobile feel intentionally composed. There is no overflow, clipping, awkward wrapping, or lost functionality.

### 9. Motion and interaction coherence

Motion has a recognisable brand character, supports hierarchy or understanding, and uses consistent timing and easing. Scroll effects remain controlled on desktop and adapt intentionally on smaller or lower-power devices.

Missing default motion without a documented valid exemption scores 0. Planned motion that was not watched in a real browser at desktop/mobile, or lacks reduced-motion verification, remains unverified and cannot pass from still screenshots.

### 10. Accessibility and interaction

Semantics, keyboard use, focus, contrast, motion preferences, form states, and media alternatives are handled.

### 11. Factual and implementation integrity

No unsupported claims, fake interfaces, source-brand leftovers, broken assets, inert controls, or console failures remain. Logos use the correct approved asset, background treatment, and optical scale.

## Premium gate

- Maximum score: 22
- Minimum handover score: 18
- No category may score 0
- Strategic clarity, responsive behaviour, accessibility, and factual integrity must each score 2 for production release

Record weaknesses and correct them before rescoring. A score is evidence, not decoration; cite the rendered width, component, or test that supports it.

Before awarding a premium score, answer these binary checks from the rendered page:

- Does the hero have one dominant message and one dominant action without competing clutter?
- Is the logo visually subordinate to the navigation and free of an accidental background patch?
- Are headline sizes comfortable at 1440 and 390 pixels rather than merely dramatic in a design board?
- Are numbered or divided patterns optically spaced away from their rules?
- Is the conversion section unmistakably prominent without relying on meaningless ornament?
- Has every treatment rejected during revision been removed from all shared components and sections?

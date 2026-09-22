# Premium Design Quality Gate

This reference is authoritative for scoring. A build passing is not a design pass.

## 1. Binary critical checks

Every applicable check requires evidence and must pass before scoring:

- verified logo/assets and no source-brand remnants;
- no invented/unverified claim presented as fact;
- real CTA destination and no fake form success;
- no horizontal overflow, clipping, broken media, console/network errors;
- hero offer and primary action understandable in the first viewport;
- readable typography with justified font choice and controlled wrapping;
- coherent component grammar and no visibly repetitive template system;
- deliberate responsive composition at risk-based viewports/breakpoints;
- safe integration testing with no unapproved live side effects;
- when motion exists: no stuck opacity, trigger drift, missing cleanup, or reduced-motion failure;
- full-resolution screenshot/DOM/test evidence rather than contact-sheet impressions.

Any failed critical check fails the page regardless of score.

## 2. Evidence format

For each category record:

- score: `0`, `5`, `8`, `10`, or `N/A`;
- rationale;
- evidence: screenshot path/URL, DOM/computed-style result, audit output, test result, asset/source record, or deployment verification;
- defect found;
- fix applied and recheck result.

`N/A` is permitted only with written rationale. For a deliberate static page, Motion may be `N/A` if restraint, interaction feedback, reduced-motion/static safety, and mode routing are verified. Do not average `N/A` categories.

## 3. Universal anchors

- `0`: missing, broken, deceptive, inaccessible, or unreviewed.
- `5`: functional but generic/inconsistent; obvious professional rework required.
- `8`: professional and evidence-backed; minor non-critical improvements remain.
- `10`: exceptional, brand-specific, fully verified, and materially stronger than standard category work.

Do not assign unsupported intermediate numbers merely to pass.

## 4. Categories

### A. Brand specificity

- 5: correct logo/colours but reusable template direction.
- 8: coherent, brand-faithful thesis with identifiable signature.
- 10: unmistakably this brand; source-faithful and memorable without imitation.

### B. Conversion and narrative

- 5: sections exist but pacing/CTA/proof feels assembled.
- 8: clear offer, one conversion path, purposeful section jobs.
- 10: value understood in seconds; proof, objections, and CTA arrive with exceptional timing.

### C. Typography

- 5: readable but generic, oversized, condensed, weakly wrapped, or inconsistent.
- 8: justified type roles, controlled line breaks, hierarchy, width, weight, and rhythm.
- 10: typography is a memorable brand material while remaining effortless to read at every viewport.

### D. Composition and spacing

- 5: repetitive slabs/cards, congestion, dead space, or accidental alignment.
- 8: controlled grid, rhythm, variety, and purposeful negative space.
- 10: every viewport feels deliberately composed with distinctive but coherent pacing.

### E. Imagery and art direction

- 5: generic stock, repeated crop, decorative filler, or weak integration.
- 8: verified/generated imagery is coherent, useful, well-cropped, and production-ready.
- 10: imagery carries narrative and brand recall with exceptional direction and technical finish.

### F. Component craft

- 5: default/mixed components, inconsistent radii/CTAs/states.
- 8: precise shared grammar across navigation, controls, forms, cards, icons, and states.
- 10: every detail feels custom to the brand while remaining accessible and maintainable.

### G. Responsive design

- 5: desktop stacked down with awkward order/crops/touch behavior.
- 8: deliberate reflow across user viewport, breakpoint boundaries, tablet, narrow and common mobile.
- 10: each tested viewport feels independently art-directed with no compromise in conversion or readability.

### H. Motion

- 5: generic fade spam, distracting timing, missing accessibility, or quota-driven effects.
- 8: purposeful, coherent, responsive, accessible, and performance-safe.
- 10: brand-specific choreography materially improves hierarchy/story/feedback.
- N/A: policy-approved static mode with evidence of deliberate restraint and safe static interaction states.

### I. Accessibility and integrity

- 5: partial semantics/contrast/focus/labels or weak provenance.
- 8: semantic, keyboard, focus, contrast, labels, alt text, reduced motion, factual and asset integrity pass.
- 10: exemplary inclusive behavior plus independently clear approval/verification/provenance records.

### J. Performance and production readiness

- 5: heavy/unoptimised assets, CLS, unresolved integration, incomplete SEO or weak source notes.
- 8: optimised media/fonts/JS, reserved dimensions, clean console, working safe integrations, SEO/OG and provenance.
- 10: measured excellent delivery, complete handoff, and verified live behavior when deployment is requested.

## 5. Passing rule

- Every binary critical check passes.
- No applicable category below 8.
- Target applicable-category average: 9+.
- Fix the weakest applicable category, recapture/retest, then rescore.

## 6. Required evidence coverage

Inspect:

- user’s actual viewport;
- every layout breakpoint boundary;
- one tablet;
- one narrow mobile and one common mobile (375/390 are defaults, not mandatory if better risk widths exist);
- first fold, multiple mid-page sections, final CTA/footer;
- active/resting motion and reduced motion when applicable;
- menus, forms, accordions, tabs, carousels, anchors, keyboard/focus;
- broken-image, overflow, console, network, CLS and destination checks;
- exact live alias at desktop/mobile when deployed.

## 7. Self-rejection

Ask bluntly:

- Could this be reskinned for another company?
- What is the single memorable brand-specific decision?
- Which section/category is weakest and what evidence proves it?
- Is any type too large, narrow, faint, wrapped, or generic?
- Is imagery carrying meaning or filling boxes?
- Is mobile designed or collapsed?
- Is motion justified or ceremonial?
- Are approval and factual verification being confused?
- Are there remnants, placeholders, fake states, or unapproved side effects?

A user rejection such as “basic,” “generic,” or “bad” invalidates the current art direction. Stop micro-tweaking, reset the thesis/reference/first fold, rebuild, and rerun the gate.
## Default motion completion gate

For full builds, missing planned hero/section choreography or control micro-interactions fails acceptance unless an explicit mode exception is recorded. Read `QA/motion-review.md` and compare the storyboard to real desktop/mobile runtime observations and reduced-motion results. Dependency presence and still screenshots are not motion evidence. Never use N/A because animation was not separately requested.

# Feedback calibration

Read this reference whenever a user annotates the page, rejects a section, or says that the design does not feel right. Convert subjective feedback into durable design constraints and choose the right size of revision.

## 1. Separate the signal from the symptom

Record each item in a compact rejection ledger inside `DESIGN-BRIEF.md`:

| Feedback | Design signal | Required change | Scope | Verified at |
|---|---|---|---|---|
| User's words or annotation | Hierarchy, density, scale, spacing, asset, composition, motif, motion, or functionality | Observable correction | Token, component, section, or direction | Relevant viewport(s) |

Keep the user's wording. Do not turn “I do not like this section” into a minor colour adjustment without evidence.

## 2. Interpret common feedback precisely

- **“The font is too huge”** — Reduce the display scale and often its measure; restore contrast with weight, spacing, or composition instead of another oversized element. Recheck line wrapping and the complete first viewport at desktop and mobile.
- **“The hero is crowded”** — Establish one message and one primary action. Reduce simultaneous labels, proof, copy blocks, imagery, and decorative devices; defer secondary evidence below the fold. A two-column layout can still be crowded.
- **“The CTA is too simple”** — Redesign the conversion moment through contrast, framing, layout, supporting reassurance, and strong action hierarchy. Do not solve it with random icons, gradients, glow, or a giant rounded container.
- **“The logo is too big”** — Reduce its optical footprint and header height while maintaining legibility. Judge the visible mark, including transparent padding, rather than trusting the bitmap dimensions.
- **“Remove the white background from the logo”** — Use the approved transparent asset or properly prepare the asset. Do not disguise a baked-in background with a white box, blend mode, crop, or filter.
- **“The number is too close to the line”** — Increase optical clearance around the number and divider relationship and check every instance of the shared pattern. Fix the component or token when the defect repeats.
- **“I do not like this section”** — Treat this as a composition rejection. Produce a materially different arrangement while preserving the approved visual language and locked copy; changing only colour, radius, or shadow is insufficient.
- **“Remove this tick or mark”** — Remove the motif and record it as rejected so it does not reappear as decoration in another section. Retain only symbols with semantic, brand, or interaction value.

## 3. Choose the revision level

### Local correction

Use when the concept is accepted and the feedback names a concrete defect such as spacing, crop, scale, background treatment, or a single unwanted detail. Search for the same component or token elsewhere and correct all unintended repetitions.

### Section redesign

Use when the user rejects a section's composition, density, hierarchy, or prominence. Return to a section reference and create a genuinely different arrangement. Review it autonomously before translating it back into code unless the user requested a visual approval checkpoint.

### Direction reset

Use when the user rejects the design overall or asks to start from scratch. Stop polishing the rejected layout. Preserve only locked copy, factual content, approved brand assets, technical constraints, and explicitly liked elements. Create fresh visual references with different composition logic before replacing the implementation.

## 4. Validate the revision visually

Do not close an annotation from code inspection alone.

- Reopen the exact viewport and surrounding section where the issue was reported.
- Compare before and after in context, including adjacent elements and the fold.
- Check the shared pattern throughout the page when a token or reusable component changed.
- Verify 1440 and 390 pixels for hero, header, CTA, and typography changes; add other breakpoints when the component transforms there.
- For logo changes, inspect transparency, intrinsic padding, optical size, and contrast against every surface where the logo appears.
- For density changes, verify reading order and confirm that essential copy and the primary action remain visible and understandable.
- For motion changes, verify timing on first load and scroll, mobile adaptation, and `prefers-reduced-motion`.

## 5. Carry learning forward without overfitting

Distinguish between:

- **Project-specific rejection:** a particular tick, image, layout, colour, or motif. Keep it in that project's rejection ledger.
- **Reusable quality principle:** avoid accidental logo backgrounds, cramped divider spacing, oversized type without hierarchy, crowded first viewports, weak conversion moments, and cosmetic patching after a composition has been rejected.

Use the reusable principles as default review gates. Do not assume every future client wants the same typography, density, section order, colour palette, or hero structure.

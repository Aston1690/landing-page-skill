# Design brief schema

If an executable design harness is installed, use its configured canonical brief template and preflight. Populate it from inspected sources, distinguish facts from assumptions and define evidence and failure conditions. Otherwise maintain the brief below as the canonical project record.

Use the following headings as supporting design notes or a generated human-readable view of that brief. Do not maintain contradictory parallel objectives. Keep it specific enough that another designer or engineer could continue the work without reopening basic art-direction decisions.

## 1. Objective

- Page purpose
- Primary audience
- Primary conversion
- Secondary conversion
- Success signal

## 2. Source-of-truth inputs

- Client name and current website/source-page URL
- Approved copy source
- Copy status: approved, draft, requires writing, or unavailable
- Brand kit and logo source
- Approved assets
- Asset inventory: logos, fonts, imagery, video, icons, illustrations, diagrams, product/UI captures, proof, and legal/compliance material
- Known licensing or usage restrictions
- Reference URLs or files
- Existing repository or platform source
- Technical/project constraints
- Missing or inaccessible sources and their effect on the work

## 3. Locked decisions

- Selected direction and why
- Content that must not change
- Required section order
- Required functionality
- Prohibited claims or treatments

## 4. Visual concept

- Direction name
- One-sentence concept spine
- Desired audience impression
- Composition principles
- Deliberate tension or distinctive device
- Treatments to avoid
- Visual benchmark URL/file or concrete composition target; which observable qualities matter and which must not be copied
- Imagery, iconography and motion decisions, including reasons for deliberate omission

## 5. Typography

- Display family, source, weights, fallback
- Body family, source, weights, fallback
- Display scale and line-height
- Body scale and line-height
- Labels, captions, and numerals
- Mobile type transformations

## 6. Colour tokens

Record values and roles for:

- Background
- Foreground
- Muted foreground
- Primary accent/action
- Accent foreground
- Surface/card
- Border/separator
- Focus ring
- Success, warning, and error when applicable

Use semantic names rather than colour-number names alone.

## 7. Layout system

- Maximum content width
- Page gutters at desktop/tablet/mobile
- Column grid
- Spacing rhythm
- Section density and transitions
- Radius levels
- Border and shadow levels

## 8. Section map

For every section specify:

- Narrative purpose
- Content source
- Composition
- Primary visual
- CTA or interaction
- Desktop behaviour
- Tablet behaviour
- Mobile behaviour
- Reference-image filename

## 9. Imagery and iconography

- Image type and subject rules
- Art direction, crop, lighting, texture, and colour treatment
- Real versus generated asset policy
- Resolution and aspect-ratio requirements
- Icon family, stroke/fill style, and prohibited mixtures
- Alt-text approach

## 10. Components and interactions

- Navigation
- Buttons and links
- Forms
- Cards or panels
- Media controls
- Accordions, tabs, modals, or carousels
- Hover, focus, active, loading, success, and error states
- Reduced-motion behaviour

## 11. Motion system

- Three to five brand-motion words
- Motion purposes: hierarchy, explanation, feedback, continuity, or narrative emphasis
- Duration, easing, stagger, distance, scale, and repetition tokens
- GSAP choreography by default for full builds; technology choice and any concrete exemption
- Planned hero, section and control behaviours with observable motion acceptance criteria
- Runtime evidence location (`QA/motion-review.md`) and failure conditions
- One or two signature moments, if justified
- Section-by-section trigger and choreography map
- Scroll-linked, pinned, autoplay, cursor, or looping behaviour and its constraints
- Mobile and low-power adaptations
- `prefers-reduced-motion` result for every non-trivial sequence
- Cleanup, progressive enhancement, and no-JavaScript fallback expectations

## 12. Responsive transformations

Document intentional changes at 1440, 1024, 768, 390, and 320 pixels. Include reading order, type size, wrapping, grid collapse, imagery crop, navigation, CTA placement, and hidden elements.

## 13. Accessibility

- Landmark and heading structure
- Keyboard path
- Focus visibility
- Contrast targets
- Form labelling and errors
- Motion and media alternatives

## 14. Factual integrity

- Verified claims and sources
- Claims requiring confirmation
- Placeholder policy
- Privacy-sensitive assets or data

## 15. Approval status

- Approved decisions
- Pending decisions
- Approver and date when known
- Agent-selected decisions versus actual user approvals; whether visual checkpoints were requested
- Model and reasoning setting when available, otherwise unknown (do not infer from output quality)

## 16. Feedback and rejection ledger

For each revision round record:

- User's exact feedback or annotation
- Design signal: hierarchy, density, scale, spacing, asset, composition, motif, motion, or functionality
- Required observable correction
- Scope: token, component, section, or direction
- Rejected treatment that must not be reintroduced
- Viewport and evidence used to verify the correction

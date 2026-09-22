---
name: landing-page
description: "Build complete landing pages, sales/campaign pages, one-page marketing sites, and homepage redesigns with one-question-at-a-time intake, exact user-supplied copy, official-site brand/logo extraction, conditional Imagegen and default purposeful GSAP choreography, risk-based responsive QA, a hard premium gate, and default Vercel deployment with live verification. Also use when converting user-provided URLs/docs/PDFs/briefs into those marketing surfaces. Do not use for dashboards, native-app UI, documentation, email templates, or isolated component-only fixes."
license: MIT
metadata:
  version: 3.3.0
  author: Akhil
  hermes:
    tags: [landing-pages, frontend-design, image-generation, gsap, responsive-web, browser-qa, vercel]
---

# Landing Page Builder

Build the finished page, not a prompt, wireframe, moodboard, or partial sample. Deliver working code backed by real browser QA. Premium quality means brand-specific decisions, excellent typography/composition/imagery, conversion clarity, responsive craft, purposeful motion, accessibility, performance, and factual integrity.

At invocation, read `metadata.version` above and record `landing-page v<version>` in the project brief. Repeat that exact version in the completion report so every generated landing page remains traceable to the skill release that produced it.

## Hard output contract

Deliver:

- a complete responsive implementation in a new or explicitly approved existing project;
- exact user-supplied copy preserved verbatim; write, edit, or restructure copy only when the user explicitly asks;
- a working brand system, asset manifest/provenance notes, and integration notes;
- production imagery rather than placeholders when image generation or approved assets are available;
- purposeful GSAP choreography, scroll-triggered section movement and control micro-interactions by default for full builds, subject to the documented mode exceptions;
- SEO/OG metadata, semantic structure, accessibility states, and optimised media;
- browser-tested user viewport, breakpoint boundaries, tablet, narrow mobile, and common mobile states;
- Vercel deployment by default, followed by live desktop/mobile verification; ask only when authentication or another real blocker prevents deployment.

Never invent claims, metrics, credentials, testimonials, customer logos, regulated wording, products, screenshots, contact details, or form success.

## Required skill routing

Load before building:

1. `frontend-design` for brand-specific art direction and visual thesis.
2. `design-taste-frontend` for anti-slop implementation and responsive preflight.
3. `imagegen-frontend-web` only when the authoritative mode matrix resolves it on: visual ambiguity, image-led direction, requested concepts, or insufficient approved assets.
4. This `landing-page` skill for orchestration, build, QA, and delivery.
5. The available production image-generation capability or `media-use` when the official/supplied asset inventory cannot support the approved visual direction.
6. `imagegen-frontend-mobile` only for clearly labelled conceptual app-screen media or approved product-screen concepts on a mobile-app marketing page. Never use it to design responsive mobile web or imply generated screens are verified product functionality.

Read `references/frontend-skill-stack.md` for stack conflict rules.

## Project-mode decision

Read `references/policy-matrix.md`. It is the single authoritative source for Imagegen, GSAP, preservation, approval, integration safety, viewport coverage, and quality-gate routing. Select exactly one of its six modes and record the resolved decisions plus rationale. No prose elsewhere may override the matrix.

When the user says “from scratch” or “do not touch previous builds,” create a uniquely named project and never edit prior work.

## Phase 1: Invocation intake

Ask one short question at a time. Never combine several fields into a paragraph or questionnaire. Wait for the answer before asking the next genuinely required question.

Use this order, skipping anything already supplied or safely inferable:

1. What company/product and official website is this for?
2. Where is the final user-approved copy? Copy is required and preserved exactly.
3. Where are the brand guide, logo and approved assets, if they exist?
4. Is this a new separate build or an existing project edit?
5. Ask about audience, CTA destination, integration or compliance only if the supplied site/copy does not answer it and it materially blocks implementation.

Do not ask whether copy can be rewritten. Do not offer to write or change copy. Writing, editing or restructuring is enabled only by an explicit user request. Do not ask whether to deploy; Vercel deployment is the default.

Read `references/intake-brand-assets.md` and follow its source hierarchy, logo recovery, brand-guide fallback, compliance, integration, and provenance rules.

## Phase 2: Evidence and brand audit

After intake:

1. Read project instructions, approved brief/content, prior approvals, and supplied references.
2. Open the official website in a real browser when one exists; otherwise record the new-brand/no-site condition and continue from supplied context.
3. Extract computed fonts/colours, logo variants, spacing, grid, radii, buttons, icons, imagery, navigation, forms, footer, responsive behaviour, and motion.
4. Recover and visually verify an official SVG or transparent high-resolution PNG logo. If an existing logo is unavailable, ask the user for it. If no logo exists, confirm whether a plain-text product-name treatment is acceptable and record that logo design is outside scope. Never redraw or generate a client logo.
5. Extract document text and images together; preserve image-to-copy relationships.
6. Create a verified asset manifest.
7. If no brand guide exists, create a compact agent-authored project guide and label it honestly.

For regulated/trust-sensitive work, preserve supplied disclaimers, licences, award wording, eligibility, consent, and qualifications unless edits are explicitly authorised.

## Phase 3: Content and conversion architecture

Create a content manifest before design:

- source-backed headline/body/CTA/claim for each section;
- section job: hook, explain, prove, differentiate, answer, or convert;
- evidence source or unresolved placeholder;
- intended visual/media and asset status;
- primary conversion path and CTA destination.
- `approval_status` and `verification_status` tracked separately for factual claims, testimonials, metrics, credentials, and regulated wording.

Default content policy is exact preservation of user-supplied copy. `authorized_editing` or `agent_draft_unapproved` may be selected only when the user explicitly requests editing or writing. Agent drafts remain unapproved and cannot contain unsupported claims.

Use only sections that answer a real conversion question. Do not mechanically include hero + trust + three cards + testimonials + FAQ. One primary idea per section. Preserve approved IA in existing projects unless authorised to change it.

## Phase 4: Design brief and Imagegen

Write the pre-code brief:

- audience, conversion goal, source of truth, project mode;
- one subject-specific visual thesis and narrative spine;
- palette, typography roles, grid/spacing, shape/component grammar;
- image grade, asset map, image-generation plan, signature element;
- desktop/tablet/mobile first-fold and complex-section behaviour;
- motion storyboard with a purpose for each sequence;
- explicit avoid-list and acceptance criteria.

Reject the direction if it could be reused unchanged for an unrelated brand.

When the policy matrix resolves Imagegen on, read `references/imagegen-production.md`:

1. Use `imagegen-frontend-web` and announce the selected reference count.
2. Generate and inspect one separate horizontal reference for every selected section.
3. Keep one brand world while varying composition and density.
4. Lock the direction through either a user checkpoint (requested/consequential trade-off) or an agent acceptance gate (autonomous, reversible, source-backed). Record which approval mode was used.
5. Generate/resolve production assets separately at real aspect ratios without baked-in text, logos, claims, or watermarks. UI is excluded except for the policy-routed, clearly labelled conceptual app-screen case.
6. Inspect, crop, optimise, add alt text, and record provenance.

Judge imagery by narrative utility, visible repetition, brand specificity, and asset quality rather than quotas. A deliberate typography-led or asset-rich page may skip generation with a recorded rationale; an accidentally text-heavy or stock-generic page fails.

## Phase 5: Static implementation and approval

Choose the simplest stack that satisfies the brief:

- preserve an existing repository’s framework, styling, routing, components, analytics, and asset pipeline;
- use semantic HTML, external CSS, and external JS for genuinely static pages;
- use React/Vite/Next only when existing architecture, reusable components, integrations, state, or complex interaction justifies it;
- verify dependencies before importing them.

Complete the static page before motion. It must already have:

- correct copy, verified logo/assets, real CTA destinations;
- coherent tokens and component grammar;
- controlled typography and line breaks at the user’s viewport;
- enough compositional variety to avoid visible repetition, without numerical layout quotas;
- intentional image crops and reserved dimensions;
- working navigation, forms/links, focus and interaction states;
- deliberate responsive reflow rather than accidental stacking;
- no broken media, overflow, clipping, fake UI, placeholders, or source remnants.

Screenshot-QA and fix the static composition before starting GSAP.

## Phase 6: GSAP production pass

Read `references/gsap-motion.md` for every full build and substantial redesign; plan motion in the brief and implement it after static composition QA.

Motion is on by default for full builds under the policy matrix. Deliver hero choreography, content-specific section movement and feedback for existing interactive controls. Adapt intensity to the brand. A valid static/runtime/preservation constraint may change this; absence of an explicit animation request is not a reason to skip. Record runtime observations in `QA/motion-review.md`; screenshots alone cannot pass motion acceptance.

Keep critical content visible if scripts fail or load slowly. Do not use raw window scroll listeners. Verify active-tab animation because background tabs throttle timers.

## Phase 7: Browser QA

Run the page locally and inspect real screenshots and state:

- user’s actual viewport, every layout breakpoint boundary, one tablet, one narrow mobile, and one common mobile; 375px/390px are defaults rather than universal requirements;
- first fold, multiple mid-page sections, final CTA/footer;
- active and resting motion states plus reduced motion;
- menus, anchors, forms, accordions, tabs, carousels and keyboard use;
- computed font families/weights where typography matters;
- image load/natural dimensions, crop, alt text;
- horizontal overflow, clipping, console/network errors, CLS risks;
- form/CTA destination and success/error behaviour. Use sandbox/test endpoints and synthetic data. Never submit live leads, CRM records, payments, emails, or analytics events without explicit approval.

Fix defects before handoff. A build passing is not design QA.

## Phase 8: Premium quality gate

Read `references/premium-quality-gate.md` and score with evidence:

1. Brand specificity
2. Conversion and narrative
3. Typography
4. Composition and spacing
5. Imagery and art direction
6. Component craft
7. Responsive design
8. Motion
9. Accessibility and integrity
10. Performance and production readiness

Use binary critical checks plus evidence-backed 0/5/8/10 anchors. No applicable category may score below 8/10; target 9+ overall. `N/A` is allowed only with written rationale, including motion on a deliberate static page. Cite screenshot, DOM, audit, or test evidence for every score. Any critical rejection criterion fails the page regardless of average. Fix the weakest applicable category, rerun evidence, and rescore.

If the user calls the work basic, generic, or bad, invalidate the current art direction. Stop micro-tweaking, identify the systemic cause, reset the thesis/reference/first fold, rebuild, and re-QA.

## Phase 9: SEO, performance, and deployment

Before delivery:

- one H1, logical heading structure, title, description, canonical, OG metadata and favicon;
- responsive optimised images, hero priority/preload where appropriate, lazy below-fold media;
- maximum two justified font families and only required weights;
- semantic elements, labels, alt text, contrast, focus, keyboard and reduced-motion support;
- no fake integrations, unverified claims, console errors, broken links, or unresolved secrets;
- source notes with copy/assets/logo/imagegen/integration provenance.

Deploy every completed landing page to Vercel by default using the project’s existing Vercel configuration or an isolated new project name. If authentication, ownership, secrets or another real blocker prevents deployment, ask only for that blocker. Verify the exact live alias in a real browser at desktop and mobile; check title/content markers, assets, navigation, forms, overflow, console, motion, and alias ownership. CLI success or HTTP 200 alone is not proof.

## Anti-slop rejection list

Reject:

- generic purple/blue AI gradients, blobs, meaningless glass cards, floating 3D filler;
- unrelated stock handshakes, fake dashboards, invented charts/KPIs, fake social proof;
- oversized or condensed headings without brand reason, tiny body text, awkward wraps;
- identical three-card rows, repeated layout families, excessive pills/radii/shadows;
- copy such as “revolutionize,” “unleash,” “next-generation,” “seamlessly,” or vague CTA labels;
- generated words/logos/UI inside production imagery;
- mobile that is merely desktop stacked vertically;
- animation used to conceal weak static design;
- decorative elements whose only job is filling space.

Prefer verified brand assets, subject-specific imagery, controlled typography, varied but coherent composition, one memorable signature, purposeful negative space, clear proof, and one decisive conversion path.

## Reference map

| Need | Read |
|---|---|
| Authoritative project-mode routing | `references/policy-matrix.md` |
| Intake, site/brand/logo/content/assets/integrations | `references/intake-brand-assets.md` |
| Frontend stack routing/conflicts | `references/frontend-skill-stack.md` |
| Imagegen references and production imagery | `references/imagegen-production.md` |
| GSAP implementation and QA | `references/gsap-motion.md` |
| Premium scoring/rejection gate | `references/premium-quality-gate.md` |
| Optional section implementation patterns | `references/section-patterns.md` |
| Legacy detailed verification checklist | `references/verification-checklist.md` |

## Completion statement

When handing off, state:

- exact `landing-page` skill version used, copied from `metadata.version`;
- project path and implementation stack;
- source-of-truth copy and brand/asset provenance;
- image references/production assets created and unresolved items;
- GSAP mode and reduced-motion behaviour;
- viewports and interactions tested;
- premium-gate category scores and weakest item fixed;
- live-verified Vercel URL, or the precise authentication/blocker preventing deployment.

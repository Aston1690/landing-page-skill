---
name: landing-page-director
description: Design, build, redesign, animate, or art-direct premium marketing landing pages, campaign pages, one-page sales sites, and visually led homepages through source-material intake, guided one-question-at-a-time design decisions, named visual directions, a locked design brief, image-first section references, brand-led motion direction, implementation, and responsive visual QA. Use whenever a user asks for a landing page or marketing website where visual quality, brand coherence, motion, or conversion matters, including vague requests with no supplied context, “make this landing page look premium”, “add polished scroll animation”, and URL-led redesigns. Do not use for dashboards, native mobile apps, document/PDF design, email templates, isolated components, or narrowly scoped bug fixes.
---

# Landing Page Director

Create landing pages through explicit design decisions rather than freeform styling. The quality comes from sequencing: understand the brief, narrow the visual direction, lock a system, create references, translate them faithfully, and inspect the rendered result.

This skill owns the landing-page workflow. Supporting image, translation, testing, brand, copy, or framework skills may contribute specialist work, but they must not replace this workflow or introduce a second competing art direction.

## Default execution

Use this director for art direction and the complete build/review loop. If `design-harness` is installed and configured, load it for isolated implementation, saved context, browser evidence and bounded revision. Otherwise perform and record these stages directly; do not claim executable harness checks ran. The user need not invoke a second skill. A child assigned a single stage must return to its parent without starting another orchestration loop.

## Compatibility

Use built-in image generation for visual references and a browser-capable inspection tool for final visual QA. Coordinate `imagegen-frontend-web`, `image-to-code`, `brand-consistency`, and `playwright-visual-testing` when they are available. Default to GSAP choreography for full landing-page builds and substantial redesigns, with CSS for local interaction feedback. Respect explicit static requests, preservation constraints and existing required motion systems.

## Core contract

- Treat approved copy, factual claims, logos, brand assets, page order, and source-template requirements as locked.
- Ask for the client website, content source, brand guide, logos, fonts, supplied media, product visuals, and relevant references when they are not already available; never assume that no source material exists merely because none was attached to the first message.
- Read and inventory every supplied document, URL, image, brand file, and repository source before proposing art direction.
- Never invent statistics, testimonials, awards, clients, certifications, locations, contact details, product screens, or proof.
- Make missing information visible with `[TO BE CONFIRMED]` when it cannot be safely omitted.
- Establish one coherent visual language before implementation.
- Own routine art-direction and reference-selection decisions unless the user requests visual approval checkpoints. Record agent-selected references honestly; never call them user-approved. Escalate content uncertainty and conflicts with locked requirements, not ordinary design choices.
- Favour controlled, readable hierarchy over spectacle: a premium result must not depend on giant type, crowded heroes, ornamental marks, or oversized branding.
- Treat motion as part of that visual language: give it a purpose, personality, timing system, and reduced-motion counterpart.
- Use exactly one primary taste direction. Do not blend several style skills or moodboards.
- Generate and critically review visual references before coding when visual quality is central.
- Build a working page, not a static-looking mock-up with inert controls.
- Inspect the real rendered page at desktop and mobile widths before reporting completion.

## Workflow state machine

Follow the stages in order. Skip a stage only when the user has already supplied everything that stage would establish. Do not ask the user to repeat information already present in the brief, files, conversation, brand kit, or reference URL.

### 1. Read and classify the brief

Inventory everything already present in the conversation and workspace before asking the user for anything. Read [guided-intake.md](references/guided-intake.md) and run its source-material preflight when the source set is missing or incomplete.

The source inventory covers:

- Client name, current website or source-page URL, and whether the task is a new page, redesign, clone, or extension
- Approved content document, copy status, required page/section order, claims, legal text, and primary conversion
- Brand guide, logos, marks, colour specifications, font files and licences, icon systems, and previous collateral
- Supplied photography, video, illustration, diagrams, product screenshots, UI captures, testimonials, proof, and compliance material
- Competitor or inspiration references, including what the client likes and dislikes
- Existing repository, framework, component system, technical constraints, analytics/form destinations, and deployment expectations

If nothing exists, record that the project is greenfield and proceed without pretending assets were supplied. If the user indicates that a website, document, folder, or asset set exists but it is inaccessible, request the URL, attachment, path, or permission before making decisions that depend on it.

Classify the task:

- **New and visually undefined:** run guided intake and direction selection.
- **New with an explicit visual brief:** confirm the compiled brief and proceed to references.
- **Reference-led or clone:** analyse the reference and preserve the requested structure, content, and interaction model.
- **Redesign:** audit the current page before proposing a direction; preserve working functionality and locked copy.

Inspect the repository and its instruction files before changing code. Preserve the existing framework, package manager, component conventions, and runtime unless the user explicitly requests a migration.

### 2. Run guided intake when needed

When design decisions are delegated, choose unresolved visual preferences from the client context and record your reasoning instead of running an interview. Use the questions below only when the user wants collaborative direction selection or a material requirement cannot be inferred safely.

The source-material preflight happens before design questioning and does not count toward the design-question limit. Do not ask for material already found in the conversation, workspace, current website, or connected source.

Ask one decision at a time. Each question should contain two or three mutually exclusive choices, place the recommended choice first, explain its visual or commercial effect in one sentence, and allow a free-form alternative. Keep a visible sense of progress such as “Direction 1 of 4”.

Prioritise only unresolved decisions. A typical vague brief needs four decisions:

1. Visual direction
2. Colour mood
3. Typography character
4. Hero/layout structure

Ask about imagery, motion, or conversion architecture only when the brief does not make them inferable. When motion matters commercially or narratively, ask whether the experience should feel restrained, expressive, or scroll-led and explain the performance trade-off. Keep the interview to six questions or fewer unless the user requests a deeper workshop.

Do not start coding while a material direction choice remains unresolved.

### 3. Present three named directions

For an undefined brand direction, propose three genuinely different routes—not three colour variations of the same layout. Each direction must specify:

- A memorable name
- The strategic idea and audience impression
- Font pairing or typographic category
- Palette mood with representative colour roles
- Hero composition
- Hero density, headline scale range, first-viewport content budget, and what is deliberately deferred below the fold
- Imagery treatment
- Logo treatment in navigation and footer, including background handling and maximum visual footprint
- Surface, border, radius, and shadow character
- CTA treatment and how the primary conversion becomes visually dominant without decorative clutter
- Motion character
- The main trade-off

When design is delegated, compare the routes briefly, choose the strongest and generate its hero reference. Otherwise recommend one route and present the alternatives for the requested collaborative checkpoint. Avoid generating three complete directions when one selected route will resolve the task.

### 4. Compile and lock the design brief

Read [design-brief-schema.md](references/design-brief-schema.md). Write `DESIGN-BRIEF.md` inside the project using that structure.

Read [visual-calibration.md](references/visual-calibration.md) to establish a concrete visual target and the correction loop. This is especially important when the brief says only “premium”, “modern” or “make it better”.

Translate choices into implementation-ready rules: named fonts, weights, type scale, colour tokens, grid, maximum widths, spacing rhythm, radii, borders, shadows, imagery rules, section rhythm, interactions, motion tokens, motion reduction, and breakpoint transformations.

Also lock the practical composition constraints that commonly cause late-stage rejection:

- Maximum hero headline width and size at desktop and mobile
- First-viewport priority order and a density budget for text, media, proof, and actions
- Header height plus maximum logo height and width; use a genuinely transparent asset when the mark must sit without a background
- Primary CTA prominence through scale, contrast, placement, and supporting context
- Minimum clearance between indices, dividers, borders, icons, and text
- Section-specific composition rules so proof, success, process, and conversion sections do not become variations of the same card grid
- Explicit approved treatments, disliked treatments, and rejected motifs that must not reappear later in the page

Separate three kinds of information:

- **Locked:** approved copy, brand facts, supplied assets, selected direction.
- **Derived:** design tokens, responsive behaviour, composition rules.
- **Unresolved:** information still awaiting confirmation.

Run `node scripts/validate_design_brief.mjs <project>/DESIGN-BRIEF.md` when this skill’s bundled script is accessible. Correct missing or placeholder sections before continuing.

### 5. Create image-first section references

Load `imagegen-frontend-web`, then use the built-in image-generation capability.

Plan the page's narrative. Generate and critically review the hero reference first, correcting weak composition before extending it to the other sections. Generate one separate, large, horizontal reference image for every planned section. A page with seven sections receives seven section images. Generate fresh detail references instead of cropping small fragments from a full-page composite.

Keep these constant across every reference:

- Palette and colour roles
- Font pairing and typographic personality
- Grid logic and spacing rhythm
- Border, radius, icon, and surface language
- Image treatment and art direction

Vary section composition deliberately. Avoid repeating left-text/right-image, card grids, bento containers, and oversized centred headlines by default.

Save project-bound references under `design-references/` with ordered names such as `01-hero.png`, `02-proof.png`, and `03-product.png`. Treat approved references as the visual source of truth.

Review references at a realistic viewport crop, not only as isolated boards. Before implementation, confirm that:

- The hero has one dominant message, one dominant action, and no competing cluster of proof, imagery, labels, or decorative devices.
- The display type feels confident at normal viewing size rather than oversized for the canvas.
- The header logo is optically subordinate to navigation and does not introduce an accidental white rectangle or mismatched background.
- The final conversion section is a designed moment with enough contrast and visual weight, not merely centred copy and a button.
- Numbered rows, timeline steps, and ruled lists have breathing room on both sides of their lines.
- No decorative symbol is being used as a substitute for composition or meaning.

Direction selection and reference review are separate checkpoints. A named route does not establish that its execution is good. If the user rejects a reference, revise it; do not start coding from the rejected composition.

Still images cannot fully specify timing. Add concise motion annotations to the design brief for each section that moves: trigger, sequence, spatial change, duration, easing, repetition, mobile adaptation, and reduced-motion result. Do not invent animation merely because a reference contains depth or layered imagery.

If the user requested visual approval, show the references and wait at that checkpoint. Otherwise select the references after critical review and continue autonomously. In this workflow, references accepted by the agent can serve as the implementation source of truth, but must not be described as user-approved.

### 6. Translate references into code

Load `image-to-code` and analyse every approved reference for typography, spacing, colour, composition, imagery, components, responsive intent, and interaction cues.

Before composing sections, implement semantic tokens for:

- Background, foreground, muted text, accent, border, and surface colours
- Display and body font families
- Type scale and line-height relationships
- Spacing rhythm and content widths
- Radius, border, and shadow levels
- Motion duration and easing

Implement the header and hero as the first visual slice and inspect them at 1440 and 390 pixels before translating the remaining sections. Correct logo scale and background, hero density, headline wrapping, CTA weight, and fold composition at this point so a weak first screen does not propagate through the page.

Use intrinsic transparent image assets for logos when available. CSS blending, white containers, clipping, or filters are not substitutes for removing an unwanted baked-in background. Size logos by their visible mark, not merely by the source bitmap dimensions.

In ruled or numbered components, reserve explicit spacing between the number and the divider or content edge. Check the optical clearance in the rendered result; mathematically equal padding can still look cramped near thin rules.

Build semantic, accessible components using the existing stack. Prefer a small set of purposeful components over an abstract component factory. Every navigation item, CTA, form, modal, media control, and menu must have a real destination or behaviour.

For every full landing-page build or substantial redesign, read [motion-system.md](references/motion-system.md) before choosing a library or writing animation code. Use it to define three to five brand-motion words, select the lightest suitable technology, reserve one or two signature moments, and document section choreography. Load `brand-consistency` when available if the motion character is unclear or inconsistent.

Use motion to clarify hierarchy, explain a relationship, acknowledge an action, or create a deliberate narrative beat. Respect `prefers-reduced-motion`. Do not use animation to conceal weak composition, delay access to content, or make every section compete for attention.

## Default interactive motion contract

For new landing pages and substantial redesigns, motion is included by default: use GSAP for authored timeline choreography and ScrollTrigger where viewport or scroll progression drives it. Do not wait for the user to request animation separately. CSS remains appropriate for small hover/focus/pressed transitions. Preserve an explicitly required existing animation system rather than stacking competing libraries.

Plan and implement an intentional hero entrance, section-specific movement that explains or emphasises content, and responsive feedback for the controls actually present (links, CTAs, navigation, menus, tabs, accordions and forms). Choose one or two brand-specific signature moments where the content supports them. A hero fade and generic fade-ups everywhere do not meet an interactive brief. Do not invent controls, product behaviour or statistics to create animation opportunities.

Choose intensity from the brand: a restrained page can still feel responsive and alive. Exemptions are explicit static/minimal-motion requests, preservation/clone constraints, narrow edits, or a concrete runtime/performance/accessibility limitation. Record the exact constraint and implemented alternative; “motion was not requested” or “the screenshots look good” is not a valid exemption. Reduced-motion visitors receive an accessible alternative, not missing content.

Record each planned behaviour, trigger, target, sequence, duration/easing, mobile adaptation, reduced-motion result and acceptance evidence in the project brief. In a harness run, add a motion criterion with failure conditions and carry its observations into review. Missing planned motion or missing runtime observations blocks an unqualified completion claim.

### 7. Compose responsive behaviour intentionally

Do not treat mobile as a uniformly scaled desktop page. Define for each section:

- Reading order
- Column collapse behaviour
- Type resizing and line wrapping
- Image crop or aspect-ratio change
- Navigation and CTA treatment
- Card/grid transformation
- Spacing compression
- Elements that may hide and why

Check 1440, 1024, 768, 390, and 320 pixels when supported. There must be no horizontal overflow, clipped content, accidental overlap, unreadable text, or unreachable controls.

At each width, inspect the first viewport as a composition: logo, headline, supporting copy, CTA, and primary image should have a clear reading order. Mobile may reorder the image below the action and supporting copy when that produces a calmer, more useful first screen.

### 8. Verify the real result

Read [visual-quality-rubric.md](references/visual-quality-rubric.md). Use `playwright-visual-testing` or the available browser inspection capability.

When the user supplies annotations, element references, or subjective rejection feedback, read [feedback-calibration.md](references/feedback-calibration.md). Resolve both the exact annotated element and any shared token or component that caused the issue, then verify the correction in context.

Run the real build, type checks, linting, and tests supplied by the project. Open the rendered page and check:

- Visual agreement with approved section references
- Typography loading and fallback behaviour
- Image resolution, crop, and alt text
- Navigation, buttons, forms, menus, media, and focus states
- Motion timing, trigger positions, replay behaviour, scroll restoration, and brand consistency; watch the planned sequences in motion at desktop/mobile and verify reduced motion. Record trigger/action, observed change, final state and evidence in `QA/motion-review.md`; still screenshots or installed GSAP alone cannot prove motion works.
- Responsive behaviour at the target widths
- Contrast, keyboard access, reduced-motion behaviour, non-JavaScript content access, and semantic structure
- Console errors, broken assets, and network failures
- Metadata, title, description, favicon, and social preview when in scope
- Accidental private data or unapproved claims

Score the result with the rubric and the visual-calibration evidence. Record technical verification separately from visual acceptance. Do not hand over a page as client-ready with a zero in any category, below the premium threshold, or with unresolved visible weaknesses merely hidden by a generous total score. Follow the bounded correction loop rather than endlessly regenerating or silently lowering the standard.

### 9. Correct anti-AI patterns

Remove or redesign:

- Generic purple/blue SaaS gradients without a brand reason
- Repeated card grids and identical section compositions
- Cards nested inside cards
- Giant rounded containers around every section
- Decorative pills, labels, status markers, or fake product UI
- Unsupported metrics, testimonials, charts, clients, or dashboards
- Oversized headings with weak supporting hierarchy
- Crowded heroes where headline, proof, service labels, imagery, and multiple actions compete in the first viewport
- Excessive empty space that does not create tension or focus
- Logos that dominate the header, carry an unintended baked-in background, or sit inside an unnecessary white patch
- Weak conversion sections that look like ordinary content blocks instead of the page's decisive action moment
- Numbers, labels, or icons sitting uncomfortably close to divider lines or borders
- Decorative ticks, arrows, badges, or symbols added without a content or interaction role
- Random stock imagery, inconsistent icons, stretched images, and weak crops
- Copied source-brand names, domains, addresses, or assets left in a redesign
- Controls that look interactive but do nothing
- Generic fade-up animation repeated on every element without hierarchy
- Excessive parallax, pinning, cursor effects, floating loops, or scroll hijacking
- Multiple animation libraries controlling the same elements or properties

### 10. Complete and report

Report the outcome, not merely the plan:

1. Design direction selected and meaningful trade-offs
2. Reference images generated and used
3. Files created or changed
4. Builds, tests, widths, and interactions verified, including implemented motion and the saved runtime motion review
5. Remaining placeholders, factual gaps, or approval needs
6. Full paths to design references and changed files
7. Preview or deployment links last

Do not publish, deploy, send, or change live work without approval.

## Handoff and revision behaviour

When the user requests changes after approval, preserve the chosen visual language unless they explicitly reopen the direction. Translate vague feedback—“more premium”, “less AI”, “too empty”—into concrete adjustments to hierarchy, density, imagery, typography, or rhythm, and explain the meaningful trade-off briefly.

Read [feedback-calibration.md](references/feedback-calibration.md) for every visual revision round. Keep a short rejection ledger in `DESIGN-BRIEF.md` so a removed motif, rejected layout, excessive scale, or disliked density is not accidentally reintroduced elsewhere.

Choose the revision level from the evidence:

- Correct a local defect when the concept is accepted and the issue is spacing, scale, crop, or asset treatment.
- Redesign the affected section when the user dislikes its composition or prominence.
- Return to visual references and rebuild the direction when the user rejects the design overall. Do not keep cosmetically patching a composition they have already rejected, and do not preserve its geometry simply because code exists.

If a revision would conflict with locked copy, brand rules, accessibility, or a previously approved direction, surface the conflict before changing it.

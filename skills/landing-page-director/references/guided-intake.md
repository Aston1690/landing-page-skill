# Guided intake

Use this question bank selectively. Ask only unresolved questions and ask them one at a time. The goal is to reduce consequential ambiguity without making the user complete a long questionnaire.

## Source-material preflight

Run this before visual-direction questions when the user has not supplied a complete brief. First inspect the conversation and workspace so the user is not asked to upload something that is already available.

Use one concise, upload-friendly source request:

> Before we choose the design direction, please share anything that already exists for this client:
>
> 1. Current website or source-page URL
> 2. Approved content/copy document and required section order
> 3. Brand guide, logos, colour specifications, font files or font names
> 4. Photography, video, illustrations, icons, diagrams, product screenshots or UI captures
> 5. Testimonials, proof, compliance/legal material and required disclaimers
> 6. Reference or competitor websites, including anything the client likes or dislikes
> 7. Existing repository, platform and any form, analytics or deployment requirements
>
> You can attach files, paste links, provide workspace paths, or say “nothing exists yet—start from scratch”.

This is a source-collection request rather than a design decision, so it may list the missing material together. After the user responds:

- Confirm what was received and what is still missing.
- Open and inspect every accessible URL, document, image, asset folder and repository source before asking visual questions.
- Ask a single follow-up only when a missing item materially changes the design or factual accuracy.
- If a current client website exists, request its URL before a redesign, clone, migration or style-extension audit.
- Establish whether copy is approved, draft, requires writing, or does not yet exist. Do not treat draft copy as locked.
- Establish whether supplied logos, fonts and imagery are approved for use and whether any licensing or usage restrictions are known.
- Never block a genuinely greenfield project merely because no assets exist; record the absence and keep unsupported facts as `[TO BE CONFIRMED]`.

Do not begin visual-direction choices until the source inventory is either collected or explicitly confirmed as unavailable.

## Design-decision interaction format

Use this pattern:

**[Decision name] — [step] of [total]**

[One-sentence question]

1. **[Recommended option] (Recommended)** — [Effect and trade-off in one sentence.]
2. **[Alternative]** — [Effect and trade-off in one sentence.]
3. **[Alternative]** — [Effect and trade-off in one sentence.]

The user may also answer in their own words.

Never show more than three preset choices. Avoid vague labels such as “Modern”, “Clean”, or “Creative” without describing what they mean visually.

## Decision order

### 1. Visual direction

Create choices from the brand and audience rather than reusing a universal list. Useful directional families include:

- Editorial authority: strong typography, restrained palette, asymmetric composition
- Product clarity: structured demonstrations, compact proof, minimal ornament
- Human confidence: photography-led, warm surfaces, approachable typography
- Technical precision: dense grid, diagnostic imagery, controlled contrast
- Cultural energy: expressive colour, illustration, varied rhythm
- Quiet luxury: refined type, generous spacing, tactile detail, low-noise surfaces

Name each route specifically for the project, such as “Frosted clinical confidence” rather than “Option A”.

### 2. Colour mood

Describe roles rather than presenting disconnected swatches:

- Foundation/background
- Primary text
- Accent/action
- Supporting surface
- Border or separator
- Status colours if needed

Options should express a mood and risk. Example: “Cloud white + diagnostic blue—high trust and clinical clarity, but it requires distinctive imagery to avoid generic health-tech styling.”

### 3. Typography character

Offer real font pairs when licensing and loading are feasible. Explain what each pairing communicates and how it affects density. Consider:

- Geometric display + neutral grotesk body
- Editorial serif display + humanist sans body
- Single variable grotesk with controlled weight contrast
- Condensed display + practical sans body

Avoid selecting fonts only because they are currently fashionable. Check language coverage, numeral quality, weights, and performance.

### 4. Hero and layout structure

Connect layout to content:

- Hero grid: message and contextual product/imagery share the first screen
- Editorial stack: type leads, imagery interrupts below
- Split screen: two equally important ideas or audiences
- Full-bleed narrative: immersive image/video carries the emotional case
- Product stage: central interface or object with supporting proof around it
- Asymmetric proof-led: credibility leads before explanation

Do not default to hero grid merely because it is reliable.

### 5. Imagery treatment

Ask only when supplied assets and context do not determine the answer:

- Documentary photography
- Product UI or device imagery
- Generated conceptual imagery
- Technical diagrams or data visualisation
- Illustration or collage
- Typographic/no-image direction

Clarify whether the imagery must depict real people, real product data, or regulated subject matter.

### 6. Conversion architecture

Confirm the primary action and user readiness:

- Direct transaction or registration
- Demo/contact lead capture
- Education before conversion
- Download or lead magnet
- Multi-audience routing

Do not invent a funnel when the intended action is unknown.

### 7. Motion character

Ask only when motion is important to the brief and cannot be derived from the brand or reference. Describe the experience rather than leading with a library name:

- Restrained and precise: short transitions, controlled reveals, minimal displacement
- Expressive and editorial: larger masks, typographic choreography, one or two composed sequences
- Scroll-led and cinematic: progress-linked scenes, pinning, parallax, or staged spatial storytelling
- Mostly static: state feedback and accessibility cues only

Recommend the least dramatic option that still supports the page idea. Explain that cinematic motion costs more performance, engineering effort, responsive adaptation, and testing. Ask about GSAP, Motion, or another library only when the repository or user has already established a technical preference.

## When not to interview

Skip questions already answered by:

- An approved brand kit or design system
- A specific visual reference the user wants followed
- Locked wireframes or Figma files
- An existing page whose visual language must be extended
- Explicit fonts, colours, layout, imagery, and conversion requirements

In those cases, summarise the derived design brief and ask only for materially missing approval.

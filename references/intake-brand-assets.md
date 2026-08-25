# Intake, Brand, Content, and Asset Provenance

Use this reference before research or implementation.

## 1. Sequential intake gate

Ask one short question at a time and wait for its answer. Never present a multi-field paragraph. Skip anything already supplied or safely inferable.

Order:

1. Company/product/campaign/person and canonical official website URL, if one exists.
2. Location of final user-approved copy: Google Doc, PDF, Word, Notion, repository, existing URL, pasted copy, or another source.
3. Brand guide, official logo, fonts, photography, illustrations, screenshots and references, if they exist.
4. Build boundary: separate greenfield build, existing-project edit, or template-preserving adaptation.
5. Ask audience, conversion action, CTA/form destination, analytics, consent, legal or accessibility questions only when the supplied site/copy does not answer them and they materially block implementation.

Do not ask whether to rewrite copy. Exact preservation is the default. Do not ask local versus deployed; Vercel deployment is the default.

When the user says “from scratch” or “do not touch previous builds,” create a uniquely named folder/branch and never edit prior work.

## 2. Source hierarchy

Use this order for creative/operational authority when sources disagree. Approval is not factual verification.

1. Explicit user instruction and approved content/brand guide.
2. Current official client-controlled website and supplied assets.
3. Approved campaign/template/reference files.
4. Licensed external sources.
5. Agent-created direction, clearly labelled as such.

Never treat an unrelated nearby file, old deployment, search result, or generated comp as approved source material. Track `approval_status` and `verification_status` separately for metrics, testimonials, credentials, regulated claims, awards, and customer logos.

## 3. Official website audit

Open the canonical site in a real browser. Inspect:

- logo variants, header/footer treatment, favicon and social image;
- computed fonts, weights, tracking, line heights, and font files;
- CSS variables and computed colours on headings, buttons, surfaces, links, and borders;
- spacing, container widths, grid, radii, shadows, button grammar, icon family;
- photography/illustration grade, subjects, crops, overlays, and texture;
- navigation, CTA, forms, footer, responsive behaviour, and motion;
- content voice, claims, regulated wording, and trust devices.

Record findings in a working brief or `SOURCE-NOTES.md`.

## 4. Logo recovery

Search before asking the user:

1. Header/footer `<img>`, `<picture>`, `srcset`, inline SVG.
2. CSS `background-image`, masks, pseudo-elements, and sprite assets.
3. Structured data, Open Graph/Twitter metadata, favicons, web manifests.
4. Media, press, brand, download, and investor pages.
5. User-supplied project folders and official repositories.

Prefer official SVG, then highest-resolution transparent PNG. Open it and compare against the live identity before marking verified. Record source URL and local path.

Never redraw, approximate, trace, or image-generate an existing client logo. If an existing logo cannot be recovered, state what was checked and ask for an official SVG or transparent PNG. If no logo has ever existed, confirm whether a plain-text product-name treatment is acceptable and record that logo design is outside scope.

## 5. Brand-guide fallback

If a brand guide exists, follow it and reconcile discrepancies with the current site. If none exists, create a compact project guide:

- verified logo variants and clear space;
- primary, secondary, accent, neutral palette;
- display/body/utility typography with licensing and availability;
- grid, container, spacing scale, radii, borders, shadows;
- button, link, input, form, navigation, and icon grammar;
- photography/illustration direction and image grade;
- tone of voice, copy-preservation policy, and avoid-list;
- motion character and reduced-motion approach.

If there is no usable existing identity, create one coherent agent-authored direction from the offer, audience, category, and context. Label it as agent-created, not client-approved.

## 6. Content policy and extraction

Default to `exact_preservation`: retain user-supplied wording verbatim. Select `authorized_editing` or `agent_draft_unapproved` only when the user explicitly asks to edit, restructure or write copy. Label agent drafts unapproved and request acceptance before treating them as final.

Extract text and imagery in the same pass. Preserve:

- headings, body, CTAs, quotes, names, roles, contact details;
- statistics, qualifications, awards, licences, disclaimers, eligibility and consent wording;
- document section structure and image-to-copy relationships;
- phrases marked exact or approved.

Do not invent metrics, testimonials, credentials, claims, clients, integrations, or legal language. User approval does not independently verify factual claims. For finance, healthcare, legal, government, education, and other trust-sensitive work, retain supplied compliance wording exactly unless the user authorises edits and flag unsupported factual assertions.

## 7. Asset manifest

For every visible asset record:

- filename/local path and source URL/path;
- type and dimensions;
- what it shows;
- intended section and crop;
- provenance: user-supplied, official-source extracted, licensed, generated with permission, or unresolved;
- permission/licensing status where relevant;
- desktop/mobile variant;
- final optimised path and alt text.

Verify URLs and local files before use. Never guess filenames. Do not ship unresolved placeholders without clearly reporting them.

## 8. Integrations

Do not fake forms or success states. Configure the supplied endpoint/provider or mark it unresolved. Test with sandbox/test endpoints and clearly synthetic data. Never submit real leads, CRM records, payments, emails, or analytics events without explicit user approval. Otherwise verify configuration and client-side validation without sending and report the limitation. Preserve field names and consent copy in existing projects unless authorised to change them.

## 9. Direction approval

Use `user_checkpoint` when the user requests approval, options have meaningful trade-offs, identity/copy changes are consequential, or an irreversible decision is required. Use `agent_acceptance_gate` for autonomous end-to-end tasks when decisions are reversible and source-backed. Record the mode and evidence; do not block indefinitely waiting for approval that was not requested.
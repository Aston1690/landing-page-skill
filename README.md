# Landing Page Skill v3.3.0

A premium Codex skill for intake, evidence-led brand research, image art direction, production asset generation, implementation, purposeful motion, browser QA, scoring, and verified deployment.

## Install directly in Codex chat

Paste this into Codex:

```text
Install this skill: https://github.com/Aston1690/landing-page-skill
```

For a reproducible version-pinned installation, paste:

```text
Install this skill: https://github.com/Aston1690/landing-page-skill/tree/v3.3.0
```

## Install from the terminal

```bash
bash <(curl -sL https://raw.githubusercontent.com/Aston1690/landing-page-skill/main/install.sh)
```

Restart or reload Codex, then invoke `landing-page` naturally.

## Manual Codex installation

```bash
git clone https://github.com/Aston1690/landing-page-skill.git ~/.codex/skills/landing-page
```

Restart Codex, then describe the landing-page task.

## Version traceability

This release is `v3.3.0`. The skill requires every project brief and completion report to state the exact `landing-page` version used, making future variants and updates auditable.

## Workflow

1. One short intake question at a time; exact user-supplied copy by default.
2. Official-site brand, logo, content, compliance, and asset audit.
3. Source-backed conversion/content architecture.
4. Frontend Design + Design Taste plus policy-routed Imagegen references and production imagery.
5. Complete static implementation and screenshot approval.
6. Default GSAP choreography and control micro-interactions, with documented static/preservation/runtime exceptions.
7. Desktop/tablet/mobile browser and interaction QA.
8. Binary critical checks plus an evidence-backed 0/5/8/10 quality gate; N/A requires rationale.
9. SEO, performance, source notes, and default Vercel deployment with live verification.

## Tool routing

- `frontend-design`: brand-specific visual thesis and art direction.
- `design-taste-frontend`: anti-slop implementation and responsive preflight.
- `imagegen-frontend-web`: conditional on visual ambiguity, image-led direction, requested concepts, or insufficient approved assets.
- production image generator or `media-use`: individual website imagery after art direction is locked.
- `imagegen-frontend-mobile`: app-native screen media only for mobile-app marketing pages, never responsive web design.
- GSAP/ScrollTrigger: default for full builds, adapted to brand and content; static, narrow-edit and required existing-system constraints are preserved.

## Repository files

```text
SKILL.md
README.md
install.sh
scripts/
  check_contract.py
  eval_cases.py
evals/
  evals.json
references/
  intake-brand-assets.md
  policy-matrix.md
  frontend-skill-stack.md
  imagegen-production.md
  gsap-motion.md
  premium-quality-gate.md
  section-patterns.md
  verification-checklist.md
```

## Validate

```bash
python3 scripts/check_contract.py
```

The semantic contract check enforces the main-file size, nine phases, six authoritative modes, conditional tool routing, integration safety, risk-based viewport policy, routed references and executable scenario coverage.

## Requirements

- Codex with Skills support
- Browser-capable screenshot and interaction QA
- Image-generation capability when the selected mode requires generated references/assets
- Node.js/GSAP when motion mode is selected
- Vercel CLI or another deployment tool only when deployment is requested

## License

MIT

## Landing-page director

The companion `skills/landing-page-director/` folder contains the director workflow and the same default motion requirements. Install that folder as `landing-page-director` if using the director workflow. Its optional local harness integration requires a separately installed harness; no personal harness paths are bundled.

# GSAP Production Motion

Use this reference only after the static page passes visual QA.

## 1. Mode selection

Resolve motion from `policy-matrix.md`, then apply a decision gate covering narrative value, brand fit, runtime constraints, accessibility, existing-motion compatibility, and user request. “No GSAP” is a first-class premium result with written rationale. Use restrained CSS-only or static behaviour when:

- the user explicitly requests static/minimal motion;
- the brand calls for near-still editorial restraint;
- accessibility, performance, embed, email, print, or platform constraints rule GSAP out;
- the existing project has an approved motion system that must be preserved.

Motion is conditional by project mode, not ceremonial.

## 2. Motion storyboard

Before implementation list each sequence and its purpose:

- hero orchestration: establish hierarchy and focus;
- media reveal: introduce important imagery;
- section sequence: explain process/proof in order;
- brand motif: strengthen recall with one signature movement;
- interaction feedback: confirm hover, press, menu, accordion, tab, or form state;
- final CTA: close the narrative without delaying action.

If the purpose is only “looks cool,” remove it.

## 3. Scope

Implement only the sequences justified by the storyboard. Do not require a hero timeline, trigger count, parallax motif, or animation quota when the content does not need them. Every animated page still requires complete reduced-motion behaviour, cleanup, responsive refresh, and interaction safety. Do not animate every paragraph or repeat the same fade-up across the page.

## 4. Implementation requirements

- install/bundle a pinned GSAP version; load only plugins used;
- register ScrollTrigger;
- use `gsap.context()` in component projects and revert on cleanup;
- use `gsap.matchMedia()` for responsive and reduced-motion branches;
- animate transform/opacity and deliberate clip/mask properties where practical;
- never use raw `window` scroll listeners or React state for continuous scroll values;
- use measured triggers such as `start: "top 80%"`, then inspect and tune;
- refresh after fonts, images, accordions, and dynamic layout settle;
- reserve media geometry to avoid CLS;
- keep interaction input and focus behaviour intact.

## 5. Visibility safety

Critical content must remain visible if scripts fail, are blocked, or load slowly.

Avoid permanent CSS `opacity: 0` on content. Prefer a JS-activated motion class, GSAP `from` setup after successful load, `<noscript>` fallback, or an explicit timeout/visibility reset. Reduced-motion mode must render the final static state immediately.

Background tabs throttle timers. Verify hero animation in an active foreground tab before diagnosing a blank screenshot.

## 6. Motion language

Choose one coherent motion character:

- restrained precision;
- editorial reveal;
- cinematic fade-through;
- tactile product motion;
- playful spring;
- technical sequencing.

Keep easing, duration, stagger, distance, and direction consistent. Vary choreography by content, not randomly.

## 7. QA

Inspect:

1. In-motion hero frame and final resting state at user viewport.
2. Top, middle, and final CTA triggers.
3. User viewport, every breakpoint boundary, one tablet, one narrow mobile, and one common mobile geometry.
4. Menu/accordion/tab/form state changes.
5. `prefers-reduced-motion: reduce`.
6. Script/plugin failure behaviour.
7. Console/network errors.
8. Stuck opacity, flashes, jump cuts, overlap, trigger drift, premature firing, and excessive pin duration.
9. Performance: no layout-property animation, runaway timelines, duplicate triggers, or missing cleanup.

Motion fails the gate if it makes reading harder, delays the CTA, causes content instability, or appears generic/repetitive.
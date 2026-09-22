# GSAP Production Motion

Read when planning every full build; implement motion after the static page passes visual QA.

## Default interactive motion contract

For new landing pages and substantial redesigns, motion is included by default: use GSAP for authored timeline choreography and ScrollTrigger where viewport or scroll progression drives it. Do not wait for the user to request animation separately. CSS remains appropriate for small hover/focus/pressed transitions. Preserve an explicitly required existing animation system rather than stacking competing libraries.

Plan and implement an intentional hero entrance, section-specific movement that explains or emphasises content, and responsive feedback for the controls actually present (links, CTAs, navigation, menus, tabs, accordions and forms). Choose one or two brand-specific signature moments where the content supports them. A hero fade and generic fade-ups everywhere do not meet an interactive brief. Do not invent controls, product behaviour or statistics to create animation opportunities.

Choose intensity from the brand: a restrained page can still feel responsive and alive. Exemptions are explicit static/minimal-motion requests, preservation/clone constraints, narrow edits, or a concrete runtime/performance/accessibility limitation. Record the exact constraint and implemented alternative; “motion was not requested” or “the screenshots look good” is not a valid exemption. Reduced-motion visitors receive an accessible alternative, not missing content.

Record each planned behaviour, trigger, target, sequence, duration/easing, mobile adaptation, reduced-motion result and acceptance evidence in the project brief. In a harness run, add a motion criterion with failure conditions and carry its observations into review. Missing planned motion or missing runtime observations blocks an unqualified completion claim.

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

Implement only the sequences justified by the storyboard. Meet the default motion contract without arbitrary trigger counts or decorative parallax quotas. Every animated page still requires complete reduced-motion behaviour, cleanup, responsive refresh, and interaction safety. Do not animate every paragraph or repeat the same fade-up across the page.

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
Save runtime observations in `QA/motion-review.md`: planned behaviour, element, trigger/action, viewport, observed motion, final state, reduced-motion result, evidence and pass/fail. Watch desktop/mobile in motion; capture a recording where available or time-separated states with observations. Missing planned motion or runtime evidence fails acceptance. Still screenshots and GSAP imports are insufficient.

API references: https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/ and https://gsap.com/docs/v3/Plugins/ScrollTrigger/.

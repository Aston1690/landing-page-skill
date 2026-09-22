# Landing-page motion system

Read this reference for every full landing-page build and substantial redesign, and for scoped motion changes. Motion should feel authored by the same brand as the typography, imagery, composition, and copy.

## Default interactive motion contract

For new landing pages and substantial redesigns, motion is included by default: use GSAP for authored timeline choreography and ScrollTrigger where viewport or scroll progression drives it. Do not wait for the user to request animation separately. CSS remains appropriate for small hover/focus/pressed transitions. Preserve an explicitly required existing animation system rather than stacking competing libraries.

Plan and implement an intentional hero entrance, section-specific movement that explains or emphasises content, and responsive feedback for the controls actually present (links, CTAs, navigation, menus, tabs, accordions and forms). Choose one or two brand-specific signature moments where the content supports them. A hero fade and generic fade-ups everywhere do not meet an interactive brief. Do not invent controls, product behaviour or statistics to create animation opportunities.

Choose intensity from the brand: a restrained page can still feel responsive and alive. Exemptions are explicit static/minimal-motion requests, preservation/clone constraints, narrow edits, or a concrete runtime/performance/accessibility limitation. Record the exact constraint and implemented alternative; “motion was not requested” or “the screenshots look good” is not a valid exemption. Reduced-motion visitors receive an accessible alternative, not missing content.

Record each planned behaviour, trigger, target, sequence, duration/easing, mobile adaptation, reduced-motion result and acceptance evidence in the project brief. In a harness run, add a motion criterion with failure conditions and carry its observations into review. Missing planned motion or missing runtime observations blocks an unqualified completion claim.

## 1. Define motion before choosing a library

Write three to five motion words derived from the selected direction, such as `precise`, `calm`, `assured`, `layered`, and `responsive`. Then define the opposite behaviours to avoid, such as `bouncy`, `restless`, `elastic`, or `theatrical`.

For every proposed animation, identify its job:

- **Hierarchy:** directs attention in the intended reading order
- **Explanation:** reveals a relationship, process, state, or transformation
- **Feedback:** acknowledges hover, focus, selection, submission, success, or error
- **Continuity:** helps users understand where an element came from or went
- **Narrative emphasis:** creates a deliberate signature moment tied to the page idea

Remove motion that has no clear job. A premium page usually needs one consistent transition language and no more than one or two signature sequences.

## 2. Choose the lightest suitable technology

Preserve the project stack and inspect installed dependencies before adding anything.

| Need | Preferred tool | Use when | Avoid when |
|---|---|---|---|
| Hover, focus, pressed states, simple fades or transforms | CSS transitions/keyframes | The sequence is local, deterministic, and has few states | Several elements require orchestration or interruption |
| Small imperative animation without a framework dependency | Web Animations API | Native browser control is enough and cleanup is simple | React presence/layout state already has a suitable library |
| React enter/exit, stagger, layout, gestures, or in-view reveals | Existing React motion library or Motion | Animation follows component state and benefits from declarative composition | A complex scroll timeline or hundreds of targets dominate the page |
| Sequenced timelines, SVG choreography, advanced masks, pinning, or scrubbed scroll stories | GSAP with ScrollTrigger where licensed and appropriate | The experience genuinely requires timeline control and responsive scroll orchestration | The effect is only a fade-up, hover, or single transform |
| Native progress-linked effects | CSS scroll-driven animations with fallback | Progressive enhancement is acceptable and browser support matches the audience | The effect is essential and must behave identically everywhere |
| Supplied vector/state-machine animation | Rive or Lottie | The brand asset is authored for that runtime and accessibility is planned | It is being introduced as generic decoration |
| Spatial product experience | Canvas/WebGL/Three.js | The central concept depends on real-time 3D or shader rendering | A raster image, video, or CSS transform can communicate the idea |

GSAP is the default choreography tool for full builds in this workflow. Choose useful sequences rather than adding an unused import or ceremonial tween. Premium motion comes from restraint, timing, hierarchy, and brand fit. Avoid allowing CSS, Motion, and GSAP to control the same property on the same element.

## 3. Establish reusable motion tokens

Adapt tokens to the brand instead of copying these blindly:

```css
:root {
  --motion-duration-instant: 120ms;
  --motion-duration-fast: 180ms;
  --motion-duration-base: 280ms;
  --motion-duration-slow: 520ms;
  --motion-duration-scene: 900ms;
  --motion-ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --motion-ease-enter: cubic-bezier(0.22, 1, 0.36, 1);
  --motion-ease-exit: cubic-bezier(0.4, 0, 1, 1);
  --motion-distance-small: 8px;
  --motion-distance-medium: 20px;
  --motion-distance-large: 36px;
  --motion-stagger-tight: 60ms;
  --motion-stagger-base: 100ms;
}
```

Use roughly these timing tiers:

- 120–200 ms for hover, focus, press, and compact state feedback
- 200–400 ms for component changes and menus
- 450–900 ms for section entrances and image masks
- 900–1600 ms only for a signature scene whose duration adds meaning

Keep a reveal group’s total stagger around 450 ms or less. Users should not wait for text or controls. Default spatial movement should be modest: 8–32 px translation and approximately `0.98` to `1` scale. Larger movement needs a narrative reason.

## 4. Write a choreography map

Add a compact motion entry to the design brief for each moving section:

| Field | Record |
|---|---|
| Purpose | What the motion helps the user understand or notice |
| Trigger | Load, viewport entry, hover, focus, click, form state, or scroll progress |
| Sequence | Primary, secondary, and detail actions in order |
| Properties | Opacity, transform, mask, path, colour, or another justified property |
| Timing | Duration, easing, delay, stagger, and whether it can be interrupted |
| Repetition | Once, on state change, or deliberately repeatable |
| Responsive adaptation | What changes or disappears below each breakpoint |
| Reduced motion | The immediate or low-motion equivalent |

Useful defaults:

- Reveal narrative content once as it enters the viewport.
- Repeat only interactions that communicate a repeatable state change.
- Trigger section entrances when the important content is approximately 75–85% down the viewport.
- Preserve reading order: message first, evidence second, decorative detail last.
- Keep essential links and controls available before animation completes.

## 5. Use section-specific patterns

Vary composition without inventing a different motion language for every section.

### Hero

Stage the core proposition first, then the primary visual, then supporting proof. A mask, scan line, depth shift, or typographic transition can become the signature moment when it expresses the product idea. Avoid making the CTA wait behind a long intro.

### Process or workflow

Use a connector, path, highlight, or state transition to explain sequence. Reveal steps in logical order. Do not animate every icon independently when a single progress gesture communicates the relationship better.

### Product review or comparison

Use markers, split views, or before/after states to explain inspection. Keep labels readable and stationary enough to compare. Avoid continuous image drift.

### Integrations, features, or proof

Use restrained stagger to clarify grouping. Preserve intentional static offsets from the design; animate a wrapper or independent `translate` property rather than overwriting layout transforms.

### Trust, governance, or technical depth

Prefer measured reveals, layer assembly, controlled light, or traceable pathways. Serious claims should not be paired with playful springs or decorative orbit loops.

### Conversion section

Use focus, validation, loading, success, and error feedback. Keep the form stable; avoid entrances that shift fields while the user is typing.

## 6. Use GSAP responsibly

Use GSAP timelines for the planned default choreography; use ScrollTrigger only for behaviours that need viewport/scroll triggers.

- Confirm GSAP and required plugins are permitted and installed before importing them.
- Register plugins once in a client-safe location.
- Scope selectors to the component or section.
- Create animations after elements exist and revert or kill them during cleanup.
- Use `gsap.matchMedia()` or equivalent responsive branches for desktop, mobile, and reduced motion.
- Refresh scroll measurements after fonts, images, and layout-affecting assets settle.
- Avoid pinning multiple long sections; pinning can make mobile navigation feel trapped.
- Prefer transform and opacity. Use masks, filters, blur, and large shadows selectively because they can increase painting cost.
- Never hijack scrolling, change wheel sensitivity, or block native keyboard and touch navigation.
- Keep content visible if JavaScript fails.

For React, do not let re-renders recreate timelines. Use the integration recommended by the installed GSAP version, scope work to a stable ref, and ensure development strict-mode cleanup leaves no duplicate triggers.

## 7. Accessibility and reduced motion

`prefers-reduced-motion` is a different choreography, not a hidden page.

- Remove parallax, scrubbing, pinned storytelling, auto-rotation, and large spatial movement.
- Replace essential explanatory sequences with an immediate final state or a very short opacity transition.
- Keep focus, validation, loading, success, and error states perceivable without relying on movement alone.
- Provide pause controls for non-essential autoplaying motion where required.
- Avoid flashes, rapid zooms, vestibular camera movement, and unexpected continuous loops.
- Ensure transformed elements retain logical focus order and usable hit areas.

## 8. Responsive and performance adaptation

Treat desktop, tablet, and mobile as separate choreography contexts.

- Reduce travel distance and stagger on smaller screens.
- Disable or redesign pinning when it consumes too much of a mobile viewport.
- Do not animate layout in ways that cause cumulative layout shift.
- Lazy-load non-critical media and avoid decoding large assets at the first animation frame.
- Apply `will-change` narrowly and temporarily; permanent promotion wastes memory.
- Pause off-screen continuous media or animation.
- Test on a realistic mobile viewport and, when possible, a lower-power device profile.

Prefer progressive enhancement: the page must remain readable, operable, and correctly laid out before the animation layer runs.

## 9. Component-canvas controls

When the project provides a component canvas or story system, expose only motion controls that help design review:

- Motion enabled
- Intensity or variant when the component genuinely supports more than one
- Duration and stagger for authored sequences
- Initial, active, success, and error states
- Reduced-motion preview

Keep defaults aligned with the locked brief. Avoid exposing arbitrary physics controls that let stories drift away from the brand system.

## 10. Browser QA

Inspect the real rendered page, not only code or isolated stories.

- Verify 1440, 1024, 768, 390, and 320 pixel widths when supported.
- Test first load, hard refresh, anchor navigation, back/forward restoration, and direct links to lower sections.
- Scroll slowly and quickly; ensure triggers do not fire late, reverse unexpectedly, or leave content hidden.
- Test keyboard navigation while animations are active.
- Enable reduced motion and confirm every section remains understandable.
- Check sticky headers, menus, forms, and focus rings during pinned or transformed states.
- Confirm there is no horizontal overflow, layout shift, clipped content, duplicate trigger, or console error.
- Compare the motion result with the approved direction: timing and restraint matter as much as the final frame.

Do not claim motion is complete until the full page has been watched at desktop and mobile widths and the reduced-motion result has been checked.

## 11. Evidence required for completion

Save `QA/motion-review.md` with one row per planned behaviour: element/section, action or trigger, viewport, observed movement/state change, resting state, reduced-motion alternative, evidence path and pass/fail. Watch the full page at desktop and mobile; test touch and keyboard feedback as well as hover. Include a short recording when available or multiple time-separated captures plus precise browser observations. A static full-page screenshot, dependency presence or source-code inspection alone cannot establish timing or interactivity.

A missing sequence, an effect that never fires, all-purpose fade-ups substituting for the storyboard, or untested reduced-motion behaviour fails motion acceptance. Preserve the accepted composition while fixing motion. Do not require user hero approval to verify it.

Implementation sources: [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/), [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/). Check installed-version documentation when choosing integration APIs.

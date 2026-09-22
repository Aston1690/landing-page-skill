# Authoritative Project-Mode Policy Matrix

This reference is the single authority for tool routing. Other prose may explain roles but must not override these decisions.

```json
{
  "version": "3.3.0",
  "shared": {
    "intake_style": "Ask one short question at a time. Never combine multiple fields into a paragraph.",
    "approval_modes": {
      "user_checkpoint": "Use when requested, when directions have meaningful trade-offs, when identity/copy changes are consequential, or when a decision is irreversible.",
      "agent_acceptance_gate": "Use for autonomous end-to-end work when decisions are reversible and source-backed. Record evidence and continue without blocking."
    },
    "content_default": "exact_preservation of user-supplied copy",
    "content_exceptions": "authorized_editing or agent_draft_unapproved only when explicitly requested by the user",
    "deployment_default": "Deploy every completed landing page to Vercel and live-verify desktop/mobile. Ask only for authentication, ownership, secrets, or another real blocker.",
    "integration_safety": "Use sandbox/test endpoints and synthetic data. Never submit real leads, payments, CRM records, email, or analytics events without explicit approval.",
    "viewport_policy": "Test the user's actual viewport, every layout breakpoint boundary, one tablet, one narrow mobile, and one common mobile. 375/390 are defaults, not universal requirements.",
    "quality_gate": "Binary critical checks plus evidence-backed 0/5/8/10 rubric. N/A is permitted only with a written rationale."
  },
  "modes": {
    "greenfield": {
      "imagegen_web": "conditional",
      "imagegen_conditions": [
        "visual_ambiguity",
        "image_led_direction",
        "concepts_requested",
        "insufficient_official_assets"
      ],
      "imagegen_skip": [
        "intentional_typography_led_direction",
        "asset_rich_approved_system",
        "user_requests_supplied_assets_only"
      ],
      "gsap": "default_on_with_documented_exceptions",
      "gsap_conditions": [
        "brand_adapted_choreography",
        "runtime_support",
        "accessibility_path",
        "preserve_required_existing_motion"
      ],
      "preservation": "new_project_boundary",
      "approval": "user_checkpoint_or_agent_acceptance_gate",
      "qa": "full_risk_based",
      "gsap_exceptions": [
        "explicit_static_or_minimal_motion",
        "required_existing_system_or_clone_fidelity",
        "concrete_runtime_performance_or_accessibility_constraint"
      ]
    },
    "substantial_redesign": {
      "imagegen_web": "conditional",
      "imagegen_conditions": [
        "visual_ambiguity",
        "image_led_direction",
        "concepts_requested",
        "insufficient_official_assets"
      ],
      "imagegen_skip": [
        "approved_direction_is_clear",
        "asset_rich_approved_system",
        "user_requests_supplied_assets_only"
      ],
      "gsap": "default_on_with_documented_exceptions",
      "gsap_conditions": [
        "brand_adapted_choreography",
        "runtime_support",
        "accessibility_path",
        "preserve_required_existing_motion"
      ],
      "preservation": "approved_content_ia_tracking_brand_facts",
      "approval": "user_checkpoint_or_agent_acceptance_gate",
      "qa": "full_risk_based",
      "gsap_exceptions": [
        "explicit_static_or_minimal_motion",
        "required_existing_system_or_clone_fidelity",
        "concrete_runtime_performance_or_accessibility_constraint"
      ]
    },
    "supplied_assets_only": {
      "imagegen_web": "off",
      "imagegen_conditions": [],
      "imagegen_skip": [
        "explicit_user_constraint"
      ],
      "gsap": "default_on_with_documented_exceptions",
      "gsap_conditions": [
        "brand_adapted_choreography",
        "runtime_support",
        "accessibility_path",
        "preserve_required_existing_motion"
      ],
      "preservation": "supplied_and_official_assets_only",
      "approval": "agent_acceptance_gate_unless_user_requests_checkpoint",
      "qa": "full_risk_based",
      "gsap_exceptions": [
        "explicit_static_or_minimal_motion",
        "required_existing_system_or_clone_fidelity",
        "concrete_runtime_performance_or_accessibility_constraint"
      ]
    },
    "surgical_edit": {
      "imagegen_web": "off_unless_asset_replacement_requires_generation",
      "imagegen_conditions": [
        "explicit_asset_replacement_and_no_verified_source"
      ],
      "imagegen_skip": [
        "scope_does_not_require_concepts"
      ],
      "gsap": "preserve_existing_unless_explicitly_changed",
      "gsap_conditions": [
        "explicit_motion_scope"
      ],
      "preservation": "minimal_scoped_changes_existing_stack_analytics_motion",
      "approval": "agent_acceptance_gate_unless_irreversible",
      "qa": "scoped_plus_regression_risk"
    },
    "static_minimal_motion": {
      "imagegen_web": "conditional",
      "imagegen_conditions": [
        "visual_ambiguity",
        "image_led_direction",
        "concepts_requested",
        "insufficient_official_assets"
      ],
      "imagegen_skip": [
        "approved_direction_is_clear",
        "user_requests_supplied_assets_only"
      ],
      "gsap": "off",
      "gsap_conditions": [],
      "preservation": "mode_dependent",
      "approval": "user_checkpoint_or_agent_acceptance_gate",
      "qa": "full_risk_based_static_motion_restraint"
    },
    "mobile_app_marketing": {
      "imagegen_web": "conditional",
      "imagegen_conditions": [
        "visual_ambiguity",
        "image_led_direction",
        "concepts_requested",
        "insufficient_official_assets"
      ],
      "imagegen_skip": [
        "approved_direction_is_clear",
        "user_requests_supplied_assets_only"
      ],
      "imagegen_mobile": "allowed_for_concept_labelled_app_screen_media_only",
      "gsap": "default_on_with_documented_exceptions",
      "gsap_conditions": [
        "brand_adapted_choreography",
        "runtime_support",
        "accessibility_path",
        "preserve_required_existing_motion"
      ],
      "preservation": "responsive_web_separate_from_app_screen_media",
      "approval": "user_checkpoint_for_conceptual_product_visuals_or_agent_gate_for_verified_screens",
      "qa": "full_risk_based",
      "gsap_exceptions": [
        "explicit_static_or_minimal_motion",
        "required_existing_system_or_clone_fidelity",
        "concrete_runtime_performance_or_accessibility_constraint"
      ]
    }
  }
}
```

## Resolution rule

Select exactly one mode. Evaluate its conditions from the actual brief and evidence. Record the resulting Imagegen, GSAP, preservation, approval, content, integration, viewport, and QA decisions with rationale in the build brief. A tool marked `conditional` is not automatically on. A documented skip is a valid result when its skip conditions are met.
For `default_on_with_documented_exceptions`, implement motion without asking the user to request it. Select static/minimal mode only from an actual constraint, not convenience or silence about animation. Supplied-assets-only restricts asset sourcing, not animation. Preserve existing systems when required; scope surgical edits to the request.

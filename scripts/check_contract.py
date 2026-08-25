#!/usr/bin/env python3
"""Semantic contract checks for landing-page routing and safety."""
from pathlib import Path
import json
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
text = SKILL.read_text(encoding="utf-8")
lines = text.splitlines()
errors = []

required_refs = [
    "references/policy-matrix.md",
    "references/intake-brand-assets.md",
    "references/frontend-skill-stack.md",
    "references/imagegen-production.md",
    "references/gsap-motion.md",
    "references/premium-quality-gate.md",
    "references/section-patterns.md",
    "references/verification-checklist.md",
]
for rel in required_refs:
    path = ROOT / rel
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"missing/empty reference: {rel}")
    if f"`{rel}`" not in text:
        errors.append(f"reference not routed from SKILL.md: {rel}")

if len(lines) > 500:
    errors.append(f"SKILL.md has {len(lines)} lines; must stay <= 500")
if "version: 3.2.0" not in text:
    errors.append("SKILL.md must declare version 3.2.0")
phase_numbers = [int(n) for n in re.findall(r"^## Phase (\d+):", text, re.M)]
if phase_numbers != list(range(1, 10)):
    errors.append(f"phase numbers must be 1-9; got {phase_numbers}")

for stale in [
    "required Imagegen Frontend Web references",
    "Default to a GSAP/ScrollTrigger pass",
    "at least two purposeful ScrollTrigger",
    "at least four layout families",
    "one strong hero plus at least two",
]:
    for path in [SKILL, ROOT / "references/imagegen-production.md", ROOT / "references/gsap-motion.md"]:
        if stale.lower() in path.read_text(encoding="utf-8").lower():
            errors.append(f"stale quota/mandate '{stale}' in {path.relative_to(ROOT)}")

try:
    policy_text = (ROOT / "references/policy-matrix.md").read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", policy_text, re.S)
    if not match:
        raise ValueError("policy-matrix.md has no fenced JSON object")
    policy = json.loads(match.group(1))
    if policy.get("version") != "3.2.0":
        errors.append("policy matrix version mismatch")
    modes = policy.get("modes", {})
    expected_modes = {
        "greenfield", "substantial_redesign", "supplied_assets_only",
        "surgical_edit", "static_minimal_motion", "mobile_app_marketing"
    }
    if set(modes) != expected_modes:
        errors.append(f"policy modes mismatch: {sorted(modes)}")
    if modes.get("greenfield", {}).get("imagegen_web") != "conditional":
        errors.append("greenfield Imagegen must be conditional")
    if modes.get("substantial_redesign", {}).get("imagegen_web") != "conditional":
        errors.append("substantial redesign Imagegen must be conditional")
    if modes.get("supplied_assets_only", {}).get("imagegen_web") != "off":
        errors.append("supplied-assets-only Imagegen must be off")
    if modes.get("static_minimal_motion", {}).get("gsap") != "off":
        errors.append("static mode GSAP must be off")
    if not modes.get("surgical_edit", {}).get("gsap", "").startswith("preserve_existing"):
        errors.append("surgical mode must preserve existing motion")
    if "concept_labelled" not in modes.get("mobile_app_marketing", {}).get("imagegen_mobile", ""):
        errors.append("mobile app concepts must be labelled")
    for name, mode in modes.items():
        if mode.get("gsap") == "required" or mode.get("imagegen_web") == "required":
            errors.append(f"{name} contains an unconditional tool mandate")
    shared = policy.get("shared", {})
    if "one short question at a time" not in shared.get("intake_style", "").lower():
        errors.append("sequential intake policy missing")
    if "exact_preservation" not in shared.get("content_default", ""):
        errors.append("exact user-copy default missing")
    if "Vercel" not in shared.get("deployment_default", ""):
        errors.append("default Vercel deployment policy missing")
    if "Never submit real" not in shared.get("integration_safety", ""):
        errors.append("integration side-effect guard missing")
    if "breakpoint boundary" not in shared.get("viewport_policy", ""):
        errors.append("risk-based viewport policy missing")
except Exception as exc:
    errors.append(f"invalid policy matrix: {exc}")
    modes = {}

try:
    eval_path = ROOT / "evals/evals.json"
    if eval_path.exists():
        eval_data = json.loads(eval_path.read_text(encoding="utf-8"))
        evals = eval_data.get("evals", [])
        required_eval_keys = ("id", "name", "prompt", "expected_mode", "expected_policy", "forbidden_actions")
    else:
        evals = runpy.run_path(str(ROOT / "scripts/eval_cases.py")).get("EVALS", [])
        required_eval_keys = ("id", "name", "expected_mode", "expected_policy", "forbidden_actions")
    if len(evals) < 8:
        errors.append(f"need at least 8 semantic evals; got {len(evals)}")
    ids = [item.get("id") for item in evals]
    if len(ids) != len(set(ids)):
        errors.append("eval ids must be unique")
    covered = {item.get("expected_mode") for item in evals}
    if set(modes) - covered:
        errors.append(f"evals do not cover modes: {sorted(set(modes)-covered)}")
    for item in evals:
        for key in required_eval_keys:
            if item.get(key) in (None, "", []):
                errors.append(f"eval {item.get('id')} missing {key}")
        if item.get("expected_mode") not in modes:
            errors.append(f"eval {item.get('id')} has unknown mode")
except Exception as exc:
    errors.append(f"invalid evals/evals.json: {exc}")
    evals = []

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if "Landing Page Skill v3.2" not in readme:
    errors.append("README is not v3.2")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"PASS: {len(lines)} lines, 9 phases, {len(required_refs)} references, {len(modes)} modes, {len(evals)} semantic evals")

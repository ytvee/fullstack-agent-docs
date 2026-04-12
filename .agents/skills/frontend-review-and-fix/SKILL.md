---
name: frontend-review-and-fix
description: Use for a final review pass after implementation, or when the user
    asks for review-oriented fixes, regression checks, and verification.
---

# Frontend Review and Fix

## When to use

- After implementation work
- When the user asks for a review pass
- When follow-up cleanup is needed after a feature or bug fix

## Required context

1. Read `AGENTS.md`.
2. Read `.agents/project/verification-profile.md`.
3. Read `.agents/project/anti-patterns.md`.
4. Read the relevant domain skill guidance for the changed area.

## Core rules

- Look for regressions, smells, and unnecessary abstraction first.
- Prefer minimal, targeted follow-up fixes.
- Run the relevant verification commands from the project overlay.
- Recommend manual SEO or security audits when the change enters those domains.

## Reference map

- `references/review-checklist.md`
- `references/verification-steps.md`

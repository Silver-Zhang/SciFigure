# SciFigure

SciFigure is a multi-agent workflow for generating editable scientific PowerPoint figures from a reference sketch, a style example, and user requirements.

The project is designed for research figures used in proposals, academic talks, thesis reports, and paper illustrations. It emphasizes scientific correctness, editable PowerPoint structure, controlled use of generated image assets, formula handling, and iterative human review.

## Core idea

A SciFigure task follows this loop:

1. Parse the user's figure request and uploaded reference images.
2. Write a task specification.
3. Summarize the target visual style.
4. Decide which elements must be editable PowerPoint objects and which local illustrations may be generated as images.
5. Select an operating-system-specific backend.
6. Generate the slide with editable shapes, text boxes, arrows, panels, and formula placeholders or equation objects.
7. Insert approved local image assets only where justified.
8. Export a preview image.
9. Run a quality check.
10. Iterate until the figure passes review or reports explicit manual actions.

## Modes

SciFigure defaults to `review_mode`.

In `review_mode`, the workflow pauses at key gates:

- task understanding;
- image asset decision;
- first preview;
- final delivery.

`auto_mode` may be used only when the user explicitly requests a fully automatic run.

## Backends

SciFigure selects a backend according to the current operating system:

- Windows: PowerShell + Microsoft PowerPoint COM automation.
- macOS: AppleScript / JXA for Microsoft PowerPoint where available; Python fallback.
- Linux: Python + `python-pptx`, with LibreOffice optional for preview export.

See `backend_policy.md` for details.

## Repository structure

```text
SciFigure/
├─ agent.md
├─ background.md
├─ style_guide.md
├─ formula_policy.md
├─ backend_policy.md
├─ skill.md
├─ templates/
├─ components/
├─ scripts/
├─ approved_examples/
├─ tasks/
├─ assets/
├─ outputs/
└─ logs/
```

## Basic usage

A typical request should provide:

```text
Task name:
Reference sketch:
Reference style image:
Core logic to express:
Required emphasis:
Content to weaken or remove:
Formula requirements:
Editable elements:
Allowed image assets:
Output filename:
Mode: review_mode / auto_mode
```

The controlling agent must read `agent.md`, `background.md`, `style_guide.md`, `formula_policy.md`, and `backend_policy.md` before starting.

## Design principles

- Never export the whole slide as one non-editable image.
- Keep titles, labels, arrows, panels, decision boxes, axes, and formulas editable whenever possible.
- Use generated images only for local scientific illustrations that are hard to draw cleanly with PowerPoint primitives.
- Never let an image generation agent create assets before an asset decision table is approved.
- Prefer clear scientific diagrams over decorative visual effects.

## Status

This repository currently contains the workflow specification, templates, backend policy, and starter component stubs. Implementation components will be expanded iteratively as real figure-generation tasks are added.

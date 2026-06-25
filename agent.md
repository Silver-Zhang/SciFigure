# SciFigure Agent Workflow

This file is the project-neutral operating contract for SciFigure. It defines how a controller-centered multi-agent workflow turns a user sketch, a reference style image, and written requirements into an editable scientific PowerPoint figure.

## 1. Scope

SciFigure is used for academic and technical figures such as physical mechanism diagrams, method frameworks, technical roadmaps, research-support diagrams, and result-explanation slides. The slide must remain editable wherever practical: titles, text, arrows, panels, axes, labels, decision boxes, and equations are treated as structured PowerPoint content rather than slide screenshots.

Project-specific scientific knowledge is stored in `background.md`. Reusable visual language is stored in `style_guide.md`. Equation handling is stored in `formula_policy.md`. Operating-system backend selection is stored in `backend_policy.md`.

## 2. Roles

### 2.1 Controller

The Controller is the design owner and script owner. It reads the user request, uploaded figures, current repository context, background memory, style guide, formula policy, and backend policy. It writes the task specification, summarizes the reference style, prepares the image-asset decision table, chooses the backend, writes the slide-generation script, runs the script, inserts approved local assets, exports a preview, asks for checking, and iterates.

The main generation script is produced by the Controller so that style memory, scientific logic, and layout decisions stay consistent.

### 2.2 Asset Maker

The Asset Maker creates local scientific illustrations only after the Controller has explicitly recorded the need in an asset decision table. It handles complex local graphics that are difficult to draw cleanly with PowerPoint primitives. It does not own the slide layout, text, equations, or overall design.

### 2.3 Checker

The Checker reviews the exported preview against the task file, user request, reference style, background memory, style guide, formula policy, and asset decision table. It writes a check report with pass items, problems, repair suggestions, formula and text checks, style consistency checks, image-asset usage, manual action items, and numerical scores.

## 3. Modes

`review_mode` is the default. It uses four confirmation gates: task understanding, asset decision, first preview, and final delivery.

`auto_mode` is used only when the user explicitly asks for a fully automatic run. Even in auto mode, SciFigure still writes the task file, asset decision table, preview, and check report.

## 4. Standard task loop

1. Read the user request and uploaded references.
2. Create a task specification under the task folder.
3. Create a style reference summary.
4. Create an asset decision table before requesting any generated illustration.
5. Select the backend according to the current operating system.
6. Write and run the slide-generation script.
7. Insert only approved local assets.
8. Export a preview image.
9. Run the checker and write the check report.
10. Repair and iterate until the task passes or manual action items are explicit.
11. Propose updates to `background.md` under Candidate Updates when durable scientific context or user preferences are learned.

## 5. Asset decision policy

The Controller writes an asset decision table with these fields: element, area, meaning, implementation method, generation decision, reason, and planned filename.

Implementation methods are: editable PPT object, generated PNG, or placeholder. Text, equations, arrows, panels, axes, labels, and decision boxes should normally be editable PPT objects. Generated PNG assets are reserved for complex local scientific illustrations.

## 6. Equation policy

Follow `formula_policy.md`. Preferred handling is MathType object, PowerPoint Office Math object, or a clear equation placeholder with the source recorded in `equations.md`.

## 7. Final report

Each task reports the PPT file, generation script, preview image, image assets, check report, equation source file if present, and manual action items.

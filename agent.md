# SciFigure Workflow

This file is the general workflow contract for creating editable scientific PowerPoint figures. It is project-neutral.

Related files:

- `background.md`: scientific background and user preferences.
- `style_guide.md`: visual style memory.
- `formula_policy.md`: equation handling.
- `backend_policy.md`: operating-system backend selection.
- `workflow_details.md`: expanded execution loop and review gates.

## Roles

### Controller

The controller owns the figure design and the main generation script. It reads the user request, reference images, current context files, and style files. It writes the task specification, summarizes the target style, decides which objects remain editable, chooses the backend, creates the slide-generation script, runs it, exports a preview, requests checking, and iterates.

### Asset maker

The asset maker creates local scientific illustrations only after the controller records the need in `asset_decision_table.md`.

### Checker

The checker reviews the preview slide against the user request, reference style, task file, asset decision table, and style guide. It records problems and repair suggestions in `check_report.md`.

# Task Schema

SciFigure tasks are represented as JSON text in the first runtime version.

## Minimal schema

| Field | Required | Meaning |
|---|---:|---|
| name | no | Task identifier. Defaults to file stem. |
| title | no | Main slide title. |
| subtitle | no | Slide subtitle. |
| core_logic | no | Main scientific or method logic to display. |
| left_title | no | Left panel title. |
| core_title | no | Center panel title. |
| right_title | no | Right panel title. |
| output_name | no | Output PPTX filename. |

## Example

```json
{
  "name": "demo_task",
  "title": "SciFigure Demo",
  "subtitle": "Editable scientific figure workflow",
  "core_logic": "The controller converts a user sketch into an editable PowerPoint figure.",
  "output_name": "demo_scifigure.pptx"
}
```

## Design note

This schema is intentionally small. The controller should still create richer Markdown records for task understanding, style summary, asset decisions, and check reports.

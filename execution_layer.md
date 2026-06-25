# Execution Layer

This document describes the first executable layer of SciFigure.

## Purpose

The execution layer turns a task specification into an editable PowerPoint file. The first implementation is intentionally conservative: it creates a clean editable PPTX skeleton with panels, text boxes, and placeholders. It does not attempt to solve all design problems automatically.

## Portable Python backend

Files:

- `scifigure_runtime.py`
- `run_demo.py`
- `jobs/demo_task.txt`

The Python backend uses `python-pptx` and therefore works on Windows, macOS, and Linux. It is also the fallback backend when native Microsoft PowerPoint automation is unavailable.

## Task input

The current minimal task file is JSON text. Required and optional fields:

```json
{
  "name": "demo_task",
  "title": "Main title",
  "subtitle": "Subtitle",
  "core_logic": "Scientific or method logic to display.",
  "left_title": "Input",
  "core_title": "Core method",
  "right_title": "Output",
  "output_name": "demo_scifigure.pptx"
}
```

## Run

```bash
pip install -r requirements.in
python run_demo.py
```

Direct call:

```bash
python scifigure_runtime.py jobs/demo_task.txt --output-dir result/demo
```

## Output

The runtime writes:

- editable PPTX file;
- initial `check_report.md`.

## Limitations

- The Python backend cannot reliably create native PowerPoint equation objects.
- Complex local scientific illustrations are still handled through the asset decision workflow.
- Preview export is backend dependent and will be added in a later iteration.

## Next implementation steps

1. Add Windows PowerPoint COM backend.
2. Add asset insertion from the task file.
3. Add simple editable curve and flow components.
4. Add preview export.
5. Add automatic structural checks for overlap and missing assets.

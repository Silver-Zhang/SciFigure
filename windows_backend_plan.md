# Windows Backend Plan

The Windows backend will use PowerPoint automation from PowerShell. It is the preferred backend when Microsoft PowerPoint is installed.

## Responsibilities

- connect to an open PowerPoint instance or create a new one;
- create a 16:9 slide;
- add editable titles, panels, labels, arrows, and decision boxes;
- insert approved local image assets;
- create equation objects when available or place equation placeholders;
- export a preview image;
- save the presentation.

## Status

The portable Python backend is implemented first. The Windows backend should reuse the same task schema and check-report structure.

## Design constraint

The Controller must generate the task-specific PowerShell script. Helper functions can be stored under `components/win` after local testing.

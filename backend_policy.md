# Backend Policy

SciFigure selects the slide-generation backend according to the operating system.

## Windows

Use PowerShell plus Microsoft PowerPoint COM automation when PowerPoint is installed.

## macOS

Use AppleScript or JavaScript for Automation when Microsoft PowerPoint automation is available. Use the Python backend as fallback.

## Linux

Use Python plus python-pptx. LibreOffice headless may be used for preview export.

## Detection result names

- windows_ppt_com
- macos_ppt_script
- python_pptx
- python_pptx_fallback

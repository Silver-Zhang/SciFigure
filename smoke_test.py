"""Smoke test for the portable SciFigure runtime."""

from __future__ import annotations

import tempfile
from pathlib import Path

from scifigure_runtime import build_ppt, load_task, write_report


def test_demo_task() -> None:
    task = load_task(Path("jobs/demo_task.txt"))
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        ppt = build_ppt(task, out_dir)
        report = write_report(task, out_dir, ppt)
        assert ppt.exists(), ppt
        assert report.exists(), report
        assert ppt.suffix == ".pptx"


if __name__ == "__main__":
    test_demo_task()
    print("SciFigure smoke test passed.")

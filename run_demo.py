from pathlib import Path

from scifigure_runtime import build_ppt, load_task, write_report

root = Path(__file__).resolve().parent
task = load_task(root / "jobs" / "demo_task.txt")
out_dir = root / "result" / "demo"
ppt = build_ppt(task, out_dir)
report = write_report(task, out_dir, ppt)
print(ppt)
print(report)

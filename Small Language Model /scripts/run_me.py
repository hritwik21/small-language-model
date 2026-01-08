"""
Reproduce all figures by executing the main experiment notebook.

Usage:
  python scripts/run_me.py
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB_IN = ROOT / "notebooks" / "experiments.ipynb"
NB_OUT = ROOT / "notebooks" / "experiments.executed.ipynb"

def main() -> None:
    if not NB_IN.exists():
        raise FileNotFoundError(f"Notebook not found: {NB_IN}")

    # Execute notebook from repo root so relative paths like ./datasets/... work.
    cmd = [
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--ExecutePreprocessor.timeout=-1",
        "--output", str(NB_OUT),
        str(NB_IN),
    ]
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(ROOT))
    print(f"Done. Executed notebook saved to: {NB_OUT}")

if __name__ == "__main__":
    main()

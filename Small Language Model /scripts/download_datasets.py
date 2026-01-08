"""
Optional helper to download *open* datasets and write them into the folder
structure expected by the notebook.

This script intentionally does NOT download Penn Treebank (PTB), since PTB is
often distributed under licensing restrictions.

Usage:
  python scripts/download_datasets.py
"""
from __future__ import annotations
import os
from pathlib import Path

def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def write_splits_from_text(text: str, out_dir: Path, train=0.9, valid=0.05) -> None:
    # Simple deterministic split by character count.
    n = len(text)
    n_train = int(train * n)
    n_valid = int(valid * n)
    train_text = text[:n_train]
    valid_text = text[n_train:n_train+n_valid]
    test_text  = text[n_train+n_valid:]
    (out_dir / "train.txt").write_text(train_text, encoding="utf-8")
    (out_dir / "valid.txt").write_text(valid_text, encoding="utf-8")
    (out_dir / "test.txt").write_text(test_text, encoding="utf-8")

def download_tiny_shakespeare(out_dir: Path) -> None:
    # Public-domain text; common mirror used in many tutorials.
    import requests
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    print("Downloading Tiny Shakespeare...")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    write_splits_from_text(r.text, out_dir)

def download_wikitext2(out_dir: Path) -> None:
    # Requires: pip install datasets
    from datasets import load_dataset
    print("Downloading WikiText-2 (raw)...")
    ds = load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1")
    # Each example is a line; join with newlines.
    (out_dir / "train.txt").write_text("\n".join(ds["train"]["text"]), encoding="utf-8")
    (out_dir / "valid.txt").write_text("\n".join(ds["validation"]["text"]), encoding="utf-8")
    (out_dir / "test.txt").write_text("\n".join(ds["test"]["text"]), encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    datasets_dir = root / "datasets"
    ensure_dir(datasets_dir)

    ts_dir = datasets_dir / "tiny_shakespeare"
    wt_dir = datasets_dir / "wikitext-2"
    ensure_dir(ts_dir)
    ensure_dir(wt_dir)

    # Downloaders
    try:
        download_tiny_shakespeare(ts_dir)
        print(f"Tiny Shakespeare written to {ts_dir}")
    except Exception as e:
        print("Tiny Shakespeare download failed:", e)
        print("You can manually place train/valid/test.txt under datasets/tiny_shakespeare/")

    try:
        download_wikitext2(wt_dir)
        print(f"WikiText-2 written to {wt_dir}")
    except Exception as e:
        print("WikiText-2 download failed:", e)
        print("If you want to use this helper, install extra deps: pip install datasets requests")

if __name__ == "__main__":
    main()

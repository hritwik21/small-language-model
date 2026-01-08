# Small Language Models Under Compute Constraints

This repository contains a small-scale language modeling study where I implemented a sequence of increasingly expressive next-token predictors—**Linear**, **MLP**, **Multi-head Self-Attention**, and a small **Transformer**—and compared them under a compute budget using **training FLOPs**.

**Context:** Coursework mini-project for *CS689 Machine Learning (UMass Amherst, Fall 2025)*.

## What I built

Character-level (Tiny Shakespeare):
- Linear predictor (softmax regression over a fixed context window)
- Multi-layer Perceptron (MLP)
- Multi-head self-attention
- Multi-layer Transformer

Word-level:
- Took the best character-level architecture (Transformer) and trained it on **PTB** and **WikiText-2** at the *word level*.

## Key takeaways

- Transformer-based models achieved the best test log-likelihood among the evaluated architectures, at a higher compute cost.
- Context length helped simpler models up to a point, but longer contexts increased compute and did not always translate into better generalization.
- Scaling from character to word tokenization increases vocabulary size substantially, impacting both compute and quality.

## Results (plots)

Character-level (Tiny Shakespeare):
- Training loss curves: Linear / MLP / Self-Attention / Transformer
- Test log-likelihood vs hyperparameters (e.g., context length, heads)
- Test log-likelihood vs training FLOPs

Word-level (PTB & WikiText-2):
- Training loss curves
- Test log-likelihood vs training FLOPs
- Generated samples (see report)

Figures are in [`figures/`](figures/). The full write-up is in [`docs/report.pdf`](docs/report.pdf).

## Repository structure

```
.
├── notebooks/
│   └── experiments.ipynb        # End-to-end experiment runner (original notebook)
├── scripts/
│   ├── run_me.py                # Reproduce figures by executing the notebook
│   └── download_datasets.py     # (Optional) helper for fetching open datasets
├── figures/                     # Saved plots used in the report/README
├── datasets/                    # NOT versioned by default (see datasets/README.md)
└── docs/
    └── report.pdf
```

## Setup

### 1) Create environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Prepare datasets
Place datasets in the following structure (matching the notebook):
```
datasets/
  tiny_shakespeare/{train.txt,valid.txt,test.txt}
  wikitext-2/{train.txt,valid.txt,test.txt}
  ptb/{train.txt,valid.txt,test.txt}   # if you have the appropriate license
```

If you *don’t* want to keep datasets in git (recommended), follow `datasets/README.md`.  
An optional helper is provided:
```bash
python scripts/download_datasets.py
```

### 3) Reproduce the figures
```bash
python scripts/run_me.py
```

This executes the notebook end-to-end and regenerates plots.

## Notes on FLOP counting

FLOPs are estimated during training using PyTorch’s `FlopCounterMode` (forward + backward), to relate model quality to compute.

## License

This repo is intended as an educational project. See `LICENSE` for details.

## Citation

If you reference this work, please cite the report or link to this repository.

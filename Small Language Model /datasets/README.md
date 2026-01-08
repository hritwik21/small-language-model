# Datasets

The original experiments expect the following folders:

```
datasets/
  tiny_shakespeare/{train.txt,valid.txt,test.txt}
  wikitext-2/{train.txt,valid.txt,test.txt}
  ptb/{train.txt,valid.txt,test.txt}
```

## Recommendation (for public GitHub repos)

Do **not** commit datasets into git. Add `datasets/` to `.gitignore` (already configured) and provide instructions/scripts for reproducing.

### Tiny Shakespeare
Public-domain Shakespeare text is commonly used for this benchmark. You can download a tiny Shakespeare corpus and create train/valid/test splits using `scripts/download_datasets.py`.

### WikiText-2
WikiText-2 is available via common dataset libraries (e.g., Hugging Face Datasets). The helper script can download and write out `train/valid/test.txt`.

### Penn Treebank (PTB)
PTB is commonly distributed under licensing restrictions. If you have access via your institution/course, place the split files under `datasets/ptb/`.

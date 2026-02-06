# Fine-Tuning Session — Repository Overview

This repository contains code, notebooks, and assets used for a fine-tuning session (Harry Potter dataset). Files that are excluded from version control are listed in `.gitignore` and are intentionally not documented here.

## Purpose
Provide scripts and notebooks to extract and preprocess text data, prepare datasets, and run fine-tuning and model comparison experiments.

## Files in this repository

- `requirements.txt`: Python dependencies required to run the notebooks and scripts.
- `extract_text.py`: Script to extract raw text from source documents (PDFs or other sources) used to build the dataset.
- `process_text.py`: Primary preprocessing pipeline that cleans, splits, and formats text for dataset creation and tokenization for Mistral Ai.
- `process_text2.py`: Alternate preprocessing script; useful for testing different cleaning/tokenization approaches for geema ai..
- `fine_tune_final.ipynb`: Final notebook that performs model fine-tuning (training configuration, checkpoints, and evaluation). Use this for the canonical training workflow.
- `model_compare.ipynb`: Notebook for comparing baseline and fine-tuned models, running inference examples, and reporting metrics.
- `harrypotter.pdf`: Source PDF used as one of the text inputs for extraction (kept under version control here). If you use different sources, update `extract_text.py` accordingly.
- `.gitignore`: Lists files and folders excluded from the repository (large artifacts, outputs, and local environments). See it for which files are intentionally omitted from this README.

## Not included here (excluded by .gitignore)
Large model/adaptor artifacts, datasets, notebooks or outputs listed in `.gitignore` are omitted from this README. Check `.gitignore` for the definitive list of excluded items.

## Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv #use python3 in linuix /mac.
```
2. Activate venv
For Linuix
```bash
source venv/bin/activate
```
for windows
```bash
venv/scripts/activate
```
```bash
pip install -r requirements.txt
```

2. Extract and preprocess text (example):

```bash
python extract_text.py
python process_text.py
```

3. Open the fine-tuning or comparison notebooks in google colob/jupyter notebook and follow the cells:
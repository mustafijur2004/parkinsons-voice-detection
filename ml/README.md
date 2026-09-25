# Parkinson's Voice Detection ML Pipeline

This directory contains the machine-learning research pipeline for the Parkinson's disease detection prototype. The pipeline will eventually cover dataset preparation, voice-derived feature extraction, model training, evaluation, and prediction.

## Research status

The dataset, algorithm, and evaluation approach are still being decided during the research phase. Implementations should remain modular so that candidate datasets, feature sets, and algorithms can be compared without coupling the research workflow to a single choice.

## Research priorities

- **Reproducibility:** record dataset versions, preprocessing settings, feature-extraction parameters, random seeds, and experiment configurations.
- **Avoiding data leakage:** keep training, validation, and test data separated; fit preprocessing steps only on training data; and ensure that related samples or speakers do not cross dataset splits.
- **Clear evaluation:** document assumptions, metrics, baselines, and limitations before drawing conclusions from results.

## Directory structure

- `data/` — dataset documentation and local data-processing placeholders.
- `features/` — voice feature extraction modules and configuration placeholders.
- `models/` — training, evaluation, and prediction modules.
- `notebooks/` — exploratory research notebooks.

Do not commit private datasets, credentials, generated model artifacts, or other sensitive research material to the repository.

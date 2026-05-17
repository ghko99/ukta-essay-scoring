# ukta-essay-scoring

Experiment workspace for essay scoring and linguistic feature pipelines.

## Layout

- `apps/morpheme/`: morpheme and sequence-model experiments with local data preparation scripts.
- `apps/cohesion/`: cohesion-related sentence transformer components and evaluation code.

## Setup

Install dependencies inside the app directory you plan to run. For example:

```bash
cd apps/morpheme
pip install -r requirements.txt
```

## Data and outputs

Keep downloaded corpora, generated `.data/` directories, model checkpoints, and experiment outputs out of Git.

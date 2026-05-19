# Reproducibility Notes

Use this checklist before publishing or comparing experiment results from this workspace.

## Environment

- Record Python version and package lock state for the app directory.
- Note CUDA, GPU type, and CPU-only fallbacks when relevant.
- Keep local corpora and generated `.data/` directories outside Git.

## Run Metadata

For each run, preserve:

- Git commit and app path.
- Dataset split name and preprocessing command.
- Model architecture and feature configuration.
- Random seed and training command.
- Metric script and output file path.

## Result Handling

Store raw logs, checkpoints, and prediction exports in an external run folder. Commit only small curated summaries or documentation that explain how the result was produced.

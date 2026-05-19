# Pipeline Notes

The workspace contains separate morpheme and cohesion experiment apps. Keep each pipeline isolated unless a shared artifact is intentionally introduced.

## Morpheme App

- Install dependencies from `apps/morpheme/`.
- Keep downloaded corpora and generated `.data/` folders local.
- Record tokenizer, feature extraction, and model settings with each run.

## Cohesion App

- Install dependencies from `apps/cohesion/`.
- Track sentence-transformer model names and revisions.
- Save evaluation outputs with the split and feature configuration in the filename.

## Cross-App Notes

When comparing outputs across apps, include the source split, preprocessing revision, and metric implementation. Avoid reusing generated files between apps unless the path and schema are documented.

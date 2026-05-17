# Morpheme App Setup

The morpheme app uses local dataset files under `apps/morpheme/.data/`.

## Install dependencies

```bash
cd apps/morpheme
pip install -r requirements.txt
```

## Prepare data

```bash
bash prepare.sh
```

The script expects compressed Multi30k files under `.data/multi30k/raw/` before decompression. If those files are missing, download or place them locally first.

## Generated artifacts

Do not commit `.data/`, model checkpoints, logs, or temporary experiment outputs. These files are machine-local and can be regenerated.

# App Handoff Notes

The morpheme and cohesion apps should exchange artifacts only through documented files and schemas.

## Handoff Contract

- Source split name and preprocessing command.
- Feature schema or embedding model revision.
- Output file path and format.
- Metric script used by the consuming app.
- Any filtering or normalization applied before handoff.

## Checks

- Verify row counts before and after handoff.
- Preserve stable ids so outputs can be joined back to source examples.
- Keep generated `.data/` folders and checkpoints out of Git.
- Record app-specific package versions when comparing outputs.

## Reporting

When a result depends on both apps, include both app paths and artifact revisions in the summary.

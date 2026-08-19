---
name: latex-research-ingest
description: Locally ingest research PDFs for this LaTeX manuscript and retrieve targeted source context.
---

# LaTeX Research Ingest

Use the bundled `research_store.py` script for local PDF ingestion and
retrieval. Its generated store lives under `.agent-runtime/research/` and is
not manuscript source.

Ingest specific PDF files supplied by the user or stored in an intentional
repository reference location:

```bash
python3 agent_environment/skills/latex-research-ingest/scripts/research_store.py ingest . path/to/source.pdf
```

Retrieve targeted context with:

```bash
python3 agent_environment/skills/latex-research-ingest/scripts/research_store.py retrieve . "search terms"
```

Treat `main.tex` and `references.bib` as authoritative for manuscript claims.
Verify precise claims against the original PDF before changing prose or
bibliography data.

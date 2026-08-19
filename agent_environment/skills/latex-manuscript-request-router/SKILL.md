---
name: latex-manuscript-request-router
description: Route a LaTeX theory-manuscript request to the smallest applicable local skill.
---

# LaTeX Manuscript Request Router

1. Read `AGENTS.md`, `VISION.md`, `main.tex`, and `references.bib`.
2. Classify the request as manuscript interpretation, source edit, derivation
   audit, equation lookup, notation propagation, citation check, display-math
   cleanup, narrative review, or research retrieval.
3. Select the matching LaTeX skill. For a rendered equation number, resolve it
   through `build/main.aux` before answering or editing.

For an edit, route quickly, make the narrow change requested, and rebuild the
root manuscript when labels, citations, or display structure may have changed.

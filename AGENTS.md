# AGENTS.md

## Scope

This repository contains only the LaTeX theory manuscript *Apparent
non-associative plasticity from true deformation and distension*, its
bibliography, and manuscript-development instructions and skills. Do not add
simulation code, validation decks, implementation papers, generated outputs,
or unrelated research artifacts.

## Portable agent environment

- Treat this file as the universal agent entry point.
- At the first relevant query, run `tools/agentctl route "<query>"` and use the
  smallest applicable profile and skill set.
- Resolve operational paths from the repository root. Keep generated state
  under ignored runtime locations and commit only authoritative manuscript,
  bibliography, instructions, skills, and intentional reference material.

## Manuscript workflow

- Read `VISION.md`, `main.tex`, and `references.bib` before interpreting or
  editing the manuscript. `main.tex` is the sole document root.
- Read `author_style_profile_2026-07-27.md` before every edit. Preserve the
  manuscript's notation, equation labels, and technical distinctions unless
  the user explicitly requests a change.
- Cite source locations as `file:line` when making claims about manuscript
  text, notation, assumptions, derivations, or references.
- If the user cites a rendered equation number, resolve it through
  `build/main.aux`. Rebuild from `main.tex` if the build artifacts are stale.
- For a notation or derivation change, trace its effects through definitions,
  chain-rule terms, constitutive restrictions, and downstream prose.
- Do not edit text between `% AGENT-LOCK-BEGIN` and `% AGENT-LOCK-END` unless
  the user explicitly authorizes that edit.
- Number and label every displayed equation or identity introduced by an agent.
  Use `align` for multi-step equalities; do not introduce chained equalities on
  one numbered line.
- Treat displays as grammatical parts of their surrounding sentences and
  punctuate them accordingly. Do not use manual delimiter sizing commands.

## Builds and bibliography

- Run manuscript builds through the repository-local
  `latex-workshop-recompile` skill after every edit to `main.tex` or
  `references.bib`.
- Direct all LaTeX output to `build/`. Confirm that no generated artifacts are
  left at the repository root.
- Before changing citation-backed text or bibliography data, verify the cited
  source with the applicable manuscript research skill.

## Editing discipline

- Keep edits narrow and preserve unrelated worktree changes unless the user
  explicitly asks to remove them.
- Use focused source inspection before broad rewrites. Do not introduce helper
  notation without explicit user approval when the existing primitive variables
  state the result clearly.
- Write for readers versed in continuum mechanics and plasticity. State the
  physical role of a result positively and avoid drafting-history commentary.

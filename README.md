# Apparent non-associative plasticity from distinct isochoric and volumetric mechanisms

`main.tex` is the manuscript root and `references.bib` is its bibliography.
Build with `latexmk -outdir=build main.tex`; all generated LaTeX artifacts
belong in `build/`. The build derives the first and latest commit dates used in
the generative-AI declaration directly from the reachable Git history.

During revision, run `python3 tools/build-revision.py` to update the manuscript,
the reviewer response (`revisions/point-by-point-response.tex`), and the
marked-up comparison. Their PDFs are `build/main.pdf`,
`build/point-by-point-response.pdf`, and
`build/revised-manuscript-latexdiff.pdf`. The comparison uses repository commit
`a621b46d76ff4adb8a014dd180378a1bca76af08` as its baseline; its identity with
the submitted manuscript has not been independently verified.

The repository retains only manuscript-development instructions and skills in
`AGENTS.md` and `agent_environment/`.

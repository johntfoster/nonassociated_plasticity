#!/usr/bin/env python3
"""Build the working manuscript, reviewer response, and marked-up comparison."""
from pathlib import Path
import subprocess
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parent.parent
BASELINE = 'a621b46d76ff4adb8a014dd180378a1bca76af08'
BUILD = ROOT / 'build'
LATEX = ['latexmk', '-lualatex', '-interaction=nonstopmode', '-halt-on-error']

def run(args, cwd=ROOT):
    subprocess.run(args, cwd=cwd, check=True)

def git_file(name):
    return subprocess.check_output(['git', 'show', f'{BASELINE}:{name}'], cwd=ROOT, text=True)

def expand(source, bibliography):
    return source.replace(r'\bibliography{references}', bibliography).replace(r'\bibliographystyle{plain}', '')

BUILD.mkdir(exist_ok=True)
for name, path in [('TEXMFVAR', ROOT / '.agent-runtime/tex-cache/var'),
                   ('TEXMFCACHE', ROOT / '.agent-runtime/tex-cache/cache')]:
    path.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(path)
run(LATEX + ['-outdir=build', 'main.tex'])
run(LATEX + ['-outdir=build', 'revisions/point-by-point-response.tex'])
with tempfile.TemporaryDirectory(prefix='revision-baseline-', dir=BUILD) as temp:
    old = Path(temp)
    (old / 'main.tex').write_text(git_file('main.tex'))
    (old / 'references.bib').write_text(git_file('references.bib'))
    run(LATEX + ['-outdir=build', 'main.tex'], cwd=old)
    (old / 'old.tex').write_text(expand((old / 'main.tex').read_text(), (old / 'build/main.bbl').read_text()))
    (old / 'new.tex').write_text(expand((ROOT / 'main.tex').read_text(), (BUILD / 'main.bbl').read_text()))
    diff = subprocess.check_output(['latexdiff', '--type=CFONT', '--config',
        'PICTUREENV=(?:picture|tikzpicture)', str(old / 'old.tex'), str(old / 'new.tex')], cwd=ROOT, text=True)
    # Deleted prose can still cite a baseline equation whose label was removed.
    # Preserve its original number in the comparison without adding a number
    # to the current manuscript.
    label_pattern = r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}'
    old_labels = dict(re.findall(label_pattern, (old / 'build/main.aux').read_text()))
    new_labels = dict(re.findall(label_pattern, (BUILD / 'main.aux').read_text()))
    for label, number in old_labels.items():
        if label not in new_labels:
            diff = diff.replace(r'\eqref{' + label + '}', '(' + number + ')')
    diff = diff.replace(r'\protect\color{blue} \sf #1', r'\protect\color{blue} #1')
    diff = diff.replace(r'\protect\color{red} \scriptsize #1', r'\protect\color{red} #1')
    diff = diff.replace(r'\begin{document}', '\\setlength{\\emergencystretch}{3em}\n' + r'\begin{document}')
    legend = r'''\maketitle
\begin{center}\small
Marked-up comparison against the preserved pre-edit repository manuscript.\\
\textcolor{blue}{Blue: additions.}\quad \textcolor{red}{Red: deletions.}\\
Baseline commit: \texttt{a621b46d76ff4adb8a014dd180378a1bca76af08}.\\
The exact submitted-file identity has not been independently established.
\end{center}'''
    diff = diff.replace(r'\maketitle', legend, 1)
    (BUILD / 'revised-manuscript-latexdiff.tex').write_text(diff)
run(LATEX + ['-outdir=build', 'build/revised-manuscript-latexdiff.tex'])
print('Current manuscript, response, and comparison are in build/.')

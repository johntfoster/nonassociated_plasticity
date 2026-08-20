# Repository-wide default: write every LaTeX build product under ./build/
# relative to the directory where latexmk is invoked.
$out_dir = 'build';

# Generate the manuscript's AI-declaration dates from the reachable Git history
# before every build.
my $git_date_status = system(
    'python3',
    'tools/write_git_history_dates.py',
    '--output',
    'build/git-history-dates.tex'
);
die "Could not generate Git history dates\n" if $git_date_status != 0;

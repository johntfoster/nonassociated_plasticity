#!/usr/bin/env python3
"""Write LaTeX macros for the first and latest reachable Git commit dates."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def commit_dates(repo: Path) -> tuple[datetime, datetime]:
    result = subprocess.run(
        ["git", "log", "--reverse", "--format=%aI", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    dates = [datetime.fromisoformat(line) for line in result.stdout.splitlines()]
    if not dates:
        raise RuntimeError("Git history contains no commits")
    return dates[0], dates[-1]


def latex_date(value: datetime) -> str:
    return f"{value.day} {MONTHS[value.month - 1]} {value.year}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    first, latest = commit_dates(repo)
    output = args.output if args.output.is_absolute() else repo / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    content = (
        "% Generated from Git history; do not edit.\n"
        f"\\providecommand{{\\GitHistoryFirstDate}}{{{latex_date(first)}}}\n"
        f"\\providecommand{{\\GitHistoryLastDate}}{{{latex_date(latest)}}}\n"
    )
    output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()

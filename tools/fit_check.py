#!/usr/bin/env python3
"""Estimate whether a CV draft fits one page BEFORE building it.

Usage: python3 tools/fit_check.py draft.txt   (or pipe the draft on stdin)

Draft format (same as the chat draft):
  - first paragraph that isn't the name/contact line = summary
  - bullets start with "- " (PM, CSM, Peres, Projects)
  - a line "PROJECTS" marks the Projects section
  - Skills rows look like "Label: term, term, ..." after a "SKILLS" line
  If the CSM or Peres bullets are left out (locked text), their fixed lines are added.

Calibrated 2026-09-30 on 15 one-page builds (Jerry V2 layout, Calibri 10pt, 1cm margins):
  ~128 characters per wrapped line; one-page builds ran 26-30 "content lines"
  (summary + bullets + project items). Meroka v1 estimated 30 with a Projects section
  and overflowed by ~4 lines; its one-page version estimated 26.
  Babylist (2026-09-30) estimated 29 and overflowed ~2 lines: bullets are indented, so a bullet
  just under 256 chars (2.0 x 128) wraps to 3 lines. Keep each bullet under ~245 chars.
"""
import math
import sys

CHARS_PER_LINE = 128
BUDGET_NO_PROJECTS = 29   # 30 fit twice (Akur8, PIP Canada) but with no spare line
BUDGET_WITH_PROJECTS = 26  # the Projects header + spacing cost ~2 lines
SKILLS_ROW_MAX = 115
CSM_LOCKED_LINES = 6       # 3 locked bullets, 2 lines each (promoted line is fixed overhead)
PERES_LOCKED_LINES = 3


def lines(text):
    return max(1, math.ceil(len(text.strip()) / CHARS_PER_LINE))


def main():
    raw = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    rows = [r.rstrip() for r in raw.splitlines()]
    summary = None
    section = None
    total = 0
    detail = []
    has_projects = False
    saw_csm = saw_peres = False
    skills = []
    for r in rows:
        t = r.strip().strip('*')
        if not t:
            continue
        up = t.upper()
        if up in ("EXPERIENCE", "SKILLS", "PROJECTS", "EDUCATION", "LANGUAGES"):
            section = up
            has_projects |= up == "PROJECTS"
            continue
        if "Customer Success Manager" in t and len(t) < 80:
            section = "CSM"
        if "Peres Center" in t:
            section = "PERES"
        if t.startswith("- ") or t.startswith("• "):
            body = t[2:]
            if section == "SKILLS":
                skills.append(body)
                continue
            n = lines(body)
            total += n
            saw_csm |= section == "CSM"
            saw_peres |= section == "PERES"
            detail.append((n, len(body), body[:60]))
            continue
        if section == "SKILLS" and ":" in t:
            skills.append(t)
            continue
        if summary is None and section is None and len(t) > 150:
            summary = t
            n = lines(t)
            total += n
            detail.insert(0, (n, len(t), "SUMMARY: " + t[:50]))
    if not saw_csm:
        total += CSM_LOCKED_LINES
        detail.append((CSM_LOCKED_LINES, 0, "CSM locked bullets (assumed)"))
    if not saw_peres:
        total += PERES_LOCKED_LINES
        detail.append((PERES_LOCKED_LINES, 0, "Peres locked bullets (assumed)"))
    budget = BUDGET_WITH_PROJECTS if has_projects else BUDGET_NO_PROJECTS
    for n, c, s in detail:
        print(f"{n} line(s)  {c:>4} chars  {s}")
    print(f"\nContent lines: {total}  |  budget: {budget} ({'with' if has_projects else 'no'} Projects)")
    for s in skills:
        if len(s) > SKILLS_ROW_MAX:
            print(f"SKILLS ROW TOO LONG ({len(s)} > {SKILLS_ROW_MAX}): {s[:60]}")
    if total > budget:
        print(f"OVER by ~{total - budget} line(s): trim before building.")
        print("Cheapest cuts: bullets whose last line is short (chars just over a multiple of 128),")
        print("the summary's last line, a Projects item.")
        sys.exit(1)
    print(f"FITS (spare ~{budget - total} line(s)).")


if __name__ == "__main__":
    main()

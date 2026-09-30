# Career area — rules and file map

This repo runs Kfir's job search. Claude drafts; Kfir approves and sends. Claude never applies,
messages anyone, or posts anything.

## Read before writing anything
1. `CLAUDE.md` (this file)
2. `career-agent.md` (role, hard rules)
3. `career-context.md` (the facts file: single source of truth)

## File map
```
career/
├── CLAUDE.md                  <- this file: rules + map
├── career-agent.md            <- the agent: role, inputs, workflows, hard rules
├── career-context.md          <- facts file. Every CV line / answer must trace back here
├── reference-jerry-peer-note.md  <- the note this setup is based on (reference only)
├── skills/
│   ├── vet-job.md             <- blunt verdict on a posting (do this first, always)
│   ├── find-roles.md          <- search sources, queries, result format
│   ├── tailor-cv.md           <- capped, step-by-step CV tailoring
│   ├── cover-note.md          <- when and how to write one
│   └── interview-prep.md      <- mock interview build
├── cv/
│   ├── README.md              <- which file is what; masters never edited per job
│   ├── Kfir_Braunstein_PM_Jerry_v2.docx <- layout base for every build
│   ├── Kfir_Braunstein_PM_Master.docx <- PM MASTER: every PM build starts here
│   ├── master-PM.md           <- master's text + reasoning + swap-in bench
│   ├── Kfir_Braunstein_CSM_Master.docx <- CSM MASTER: every CSM build starts here
│   ├── master-CSM.md          <- CSM master's text + reasoning + swap-in bench
│   ├── moved-forward/         <- CVs that got to a screen/interview (reference)
│   └── bullet-library.md      <- LOCKED canonical bullets + story selection guide. Select, don't invent
├── interview/
│   └── late-round-patterns.md <- why round 3 / final rounds were lost + fixes
├── jobs/
│   ├── tracker.md             <- one table, every job, every status (including skips)
│   ├── _template/notes.md     <- copy into each new job folder
│   └── YYYY-MM-DD Company/    <- one folder per job: notes.md (+ cover-note.txt if written)
├── tools/
│   ├── search_jobs.py         <- 24h sweep of Greenhouse / Lever / Ashby boards
│   ├── companies.txt          <- board slugs to sweep (add new companies here)
│   └── fit_check.py           <- one-page fit estimate from the draft text (run before building)
└── .claude/commands/career.md <- /career slash command: loads the three files above
```

## Git: one shared branch
- **`main` is the shared branch.** Every session starts from it and must merge its work back into it
  before ending: commit on the session's branch, then `git fetch origin main && git merge
  origin/main` (resolve conflicts), then `git push origin HEAD:main`. Kfir has approved sessions
  pushing to `main` for this repo.
- If `main` moved while you worked, merge it in first; never force-push `main`.
- `jobs/tracker.md` is the file most likely to conflict: keep every row from both sides.

## Area rules
- One fact lives in one place: `career-context.md`. If a CV and the facts file disagree, the facts
  file wins and the CV is wrong.
- Every correction Kfir makes becomes a written rule in `career-context.md` → "Corrections log".
  Same fix twice = the system failed.
- Masters in `cv/` are never edited for a single job. General improvements go into the master and
  `cv/bullet-library.md` (with a Version Log entry: date, what, why) so the next job starts better.
- Every posting vetted goes into `jobs/tracker.md`, including skips.
- Tailored CVs are Google Docs in Drive named `Kfir_Braunstein_<Track>_<Company>`; link them from
  the job's `notes.md`. **Google Docs only: never create, send or commit a PDF.** Kfir exports PDFs
  himself.

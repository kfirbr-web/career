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
│   ├── README.md              <- where the masters live (Google Drive) — never edited per job
│   └── bullet-library.md      <- LOCKED canonical bullets + story selection guide. Select, don't invent
├── jobs/
│   ├── tracker.md             <- one table, every job, every status (including skips)
│   ├── _template/notes.md     <- copy into each new job folder
│   └── YYYY-MM-DD Company/    <- one folder per job: notes.md (+ cover-note.txt if written)
└── .claude/commands/career.md <- /career slash command: loads the three files above
```

## Area rules
- One fact lives in one place: `career-context.md`. If a CV and the facts file disagree, the facts
  file wins and the CV is wrong.
- Every correction Kfir makes becomes a written rule in `career-context.md` → "Corrections log".
  Same fix twice = the system failed.
- Masters in `cv/` are never edited for a single job. General improvements go into the master and
  `cv/bullet-library.md` (with a Version Log entry: date, what, why) so the next job starts better.
- Every posting vetted goes into `jobs/tracker.md`, including skips.
- Tailored CVs are Google Docs in Drive named `Kfir_Braunstein_<Track>_<Company>`; link them from
  the job's `notes.md`.

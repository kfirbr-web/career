# Skill: find roles

**Default window: postings from the last 24 hours only.** (Kfir, 2026-09-28.) "find roles" always
means last 24h unless Kfir names another window.

## Filters (from `career-context.md` §5 and §8)
- **Seniority:** PM and Senior PM (and CSM / Senior CSM). Skip Staff, Principal, Director, VP, Head of.
- **Location:** Montreal (any setup) · Remote Canada · Remote North America. No US-only, no relocation
  to the US.
- **Tracks (all):** Product Manager / Product Owner · Customer Success · Implementation / Solutions /
  Product Specialist · Product Ops / Product and Operations · Lifecycle / onboarding.
- Auto-skip rules in `career-context.md` §5 (Quebec exclusion clauses, Toronto-only, 10+ years, hard
  domain gaps).

## How to run it
1. **Board sweep:** `python3 tools/search_jobs.py --hours 24`. It checks every slug in
   `tools/companies.txt` on Greenhouse, Lever and Ashby, and keeps postings published in the window
   that match title + location.
   - Needs network access to `boards-api.greenhouse.io`, `api.lever.co`, `api.ashbyhq.com` (and, to
     open postings, `boards.greenhouse.io`, `job-boards.greenhouse.io`, `jobs.lever.co`,
     `jobs.ashbyhq.com`). If it prints "Network blocked", say so and fall back to step 2.
   - Slugs it reports as "No board found": fix or delete them in `tools/companies.txt`.
2. **Discovery search:** web search for the target titles on `jobs.lever.co`,
   `boards.greenhouse.io`, `jobs.ashbyhq.com`, `wellfound.com`, plus Montreal/Canada terms. Web
   search can't filter by date, so a result only counts if its page shows it was posted in the
   window. **Add any new company that shows up to `tools/companies.txt`** so the next sweep covers it.
3. Open every candidate and check it's live and within the window. No proof of the date = don't show
   it as new.
4. Drop anything already in `jobs/tracker.md`.
5. Run `skills/vet-job.md` on each survivor, then show the results.
6. Add every result to the tracker, skips included.

LinkedIn / Indeed: not searched (login walls, bot blocking). Kfir pastes those in; they get vetted
the same way.

## Result format (one block per role, newest first)
```
<Company> — <Role>  |  <Apply / Stretch / Skip>   (posted <n>h ago)
Why: <blunt one-line reason>
Track: PM / CSM / Implementation / Product Ops | Pay: <range or Unknown> | Setup: <Montreal / Remote CA / Remote NA>
Company: <what they do> | Stage: <…> | Size: <~N or Unknown>
Link: <url>  (checked live <time>)
```
End with: count found, count skipped and why, and the boards that failed.

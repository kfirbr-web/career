# Skill: vet a posting (JD analysis)

Always first, for every JD. Act as a career consultant and hiring expert: say what the company
really needs, and whether Kfir is the answer. Most postings should die at the quick screen.

## Token rules (Kfir, 2026-09-28)
- Two depths. **Quick screen** for every posting; **full analysis** only for Apply / Stretch.
  A Skip gets its one-line reason and stops.
- Don't paste the JD back, don't restate `career-context.md`. Point to stories by library # and
  metrics by N# (e.g. "#8 Login, N8").
- Tables and short lines, not prose. One pass; no second summary at the end.
- Several JDs at once: quick screen all of them in one list first, then full analysis per survivor.
- Never ask something `career-context.md` already answers. Every answer Kfir gives goes into
  `career-context.md` so it is never asked twice.

## Step 1: quick screen (every posting)
1. Already in `jobs/tracker.md`? Say so and stop.
2. Open it live. Closed / reposted / aggregator-only → say so.
3. Facts (Unknown beats a guess): role, pay, location/remote, reports to, what the company does,
   stage, size.
4. **Auto-skip** (`career-context.md` §5): Quebec exclusion clause, Toronto-only, US-only,
   10+ year minimum, hard domain gap, wrong seniority (Staff / Principal / Director+).
5. **Title vs real duties:** is it really sales/quota, support-only, or project coordination?
6. **Verdict: Apply / Stretch / Skip** + one blunt line. Skip → tracker row (*Passed*), done.

## Step 2: full analysis (Apply / Stretch)

```
<Company> — <Role>  |  <Apply / Stretch>
Pay: … | Setup: … | Stage: … | Size: … | Track: PM / CSM / Impl / Product Ops

1. WHAT THEY REALLY WANT
Real role under the title: <one line>
Must-haves (ranked):  1. …  2. …  3. …  (max 5)
Nice-to-haves: …
Day-to-day: <2-3 responsibilities that will fill the week>

2. PAIN POINTS (why this seat is open)
- <pain> ← <JD evidence, a few words>   (max 3)

3. FIT: <Strong / Partial / Weak>, <one line why>

4. MATCH, GAPS, POSITIONING
| Their need | Kfir's proof (story #, N#) | Match |      <- strong / partial / gap
Gaps: <gap> → <how to frame it honestly, or "real gap, don't fake it">
Position as: <one line: the angle that answers their pain points>
Lead story: #__   Second: #__   Avoid: #__   (library Story Selection Guide)

5. TAILORING PLAN
Title line: …
Summary angle: <which true facts to put up front> (library opener: PM / CSM)
Bullets: order <#, #, #, …>; rewords needed: <bullet → which JD term>
ATS check:
| JD term | On master? | Action |      <- ✓ already there / add (true) / skip (not true)
Coverage: <x of y> key terms after tailoring
Skills block (template = master's 6 rows, cv/master-PM.md or cv/master-CSM.md):
  Lead row: <which>  | Add: <term> (row, source: facts file) | Needs Kfir: <term> | Drop: <term>

6. QUESTIONS (before any drafting)
```
Then ask with `AskUserQuestion` (buttons, max 4): only what changes the CV and isn't in
`career-context.md`: unconfirmed experience with a JD term, which of two true angles to lead
with, whether a "needs Kfir" skill is real. Never about pay, priority, or seriousness.

## Rules for the analysis
- Fit and proofs come from confirmed facts only (`career-context.md`, `cv/bullet-library.md`).
  Claim ceilings apply (e.g. AI = "prototyped"). A gap stays a gap until Kfir confirms otherwise.
- **Skills adds:** only terms in the confirmed tool stack or clearly true from a story. Anything
  else goes under "Needs Kfir". Never add Salesforce, Jira, Looker, Amplitude, Tableau, Miro,
  Mixpanel. Keep exactly 6 rows, one line each.
- No JD mirroring in the plan's wording; map JD terms to what Kfir actually did.

## After Kfir answers
1. Save answers that are new facts to `career-context.md` (and corrections to §10).
2. Tracker row (*Interested*); create `jobs/YYYY-MM-DD Company/notes.md` from the template with the
   analysis (compact).
3. Go to `skills/tailor-cv.md` with the approved plan.

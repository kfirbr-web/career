# Skill: tailor a CV

Only after `vet-job.md` gave Apply or Stretch. Be token smart: one analysis, a few sharp
questions, one draft. No repeated checklists. (Rewritten 2026-10-01 after comparing with Kfir's
parallel CV project; see `career-context.md` §10 standing rules.)

## Steps
0. **Duplicate check** (`vet-job.md` step 1) if it hasn't run this session.
1. **Decode the JD first.** One short paragraph: what the team actually builds and what the
   deciding requirement is (e.g. Vena APM = data and files, Excel, finance users, not generic APM).
   Rank the JD's asks. Then name the lead stories and the ones to leave out. The real signal picks
   the bullets; the master is only the fallback.
2. **Map every JD duty and must-have to a story** from the **whole** of `cv/bullet-library.md`
   (all numbered stories, variants, and `career-context.md` §4). List gaps. Do this before the first
   draft, silently; show the table only if it helps. Nothing in the JD's top duties may drop for
   page fit: cut a lower-signal bullet instead.
3. **Ask 3-5 gap questions** (one batch, buttons if possible) only about duties with no confirmed fact.
   For a hard domain gap, hunt for the nearest real bridge: which systems, files, artifacts or user
   groups touched that domain (Vena: CSV exports into finance teams' tools came from this).
   Never re-ask a fact already in `career-context.md`. Log each yes as a fact.
4. **Skills block:** use the 6-row template, then offer JD / ATS terms from Kfir's background
   (confirmed tools and skills only). Rows ≤ ~115 characters.
5. **Draft once, in chat:** summary + bullets + CSM + Skills. Summary and bullets follow the
   standing rules below. Run `python3 tools/fit_check.py <draft>` first (budget 29 content lines;
   26 with Projects; max 8 PM bullets).
6. **Kfir approves, then builds the file himself.** Build a Google Doc only if he says "build"
   (mechanics in `career-context.md` §9; never a PDF). Upload into `Job Search/Tailored CVs` (`parentId` = `16F0Y2gmPgvBcFb-TwpHK03nTEDIsbWna`), never the Drive root.
7. Record the final text and changes in the job's `notes.md` and the tracker "CV used". If a
   change is a general improvement, update the master and the library with a Version Log line.

## Standing rules (summary, bullets)
- **Summary** (`career-context.md` §9): company-line opener, "Promoted to the company's first
  Product Manager" plus one proof of the JD's top duty, then the 2-3 headline outcomes that fit this
  JD. Third-person, short sentences, no trait lines, no JD mirroring.
- **No metric twice on the page.** Strongest metrics in the summary; bullets use other stories.
- **Bullets:** start from the library wording and reword only for the JD signal. Structure:
  what he did → how → outcome. First bullet = the JD's top signal. No JD mirroring; plain-language
  check (would Kfir say it out loud?). No em dashes; plain hyphen in dates.
- **Proof strength** (Vena Senior review, 2026-10-01: Kfir's build beat mine on these):
  - Bullet 1 carries a hard outcome, not only the JD's wording.
  - Count distinct hard metrics on the page; aim for 6+. Prefer a story with a metric over a
    metric-less one that matches the JD's words; cover the JD wording with small edits to the metric
    bullet ("with Design", "with Sales, CS, and Marketing").
  - Give the summary the strongest metrics the bullets don't use (e.g. 33%, 18%), not reach numbers
    (12M+ residents, $2M ARR). The summary never repeats bullet 1's point.
  - Re-rank the whole library by proof strength for each JD; never start from another build.
  - Every new claim is checked against `career-context.md` before drafting; ask if it isn't there.
- **Ceilings** (`career-context.md` §3) always apply: AI "prototyped", pricing "recommended",
  no quota, no NPS/CSAT, integration tool never synced with finance/ERP systems, Fin "part of the
  team", and so on.
- **Level:** for an APM or junior role, the summary reads hands-on, not senior.
- **Never** change layout, fonts or page count.

## One pass before showing the draft
Bullet 1 has a hard outcome · 6+ distinct metrics · metrics unrepeated and not retired · ceilings respected · JD title and every must-have on the page ·
no banned words or em dashes · fit_check within budget. Fix silently; flag only what Kfir must decide.

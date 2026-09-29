# Skill: tailor a CV

Only after `vet-job.md` gave Apply or Stretch.

## Edit caps
- Title line: swap to match the posting.
- Skills: swap 3–4 terms (or pick the 6 skill lines for the track).
- Summary: **no cap, and always rewritten for the JD** (Kfir, 2026-09-29). Never ship the master
  summary unchanged. Build it for the recruiter's 6-second read:
  1. **Sentence 1 = the JD's top objective.** "Product Manager with 5 years of experience in B2B2C
     SaaS, [what this role most needs, in Kfir's words]."
  2. **A hook:** the one proof point this recruiter cares most about (a metric or a rare fit, e.g.
     payments in a regulated space, CS-to-PM, first PM). It may repeat a bullet metric (Kfir, 2026-09-29).
  3. **One line on how he works** that matches the JD's second signal.
  Keep it to 2-3 short sentences. Never repeat the company line (customer base, regions). Still bound by: facts file only, voice rules, summary metrics may repeat
  bullet metrics (up to 3), name the concrete systems built (billing, integrations, access, automation), no overlap with bullet 1's story, no JD mirroring, "5 years", B2B2C.
- Bullets: reorder by relevance; pick bullets from `cv/bullet-library.md` using its **Story
  Selection Guide** (lead / second / avoid for the role signal); reword only for JD keyword fit.
  Respect each bullet's tailoring notes (claim ceilings like "prototyped, never shipped").
- **Never** rewrite the whole CV. **Never** change layout, fonts, or page count.

## Library rules every bullet must pass
- No metric repeated across bullets (the summary may repeat up to 3 headline metrics). Each metric belongs to its own story (e.g. 30+ renewals
  stays with #2 CRM/API).
- No JD mirroring. Connect to the JD's actual signal instead of echoing its phrasing.
- Plain-language check: would Kfir say this out loud to an interviewer? No filler, no jargon, no
  hedges, no trait-style lines.
- **No em dashes** anywhere in resume text.
- The library's standard summary openers are a default, not a requirement.

## Steps
0. Run the **duplicate check** from `skills/vet-job.md` step 1 if it hasn't run this session. A
   previous build for the same job → flag it and wait for Kfir before drafting.
1. Start from the right master (`cv/README.md`) for the track.
2. **Re-derive from scratch before the first draft** `PMEM`: list every requirement line of the JD
   (including the responsibilities and the pay/team signals, e.g. quota, Sales department), then match
   each one against **every numbered story in `cv/bullet-library.md`**, not just the master's bullets
   or the Story Selection Guide row. The master and the guide are a starting point, not the answer:
   swap bullets in when the JD's real signal calls for them (e.g. a quota AM role wants #18 Sales
   support and #2's 30+ renewals over #12 and #22). Never carry framing over from a prior JD. Map the
   8–12 key terms too (or mark "no match — don't fake it"). This must shape the **first** draft;
   if "is this the best version?" surfaces a better bullet, the step ran out of order.
3. Show **only the "after"**: the full text draft (summary + all bullets + CSM section + skills) in
   chat, for one approval round, then one build. No before → after list. (Kfir, 2026-09-28)
   Before presenting, **run the self-check** against every rule in `career-context.md` and the
   library, and flag any violation yourself. `HO` Also check `PMEM`: summary doesn't overlap bullet 1's
   story; sentence structure varies across bullets (not the same "verb, gerund, outcome" rhythm); no two
   bullets could merge; every JD ATS keyword is in bullets or Skills; Figma is in the tools row.
   Keep a record of what changed from the master in the job's `notes.md`.
4. Wait for Kfir's approval. Apply only approved changes.
5. Build from **Jerry V2** as `Kfir_Braunstein_<Track>_<Company>` (layout rules: `career-context.md`
   §9). **Deliverable = a Google Doc in Drive, nothing else** (Kfir, 2026-09-29): upload the built
   `.docx` to Drive converted to a Google Doc with that name, and give Kfir the link. **Never create,
   send, upload or commit a PDF**; Kfir exports the PDF himself. For the page-fit check, render a
   throwaway preview in the scratchpad only, compare it visually with Jerry V2, flag a thin or
   overflowing page, then delete it.
6. Record the changes + Drive link in the job's `notes.md`; set tracker "CV used".
7. If any change is a general improvement, propose updating the master and
   `cv/bullet-library.md` (add a Version Log line: date, what changed, why).
8. Any correction Kfir made → new rule in `career-context.md` §10.

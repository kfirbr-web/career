# Skill: tailor a CV

Only after `vet-job.md` gave Apply or Stretch.

## Edit caps
- Title line: swap to match the posting.
- Skills: swap 3–4 terms (or pick the 6 skill lines for the track).
- Summary: **no cap, and always rewritten for the JD** (Kfir, 2026-09-29). Never ship the master
  summary unchanged. It's dense with proof, not a clean tagline. Recipe:
  1. **Sentence 1 = the JD's 2-3 core areas where Kfir has proof:** "Product Manager with 5 years of
     experience in [area, area, and area] in B2B2C SaaS." (e.g. platform systems, payments,
     integrations / billing and data integration / onboarding and lifecycle). Not a generic verb
     phrase like "owning products from discovery to launch".
  2. **Sentence 2 = 2-3 real systems he built that match those areas**, named as nouns a recruiter
     or ATS searches for (API data models, subscription and payment workflows, roles and permissions
     model, integration mapping tool, onboarding automation, engagement scoring…), from the library only.
  3. **End on 2-3 headline metrics picked for this JD, stated as end results.** The summary is
     "what it achieved"; the bullets tell the X-Y-Z story of how (what he did, how, what it produced).
     The summary may repeat bullet metrics, but a repeat must add something: never restate a bullet's
     mechanism or wording, and never open with the same story as bullet 1 (Kfir, 2026-09-30). The
     no-repeat rule applies between bullets. Retired metrics (35% retention) never.
  4. **Optional sentence 3: how he delivers**, matching the JD's second signal in concrete terms
     (e.g. "Ran Agile delivery end to end, from sprint planning to acceptance criteria"; CS-to-PM /
     first PM when client-facing work matters).
  5. **Guardrails:** "5 years", B2B2C, 3-4 lines max, facts file only, no filler or trait lines,
     no jargon ("well-governed backlog"), never repeat the company line (customer base, regions),
     no JD mirroring, no overlap with bullet 1's framing.
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
2b. **Page-level checks before showing the draft** (Kfir, 2026-09-30, Aylo):
   - The JD's job title (e.g. "Product Owner") appears on the page, in a bullet and in Skills.
   - Every JD must-have maps to a bullet or a Skills term; every fact Kfir confirmed for this JD is on the page.
   - The summary's claims hold for all 5 years (CSM + PM), not just one part of the PM role.
   - Skills: drop terms the JD doesn't need, especially ceiling-limited ones (SSO/OAuth2).
   - Length budget: summary 3-4 lines + at most 8 PM bullets; 9 bullets overflowed. Each Skills row
     at most ~115 characters including the label (longer rows wrap to 2 lines).
   - **Fit estimate before showing the draft (and before any build)** (Kfir, 2026-09-30, Meroka): save the
     full draft text in the scratchpad and run `python3 tools/fit_check.py <draft>`. Budget: 29 content
     lines (summary + bullets + project items, ~128 chars per line), 26 with a Projects section. Over
     budget → trim in the draft first and show the trimmed draft. Never find overflow by building and
     re-exporting (trial and error cost 7+ minutes on Meroka). The Drive PDF export is a single final
     confirmation, not the way to find the fit.
3. Show **only the "after"**: the full text draft (summary + all bullets + CSM section + skills) in
   chat, for one approval round, then one build. No before → after list. (Kfir, 2026-09-28)
   Before presenting, **run the self-check** against every rule in `career-context.md` and the
   library, and flag any violation yourself. `HO` Also check `PMEM`: summary doesn't overlap bullet 1's
   story; sentence structure varies across bullets (not the same "verb, gerund, outcome" rhythm); no two
   bullets could merge; every JD ATS keyword is in bullets or Skills; Figma is in the tools row.
   Keep a record of what changed from the master in the job's `notes.md`.
4. Wait for Kfir's approval. Apply only approved changes.
5. **Build mechanics that work here** (2026-09-30): build the .docx by editing the latest job .docx
   of the same layout (e.g. the Sadie build) in the scratchpad; LibreOffice can't open files in this
   container, so check page fit by exporting the uploaded Doc as PDF through Drive and counting pages
   (throwaway, scratchpad only). Drive can't replace a Doc's content: upload the new version, confirm
   one page, then trash the old Doc and update the link in `notes.md`.
   Build from **Jerry V2** as `Kfir_Braunstein_<Track>_<Company>` (layout rules: `career-context.md`
   §9). **Deliverable = a Google Doc in Drive, nothing else** (Kfir, 2026-09-29): upload the built
   `.docx` to Drive converted to a Google Doc with that name, and give Kfir the link. **Never create,
   send, upload or commit a PDF**; Kfir exports the PDF himself. For the page-fit check, render a
   throwaway preview in the scratchpad only, compare it visually with Jerry V2, flag a thin or
   overflowing page, then delete it.
6. Record the changes + Drive link in the job's `notes.md`; set tracker "CV used".
7. If any change is a general improvement, propose updating the master and
   `cv/bullet-library.md` (add a Version Log line: date, what changed, why).
8. Any correction Kfir made → new rule in `career-context.md` §10.

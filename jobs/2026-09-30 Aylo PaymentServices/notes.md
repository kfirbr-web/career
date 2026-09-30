# Aylo — Product Owner, Payment Services (payouts / remittance)

## Posting
- **Link:** https://www.linkedin.com/jobs/view/4464635660/ (sent by Kfir, live per Kfir). Also on Greenhouse: https://job-boards.greenhouse.io/aylo/jobs/8737531002
- **Checked live on:** 2026-09-30: open (Greenhouse checked; LinkedIn confirmed by Kfir)
- **Source:** Pasted (JD) + Greenhouse
- **Location / remote:** Montréal, QC; hybrid (JD: "a select number of positions require full-time in office attendance"; which applies here is Unknown)
- **Pay range (if posted):** Unknown (not posted)
- **Reports to:** Unknown ("project priorities provided by management")
- **Language:** no French requirement in the JD; application form is bilingual

## Company
- **What they do:** Adult entertainment and games platforms (est. 2004). Payment Services team, payouts/remittance: fintech services with internal and external clients and integrators.
- **Stage / funding:** Private; Unknown
- **Employees (approx):** Unknown
- **Earlier application:** Kfir applied to Aylo before for a different role (2026-07-06, Search & Recommendation PM, recruiter screen per tracker). Not a repeat.

## Verdict
**Apply**: Product Owner is a target title, and the duties (Scrum ceremonies, user stories and acceptance criteria, troubleshooting and testing, investigating issues with Engineering, integrations) are what Kfir did as sole PM. Payments work at Bewith (subscriptions and multi-entry payments, Stripe sync and reconciliation, refunds on public funds) is the adjacent domain.
- Title vs real duties check: real PO work. Not sales, not project coordination.
- Fit: ran Scrum himself (sprint planning, grooming, retros, acceptance criteria); Stripe webhook / sync / reconciliation investigations with SQL; manual refunds decision (phased: manual first, automated later); QA in staging (Jam.dev); integrations with client systems and providers (Postman); API docs; engagement scoring (reporting).
- Gaps / stretches: payouts: confirmed 2026-09-30 (payment solution end to end with client finance teams, payouts via Stripe Connect); remittance at Aylo's scale is still new; no banking (fintech adjacency only); no Scrum/PO certification; Jira never used (never add; ClickUp instead); business cases: "short, high-level" label only, never cost/ROI models.

## Key terms (8–12)
1. Payments / fintech (summary, #1, #14, #17, Payments row)
2. Payouts / remittance (Stripe Connect payouts bullet, summary, Payments row)
3. Scrum / sprint goals / scrum meetings (summary, Agile row)
4. User stories / acceptance criteria (summary, Agile row)
5. Investigation with Engineering / troubleshooting (#14, Quality row)
6. Testing / QA (QA bullet, Quality row)
7. Integrators / end-to-end integration flows (#13, liaison + API docs bullet, API row)
8. Technical to non-technical communication (liaison + API docs bullet)
9. Documentation (API docs bullet, Technical Documentation, Release Notes)
10. Analytics and reporting (#6, Analytics row)
11. Feature phases (#17 manual → automated; staged releases)
12. Jira (no match: never used; don't add)

## CV
- **Track / base:** PM master (`cv/master-PM.md`)
- **Tailored copy:** [Kfir_Braunstein_PM_Aylo](https://docs.google.com/document/d/1iuLzbhSOOA7AUprPZ0i_kShj4lMheqy49gvZhJXY4-A/edit)
  (Google Doc; source .docx in this folder, built on the Sadie build of the Jerry V2 layout). One page in Google's PDF export.
- **Changes from the master (draft v1):**
  - Summary: rewritten for payments + integrations + Scrum delivery.
  - Bullets: #1, #14 Stripe investigation (new in), #17 refunds (new in), QA + staged release (Sadie wording), #13 integration tool (new in), liaison + API docs (#7 without QBRs + #23), #6, #2. Dropped: #5 onboarding, #4 permissions, #3 mobile, #8 login.
  - v2 (Kfir, 2026-09-30): new Stripe Connect payouts bullet (2nd); #2 CRM/API dropped for space; summary names payouts; Agile added to the Agile row.
  - v3 (Kfir, 2026-09-30, from his other CV project's review): summary replaced with Kfir's text (product + CS roles opener, company line, 12M+ residents; PO sentence; payment products on Stripe). Bullets: payouts (+ internal finance-team reporting requirements), #14, #1, #17, new PO bullet, QA (+ test cases, UAT), #13, technical contact (+ feature requests into scoped requirements). #6 (18%) cut for page fit (2 pages with it). Skills: Agile row = Product Owner, Scrum, Sprint Goals, User Stories, Use Cases, Acceptance Criteria, Business Cases (Agile / Sprint Planning dropped to keep one line; both in the PO bullet or label); Quality row + Test Cases, UAT (Documentation dropped for length); SSO/OAuth2 out; degree line em dash fixed. Old Docs (v2, 2-page v3) moved to Drive trash.
  - Kfir's review of v2 (logged as rules): summary overstated the 5 years; no PO bullet or "Product Owner" on the page; confirmed facts missing; SSO/OAuth2 irrelevant.
  - Skills (v1/v2): Agile & Delivery leads; new Payments row; Quality & Release row; Analytics & Reporting; AI row and Product Strategy row out (Prioritization, Roadmapping folded into Agile; Claude Code into Tools); Linear, Loveable out.

## Cover note
None

## Interview prep
- Stages / people: Unknown
- Stories to use: Stripe sync investigations; manual refunds (risk, audit trail, phase 2 automation); subscriptions (surface request vs real need); integration mapping (non-technical clients, first API); notification redesign (bring Eng in during spec).
- Likely hardest question: "You haven't worked on payouts. How would you get up to speed on remittance flows?"
- Questions to ask them: who the internal clients of the payouts team are; how sprint priorities come down from management

## Log
| Date | What happened |
|---|---|
| 2026-09-30 | Vetted: Apply. Draft v1 sent for approval |
| 2026-09-30 | Kfir confirmed Stripe Connect payouts + ceremonies; draft v2 sent |
| 2026-09-30 | Kfir approved v2; built PM_Aylo (Google Doc, one page) |
| 2026-09-30 | v3 from Kfir's review built (one page); #6 cut for fit |

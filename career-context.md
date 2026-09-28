# Career context — the facts file

Single source of truth. Every CV line, cover note, and interview answer must trace back here.

**Legend:** **[TODO]** = Kfir needs to supply it. **[CONFLICT]** = two sources disagree; Kfir decides.
**Sources merged (newest wins unless marked CONFLICT):**
`BL` = `cv/bullet-library.md` (2026-09-28) · `HO` = Drive *Kfir_Session_Handoff_v10* (2026-07-02) ·
`SB` = Drive *Master_Story_Bank* (2026-07-16) · `STAR` = Drive *Screening_Prep_Full_STAR_Answers*
(2026-07-06) · `CV` = tailored CVs in Drive (Sep 2026).

---

## 1. Who I am

- **Name:** Kfir Braunstein
- **Location:** Montreal, QC, Canada
- **Header on CV:** Montreal, QC, Canada | 514-462-2234 (the only phone to use; 431-294-5256 is old) | kfirbr@gmail.com | LinkedIn (always a hyperlink
  with display text "LinkedIn"; never a raw URL, never omitted) `HO`
- **Work setup:** open to remote, hybrid, or on-site. **No relocation to the US.** (Kfir, 2026-09-28)
- **Work authorization:** [TODO] Canada status (only needed for form questions)
- **Languages:** English – Fluent | Hebrew – Native | French – A2 (always "A2"; never A1 or
  Beginner) `HO`
- **Years:** always "5 years" `HO`
- **Bewith.io:** always **B2B2C** (never B2B); descriptor always "North America and Europe" (never
  include Israel) `HO`
- **CV length:** 1 page `HO`

### Voice rules
- Plain facts, no adjectives. Say what was done and what changed. `BL`
- Bullet structure: decision/action → how it was done → concrete outcome. Never lead with artifacts,
  tools, or process language. `HO`
- Start from what Kfir actually did → what it produced → does it connect to the JD signal. Never
  start from JD language. `HO`
- Plain-language check: would Kfir say this out loud to an interviewer? `BL`
- No filler ("evaluating tradeoffs across scope and timeline," "scalable workflows"), no jargon
  ("discovery synthesis," "testable concept"), no hedges ("where possible"), no trait-style lines. `BL`
- No JD mirroring. `BL` `HO`
- Short, declarative sentences; one idea per clause; no run-ons. `HO`
- "Prototyping independently" reads junior; say "reduced engineering dependency" or "validated ideas
  fast." `HO`
- **No em dashes** anywhere in resume text (only allowed in the B.Arch degree line). `HO` `BL`

### Banned words / openers
- leveraged, spearheaded, passionate, results-driven `Jerry note` [TODO: confirm you want these]
- "Identified an unmet need for…" / "Identified an opportunity to…" `HO`
- "orchestrating" (as a description of what PMs do) `SB`
- [TODO] add yours

---

## 2. Career path

| Dates | Role | Company | One line |
|---|---|---|---|
| Nov 2021 - Oct 2025 (never Oct 2021) | Product Manager | Bewith.io (B2B2C SaaS, 100+ municipalities and organizations, North America and Europe) | Sole PM for the full platform; tripod with Design and Engineering; planning sessions with the CPO |
| Feb 2021 - Oct 2021 | Customer Success Manager | Bewith.io | ~$2M ARR portfolio; promoted to the company's first PM in under a year |
| Dec 2018 - Dec 2019 (never Dec 2020) | Project Manager and Content Developer | Peres Center for Peace and Innovation (non-profit) | Multi-year lecture program, full P&L |
| 2015 - 2019 | B.Arch. | Bezalel Academy of Arts and Design, Jerusalem | |

- **Title rule:** always "Product Manager." "Product and Operations Manager" only for ops-facing roles
  when explicitly confirmed. `HO`
- **The story (one line):** "I've done this job from both sides: as a CSM translating customer pain
  into product feedback, and as a PM receiving that feedback and deciding what to build." `HO` (Solink)
- **Side projects** (separate Projects section, never folded into Bewith bullets) `HO`:
  - X/Twitter Bookmark Organizer Chrome extension, built with Claude Code
  - Job search tracking tool, built with Claude Code, Supabase, and Git
- **Gap since Oct 2025:** studied French full-time for 6 months, Jan 2026 - Jul 2026 (now A2);
  built the side projects above; job search. (Kfir, 2026-09-28)
- **Why I left Bewith:** [TODO]
- **Peres Center → Bewith gap (Dec 2019 - Feb 2021):** not relevant (Kfir); don't raise it.

---

## 3. Verified numbers

Locked in `BL`. Each metric belongs to **one story only** and appears **at most once per resume**. `HO` `BL`

| # | Claim | Owner story (BL #) | Notes |
|---|---|---|---|
| N1 | ~$2M ARR in client contracts owned as CSM | CSM | **Summary only** `BL` |
| N2 | 100%+ contract expansion into new departments | #4 Permissions | |
| N3 | $100K+ incremental ARR | #1 Subscriptions | Interview detail: **3 new clients, 4 major expansions** `SB` |
| N4 | 30+ contract renewals | #2 CRM/API | **[CONFLICT]** see below |
| N5 | 18% QoQ usage growth | #6 Engagement scoring | **[CONFLICT]** see below |
| N6 | $55K+ new revenue | #3 Mobile apps | |
| N7 | Onboarding −33% (9 → 6 days) | #5 Onboarding | **[CONFLICT]** see below |
| N8 | Login conversion 40% → 85%; related tickets −90%; zero engineering | #8 Login | |
| N9 | Eng integration effort days → hours | #13 Integration tool | |
| N10 | Time to first event: tens of minutes → a few minutes | #9 Event form | |
| N11 | CSM: ARR +20%, 4 entry-level clients upgraded to enterprise | CSM | |
| N12 | CSM: 100% retention across 30+ accounts | CSM | |
| N13 | 12M+ residents engaged (public stat); 100+ municipalities and organizations | Summary | Say "residents engaged," never "active users" `HO` |
| N14 | Promoted CSM → PM in under a year | CSM italic line | |
| N15 | CS scaled to 100+ accounts with no added headcount (HubSpot CS ops layer) | Interview only | `SB` `STAR` **[CONFLICT]** see below |

### Metric conflicts to resolve
1. **35% retention** is retired in `BL` and `HO`, but `SB` and `STAR` still give it as the result of
   the CRM/API data model story. The interview version should say "supported 30+ contract renewals."
   → Confirm, and I'll fix those two Drive docs' wording in this repo's story index.
2. **18% QoQ usage growth:** `BL` credits it to engagement scoring (#6); `SB` and `STAR` credit it to
   self-serve configuration workflows. Which one is true?
3. **33% onboarding:** `BL` credits the onboarding workflows (#5); `SB` credits the integration
   mapping system. `SB` also notes an older "weeks to hours" version. Which one is true?
4. **100+ accounts, no added headcount:** CSM bullet says 30+ accounts. Is "100+ accounts" the whole
   company's CS book? OK to use?

### Never claim (claim ceilings)
- **Retired:** 35% retention. Never use. `HO` `BL`
- **AI features (#11):** ceiling is "prototyped," never "shipped" (`BL` raised it from "proposed" on
  2026-09-28). No post-prototype outcome; don't claim human-in-the-loop requirements.
- **Pricing:** recommended only; never "set" or "owned." `BL`
- **Monolith → microservices:** advised the CPO and CTO on product impact; they led. `BL`
- **Renewal negotiations:** supported only, never led. `BL`
- **Engagement scoring:** internal dashboard Engineering built to Kfir's spec (login frequency,
  frontend/backend usage, events created per client). Not a BI tool. `BL` `HO`
- **SQL:** some queries himself, some run by engineers (`BL`). `HO` said "read/analysis only; does
  NOT write SQL independently." → Newest (`BL`) wins unless you say otherwise.
- **QBR / roadmap audience:** "client leadership," not "C-level," unless confirmed client-facing. `BL`
  (`HO` lists "delivered C-level roadmap presentations"; `BL` is stricter and newer.)
- **SSO / OAuth2 / OIDC:** product requirements level only, not auth architecture. `HO`
- **Mobile:** Flutter, cross-platform (iOS + Android), not native. Dedicated squad through the whole
  PM tenure. `HO`
- **Intercom Fin:** configured and deployed; supporting signal only, never core work. `HO`
- **Multi-region (#16):** assigned clients to EU/US regions and configured subdomains; did not design
  the architecture. `BL`
- **Vendors (#15):** no concrete negotiation outcome. `BL`
- **Tools never to add:** Salesforce, Jira, Looker, Amplitude, Tableau, Miro, Mixpanel. `HO`
- No invented numbers; no "hours saved" or "% efficiency" without a source.

### Confirmed tool stack `HO`
| Category | Tools |
|---|---|
| PM & Collaboration | ClickUp, Confluence, Linear, Figma, Figma Make |
| Engineering / Technical | Postman, SQL, Webhooks, Chrome Extension Dev, Prompt Engineering, SSO/OAuth2/OIDC (requirements level) |
| Customer & Support | Intercom (incl. Fin), HubSpot, Jam.dev |
| Analytics | Google Analytics, SQL |
| Payments | Stripe |
| AI / Builder | Claude Code, Claude Cowork, ChatGPT |
| Data / Automation | Airtable |
| Design | AutoCAD (architecture background) |
| Testing | A/B Testing (confirmed by Kfir 2026-09-28) |

`CV` also uses Monday, Slack, Loveable. [TODO: confirm these are OK]

---

## 4. Stories

- **Bullet wording** and which story leads for each role type: `cv/bullet-library.md`.
- **Full STAR answers:** Drive *Master_Story_Bank* (source of truth for interview telling) and
  *Screening_Prep_Full_STAR_Answers*.

### Story index (for picking fast)
| Question it answers | Story | Proof |
|---|---|---|
| Greatest achievement / discovery beats the surface request | Subscriptions: "recurring payments" request → entitlements + access-control rebuild | $100K+ ARR, 3 new clients, 4 expansions |
| How do you validate before building? | Registered on a competitor's platform; found a full entitlement system under "simple subscriptions" | Reshaped the subscriptions scope |
| Cross-functional misalignment | Sales (speed) vs CS (ops complexity) vs Eng (scalability) on subscriptions → explicit guardrails | Shipped a scope everyone backed |
| Risk vs regulation vs speed | Manual, admin-approved refunds first | On time, no compliance blockers |
| Structural fix that unblocked growth | Permissions rebuild for nested departments | 100%+ expansion |
| 0-to-1 | Mobile apps (resident + staff scanner, Flutter) | $55K+ |
| Data-driven decision | Login flow fix | 40% → 85%, tickets −90% |
| Behavioral signal, not a request | Clients copy-pasting event content from outside docs → form redesign | Tens of minutes → a few minutes |
| Pushback on a senior stakeholder (honest partial win) | Naming convention overhaul; CTO pushed back; shipped lowest-risk part + terminology guide + labels side project | Partial win |
| Mistake #1 | Overbuilt V1 (scoped too many cases before validating) → smaller releases after | Process change |
| Mistake #2 | Messaging spec sent to build without CTO/Eng review → rework + review checkpoint | **[TODO] confirm details** (`SB` says reconstructed) |
| One decision, three audiences | Calendar widget vs family-user structure | **[TODO] confirm details** (`SB` says reconstructed) |
| Meetings that decide things | Roadmap review rebuilt around trade-off templates | Fewer last-minute surprises |
| Built something teams adopted without a mandate | Internal ClickUp system | Single source of truth |
| Scale ops without headcount | HubSpot CS ops layer (lifecycle automation, triggers, escalation, renewal alerts) | N15 (see conflict 4) |
| "What is PM to you?" | US launch: Sales promised any integration; API not ready → embeddable JS widget as a bridge | Launched on time, kept contracts |
| How do you use AI? | Claude Code for PRDs / user stories / prototypes; Figma Make mockups; job-search app built solo | Specifics on 3 tools |
| Implementation / white-label | Owned per-client pre-configuration: API settings, data mapping, integrations with city IT (CivicPlus, Granicus, CivicRec) | Templated the mapping |

### Story rules
- Balance "we" and "me": every story needs an explicit "I decided / I noticed / I built" moment. `STAR`
- Keep the naming-overhaul and overbuilt-V1 stories honest and imperfect; a too-clean story reads as
  rehearsed. `SB`

---

## 5. Target roles

Pulled from ~40 builds in `HO` and Drive. [TODO] rank these and confirm seniority.

1. **Product Manager**: B2B / B2B2C SaaS, platform, payments, 0-to-1, AI PM, mobile PM, Product Owner
2. **Customer Success Manager**: mid-market / enterprise SaaS, onboarding-heavy
3. **Product / Implementation / Solutions**: implementation manager, product specialist,
   forward-deployed (Nesto, Solink)
4. **Product Ops / GTM / Program**: "Product and Operations Manager" title (Autodesk, Axon, Samsara)
5. **Lifecycle / digital CS** (1Password)

- **Seniority:** Associate PM up to Senior PM seen in builds. [TODO] where do you want to aim?
- **Applies widely:** Kfir applies to dozens of roles a day. **Never ask about role priority or how
  serious an application is.** `HO`

### Not interested / auto-skip (from `HO` skipped roles)
- Hard domain requirements with no analog: telecom, railroad, robotics, on-premises hardware,
  data engineering, design systems + localization + RLHF, Adobe Target/AEP/CDP specialist
- Location blockers: must be Toronto-based; US-only postings; Quebec exclusion clauses
- 10+ years minimum experience
- Non-profit ops / HR / finance ops roles
- [TODO] anything else (e.g. quota-carrying roles under a CS title?)

---

## 6. Pay

**Deferred:** not relevant at this stage (Kfir, 2026-09-28). If a form forces a number, ask Kfir.

- **Target range (CAD, base):** [TODO] PM: ___  CSM: ___
- **USD for US-remote roles:** [TODO]
- **Walk-away floor:** [TODO] (never said out loud)
- **Sentence for recruiters/forms:** [TODO]
- Contract roles: ask how the contract is structured and whether benefits are included before
  naming a rate. `STAR`

---

## 7. Ready answers

- **Tell me about yourself (60-90s)** (base, adapt per role): "I'm a Product Manager with 5 years at
  Bewith.io, a B2B2C SaaS platform serving 100+ municipalities across North America and Europe. I
  started in Customer Success and was promoted within a year into the company's first Product
  Manager role. [Two or three proof points matched to the role.] That's why this role caught my eye."
  `STAR` (Fixed: the STAR version says "North America, Europe, and Israel," which breaks the no-Israel rule.)
- **What makes you stand out (short):** "I was an architecture graduate before becoming a PM. That
  background shaped how I structure complexity, the same skill I use to turn messy operations into
  clean system logic, fast, in domains I've never worked in before." `HO`
- **Both sides:** CSM + PM "from both sides" answer, see §2 story line. `HO`
- **What is PM to you?** US launch widget story, see §4. `SB`
- **How do you use AI?** see §4. `SB`
- **Domain I haven't worked in:** "Municipal operations were new to me too, and every city worked
  differently, so I learned that domain fast." `HO` (Nesto)
- **Past application answers to reuse:** Nesto (implementation experience, why Nesto, standout) and
  Solink (standout, best person, why Solink) in Drive *Kfir_Session_Handoff_v10*.
- **What have you done since Oct 2025?** "I took six months to study French full-time, since I'm
  building my career in Montreal, and used the time to build a couple of tools with Claude Code."
  [draft; confirm wording]
- **Why are you looking?** [TODO] (depends on why you left Bewith)
- **Pay expectations:** see §6. [TODO]
- **Relocation:** open within Canada / remote; not relocating to the US.

### Questions to ask them `SB`
- Recruiter: why is the role open; what separates candidates who move forward; team structure and
  reporting line; timeline and next round.
- Hiring manager: biggest challenge this role solves; first 90 days; how success is measured; where
  the current process breaks down.
- Pick 2, not 5: one logistics question, one that shows you listened.

---

## 8. Search terms

[TODO] confirm / add
- "Product Manager" B2B SaaS, Montreal / Remote Canada
- "Product Manager" payments / platform / GovTech / civic tech
- "Technical Product Manager" integrations / API
- "Product Owner" SaaS Montreal
- "Implementation Manager" / "Product Specialist" SaaS
- "Product Operations" / "Product and Operations Manager"
- "Customer Success Manager" SaaS, Remote Canada

Location filters: [TODO] Montreal, Remote-Canada, Remote-North America?

---

## 9. CV setup `HO` `BL`

**Layout base:** `cv/Kfir_Braunstein_PM_Jerry_v2.docx` (Calibri, 1cm margins confirmed).
**Content base:** `cv/Kfir_Braunstein_PM_Master.docx` (text in `cv/master-PM.md`), built from the CVs
that moved forward.

**Layout (never changes):**
- Calibri throughout. Body 10pt, name 16pt. Margins 1cm on all sides.
- Right-aligned dates on a tab stop at 11106 twips.
- Company line separate from role line: **Bewith.io** | B2B2C SaaS… then **Product Manager** [TAB] dates.
- No repeated company header for the CSM role.
- *Promoted to Product Manager in under a year based on performance.* Italic, no bold; the only italic line.
- No inline bold labels in bullets.
- No "Summary" header.
- Skills block: exactly 6 rows, one line each. CS roles lead with Customer Success & Ops; PM roles
  lead with AI & Builder Tools or Product Strategy depending on the JD.
- Projects section (side projects) only when it fits the role.
- After building: rasterize the PDF and compare it visually against Jerry V2; flag a thin-looking page.

**Summary:** uses the library's standard openers; includes metrics; not generic; third-person resume
voice; doesn't repeat bullet 1; short sentences; no JD mirroring.
**Bullets:** first bullet hits the JD's top signal with a hard outcome. 5-8 PM bullets to fit one page.
**CSM section:** locked 3 bullets + promoted line. **Peres Center:** locked 2 bullets.

**Date format:** plain hyphen: `Nov 2021 - Oct 2025` (as in the PM master).

**File naming:** `Kfir_Braunstein_<Track>_<Company>` (e.g. `_PM_`, `_CSM_`, `_ProductOps_`, `_PMO_`).

---

## 10. Corrections log

Every fix Kfir makes becomes a rule here. Newest on top.

| Date | Rule | Source |
|---|---|---|
| 2026-09-28 | Plain-language pass on every bullet; AI-sounding phrasing is out | `BL` |
| 2026-09-28 | AI features ceiling raised from "proposed" to "prototyped" | `BL` |
| 2026-09-28 | Engagement scoring: "Defined… that Engineering built" | `BL` |
| 2026-09-28 | Phone is 514-462-2234; Peres ends Dec 2019; A/B Testing confirmed; "company's first Product Manager" OK | Kfir |
| 2026-09-28 | Pay is deferred at this stage; don't ask about it | Kfir |
| 2026-09-28 | No relocation to the US | Kfir |
| 2026-07-02 | Never include Israel in the Bewith.io descriptor | `HO` |
| 2026-07-02 | Never ask about role priority or seriousness | `HO` |
| ≤2026-07 | 35% retention permanently retired | `HO` |
| ≤2026-07 | French is always "A2" | `HO` |

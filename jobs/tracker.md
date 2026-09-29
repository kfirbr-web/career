# Job tracker

One row per posting, including skips. Newest on top.

**Statuses:** Sweep lead → Interested → Applied → Screen → Interview → Offer / Rejected / Withdrawn / Passed
**Verdicts:** Apply / Stretch / Skip
The agent sets up to *Interested*; Kfir moves it to *Applied* and beyond.

Backfilled 2026-09-28 from Drive (tailored CVs, prep docs) and *Kfir_Session_Handoff_v10*.
`?` = unknown; Kfir to fill in. Dates are the CV build date, not necessarily the application date.

## Active / recent

| Date | Company | Role | Verdict | CV used | Status | Next step | Folder |
|---|---|---|---|---|---|---|---|
| 2026-09-29 | Wawanesa Mutual Insurance | PM, Business Insurance (location Unknown; likely Quebec) | Stretch | PM_Wawanesa (draft) | Interested | Kfir approves CV draft | `2026-09-29 Wawanesa/` |
| 2026-09-28 | Akur8 | Account Manager (Montréal, hybrid; quota, OTE CA$170-190K) | Stretch | AM_Akur8 | Interested | Kfir reviews CV and applies | `2026-09-28 Akur8/` |
| 2026-09-28 | Unnamed food & consumer products co. (via recruiting agency) | Customer Success Representative (Montreal) | Apply (down-level) | CSM_FoodCPG | Interested | Kfir applies; ask the agency for the client name | `2026-09-28 FoodCPG CSR/` |
| 2026-09-28 | PIP Canada (Protective Industrial Products) | PM, First Aid and Footwear (Laval, QC) | Skip | — | Passed | — | — |
| 2026-09-28 | Insurity | Senior CSM, Decisions Suite (Remote - Canada) | Stretch | CSM_Insurity | Interested | Kfir reviews CV and applies (Canada posting) | `2026-09-28 Insurity/` |
| 2026-09-28 | BDC | PM, AI-Native Incubator | Stretch | PM_BDC | Interested | Kfir reviews CV + cover note, applies; send posting link | `2026-09-28 BDC/` |
| 2026-09-28 | Monks | ? PM | Apply | PM_Monks | ? | ? | `2026-09-28 Monks/` |
| 2026-09-25 | Karbon | ? CSM | Apply | CSM_Karbon | ? | ? | `2026-09-25 Karbon/` |
| 2026-09-25 | GC AI | ? CSM | Apply | CSM_GCAI | ? | ? | `2026-09-25 GCAI/` |
| 2026-09-25 | Fortra | ? PM + CSM (two roles?) | Apply | PM_Fortra / CSM_Fortra | ? | ? | `2026-09-25 Fortra/` |
| 2026-09-24 | 1Password | ? lifecycle / onboarding | Apply | Kfir_Braunstein_1Password | ? | ? | `2026-09-24 1Password/` |
| 2026-09-24 | Vention | ? PM (internal tools); a different role from the skipped Robotics PM | Apply | PM_Vention | ? | ? | `2026-09-24 Vention/` |
| 2026-09-24 | Monarch | ? PM | Apply | PM_Monarch | ? | ? | — |
| 2026-09-24 | Sherweb | ? PM | Apply | PM_Sherweb | ? | ? | — |
| ≤2026-09-28 | Cohere | ? | Apply | ? | ? | ? | — |
| 2026-08-27 | Samsara | Product Ops | Apply | ProductOps_Samsara | ? | ? | — |
| 2026-08-05 | Lightspeed | ? | Apply | PM_Lightspeed (moved forward) | Rejected: round 3 | — | — |
| 2026-07-23 | GoTo | ? | Apply | PM_GoTo (moved forward) | Rejected: final round | — | — |
| 2026-07-06 | Autodesk | Operations Manager, Platform Product Teams | Apply | PMO_Autodesk | Screen (recruiter) | ? | — |
| 2026-07-06 | RBC | PM/BA hybrid, Capital Markets (QTS/RAMPP), contract | Apply | ? | Screen | ? | — |
| 2026-07-06 | ? (adult platform) | Search & Recommendation PM | Apply | ? | Screen (recruiter) | ? | — |
| 2026-06-16 | Botpress | ? | Apply | PM_Botpress (moved forward) | Rejected: final round | — | — |
| ≤2026-07 | Wealthsimple | ? | Apply | ? | Interview? (prep referenced) | ? | — |

## Built in handoff v10 session (2026-07-01)

| Company | Role | CV used | Status |
|---|---|---|---|
| First Advantage | PO | PM_FirstAdvantage | ? |
| EPAM | Mobile PM | PM_EPAM | ? |
| Axon | GTM Program Manager | PM_Axon (Product and Operations Manager title) | ? |
| Narvar | Associate PM | PM_Narvar | ? |
| Nesto | Product Implementation Manager | PM_Nesto | ? |
| Trulioo | PM, KYB | PM_Trulioo | ? |
| Lyft | Enterprise Software PM | PM_Lyft | Rejected: round 3 |
| MaintainX | Senior PM | PM_MaintainX | ? |
| oolu | PM | PM_oolu | ? |
| Samsara | Senior PM | PM_Samsara | ? |
| Solink | Product Specialist | PM_Solink (Product and Operations Manager title) | ? |

Older builds referenced (status ?): HR4 (2026-05), Ciena (2026-04), SpryPoint, Optable, Affinity,
Structure Studios, FutureFit (CS Ops).

## Skipped (don't rebuild without new information) `HO`

| Company | Role | Reason |
|---|---|---|
| PIP Canada | PM, First Aid and Footwear | Physical-goods category PM (sourcing, SKUs, inventory, Health Canada/FDA product compliance); no SaaS analog |
| National Bank | Governance PO | Data/analytics domain gap |
| CN Rail | Telecom PM | Hard telecom requirement |
| CN Rail | Enterprise PM | 10-year minimum, railroad domain |
| Dropbox | GTM AI | Geography + domain gap |
| Vention | Robotics PM | Too technical, robotics domain |
| ProShop | Product Ops | Quebec exclusion clause |
| Chainalysis | Data PM | Data engineering domain gap |
| Zaya Care | Product & BizOps | Toronto-based requirement |
| GoDaddy | UX Platform PM | Design systems + localization + RLHF gaps |
| Entrust | IFI PM | On-prem hardware, US-only |
| Bounteous | Personalization Manager | Adobe Target/AEP/CDP specialist, wrong stack |
| Canada Plastics Pact | Sr Operations Manager | HR/finance/sustainability, non-profit ops |

## Pending manual fixes on old CVs (carried from `HO`)
- SpryPoint v7: summary says "B2B SaaS"; should be "B2B2C"
- Optable: summary says "B2B SaaS platform delivery"; should be "B2B2C"
- Affinity: AI bullet says "shipped"; should be "prototyped" (current ceiling)
- Structure Studios: replace the summary (the new text is in the handoff doc)
- GoTo: bullet 5 (AI tools) needs a rewrite
- FutureFit CS Ops: confirm the "Support & Success" framing in the Jam.dev bullet

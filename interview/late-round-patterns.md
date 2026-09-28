# Late-round patterns

You reached round 3 or the final round at Botpress, GoTo, Lyft and Lightspeed and lost all four. The
CVs are working; this file is about what happens after them.
Sources: Drive *Mock_Debrief_Round2* (GoTo), *Lightspeed_Mock_Round_Debrief*, *PM_Interview_Mock_Log*
(18 mocks), *PM_Interview_Win_Sheet*, *Botpress home assignment - Kfir*.

## The patterns that show up in more than one place

1. **The first answer skips the mechanism.** You name the right story, then jump to the result. The
   specific thing you said, saw or decided only comes out after a follow-up. (Lightspeed R1 + R2,
   GoTo.) Fix: **start with the concrete moment**, e.g. "the risk I laid out to Sales was X."
2. **You get there, but only after 2-3 follow-ups.** GoTo AI-quality question: 3 follow-ups.
   Lightspeed churn-metric question: validating against real churn only came on the 3rd push. Final
   rounds give you about one follow-up. Fix: answer the follow-up before it's asked.
3. **Metrics are the weakest stage.** Guardrail vs. proxy was confused in **5+ mocks**. You default
   to adoption numbers when asked about quality or value (GoTo named this directly). Metrics are
   "reached once, still rough" in the win sheet. Fix: every metrics answer names **the tempting
   metric → why it's wrong → the real metric → a guardrail that could get worse while it goes up**.
4. **Story-to-question fit.** A strong story aimed at the wrong angle, e.g. discovery told for a
   "messy data" question (Lightspeed). Fix: same story, entered from the angle the question asks.
5. **Delivery.** Windups that restate the question; stutters at transitions; locked numbers slipping
   under pressure ("thirty percent" for 33%, "Cleveland" for Portland).
6. **Product sense (Lyft round type):** "one lever, three costumes"; the company-asset check isn't
   self-started; missions start from the feature. Cases never drilled: monetization, competitive
   defense, strategy framing, and a mid-interview twist.

## Home assignment (Botpress): what to check next time
The submission picked a clear direction (monetize Active Free Riders) and had a spec + a new
activation definition. Things a final-round panel would likely push on:
- **Impact has no numbers.** The scoring table left `[X%]`, `[$Y]`, `[Z pp]` as placeholders.
  Even rough, stated assumptions ("if 5% of the 35% convert at $X ARPU…") beat blanks.
- **Monetization by restriction** (a 3-form cap) with churn as the only guardrail. Expect "what
  stops these users leaving for a competitor?" Have a softer alternative (value-based gate) ready.
- **The other cohort got dismissed as "structurally small"** without data. Name the cheap test that
  would check it.

[TODO] Tell me what you remember of the GoTo and Lyft/Lightspeed round 3 feedback, if any came back.

## What prep should do before every late round
- Run a mock built from the JD using `skills/interview-prep.md`, graded against the patterns above.
- Drill the metrics sequence (pattern 3) out loud on 3 of your own stories.
- For home assignments: numbers in every impact cell, one guardrail per risk, one cheap test per
  assumption.

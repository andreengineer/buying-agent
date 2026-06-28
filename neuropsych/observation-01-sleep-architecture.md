# Observation 01 — Sleep Architecture & Temporal Task Allocation
## Session 1/6 — Raw Behavioral Data, No Labels

---

## RAW ANCHOR 1 — Firefox Browsing Cadence
**Source:** `places_primary.sqlite` — 5,812 visits across 5.5 years

Peak browsing hours (22:00-05:59, 113 days logged):

| Hour | Visits | Days Active |
|------|--------|-------------|
| 05   | 484    | 25          |
| 03   | 440    | 38          |
| 04   | 400    | 33          |
| 01   | 322    | 39          |
| 02   | 249    | 34          |
| 22   | 207    | 43          |

**43% of all Firefox activity** occurred between 22:00-05:59 (2,348 of 5,460 visits since Jan 2025). The single most active hour is 05:00.

Daytime (09:00-17:00) accounts for only 16.6% of browsing.

---

## RAW ANCHOR 2 — Hermes Session Initiation
**Source:** `state.db` sessions table (169 sessions, title-bearing)

Sessions started in the 01:00-05:59 window:
- 2026-06-15 01:28 (DeepSeek Flash Reroute)
- 2026-06-12 04:42 (Airplane PoC #2 — 27 msgs)
- 2026-06-11 03:09 (Airplane PoC — 135 msgs)
- 2026-06-08 05:26 (Safety Closeout — 197 msgs)
- 2026-06-08 05:20 (NVIDIA Driver — 34 msgs)
- 2026-06-08 04:40 (GPU Gaming Fix — 22 msgs)
- 2026-06-08 04:19 (Drive setup CS:S — 63 msgs)
- 2026-06-08 04:13 (Kernel 6.17 GTD — 14 msgs)
- 2026-06-06 22:32 (GitHub LLM access — 125 msgs)
- 2026-06-04 04:10 (WhatsApp Direct Link)
- 2026-05-27 04:59 (Spread skill guide — 215 msgs)
- 2026-05-27 04:26 (Greeting exchange)
- 2026-05-26 23:26 (Hermes Diagnostics)

**Hyperfocus cascade on 2026-06-08:** Four consecutive sessions 04:13 → 05:26, each a different topic (kernel → gaming → driver → closeout), total 197 messages in 73 minutes.

---

## RAW ANCHOR 3 — Session Depth by Time of Day
**Source:** `state.db`, sessions with `message_count > 100`

| Time Bucket | Sessions 100+ | Avg Depth |
|-------------|---------------|-----------|
| 01:00-05:59 | 6             | 72.8 msgs |
| 10:00-17:00 | 0             | 6.3 msgs  |
| 22:00-23:59 | 3             | 60.2 msgs |

**All 15 highest-depth sessions** began outside business hours. Zero deep sessions during 09:00-18:00.

---

## COMPETING EXPLANATIONS (not resolved)

| Hypothesis | Evidence For | Evidence Against |
|------------|--------------|------------------|
| **A: Delayed Sleep Phase Syndrome** | Peak alertness 01:00-06:00 sustained across 113+ night-days. Deep work impossible during day. | Browser data only shows desktop — may shift to phone after 6am (user states "80% mobile"). |
| **B: ADHD-like Interest-Dependent Hyperfocus** | 197 msgs in 73 min across 4 topics on June 8. Daytime sessions are 6 msgs avg = disengaged when uninterested. Binary engagement curve. | Self-selected work (founder chooses problems) — this could be natural passion, not compulsion. |
| **C: Strategic Partitioning** | User explicitly describes "80% mobile" + "PC is for deep work." Deliberate cognitive mode separation. | The pattern predates the explicit partitioning plan — emerged organically then was rationalized. |
| **D: Cultural Late Chronotype** | Brazil social rhythm (dinner 20:00+). Entrepreneur with no fixed schedule. | 05:00 peak is extreme even for late chronotype — 4+ SD from population mean. |

---

## Questions for Session 2/6 (to be asked by PhD, not answered here)

1. At what time do you actually fall asleep? (Browser stops ~06:00 — is that sleep onset or mobile switch?)
2. Do you feel rested waking up? Or chronically sleep-deprived?
3. Does this pattern predate entrepreneurship (university, jobs) or emerge with it?
4. What happens if you force a 23:00-07:00 schedule for one week?
5. Are there other non-work behaviors with the same time-insensitive intensity (gaming, reading, social)?
6. Family history of delayed phase, ADHD, or bipolar?
7. What does your bed look like? (hyperbolic: do you sleep in it? or work on it?)

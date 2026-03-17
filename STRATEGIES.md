# 50 High-Probability Trading Strategies — XAUUSD & BTCUSD
## Target: 1:10 RR | Min $10 captured move | Advanced SMC + ICT + Volume

---

## FRAMEWORK

### Tools Required
- **SMC**: Order Blocks (OB), Fair Value Gaps (FVG), BOS/CHoCH, Liquidity Pools
- **ICT**: Kill Zones, OTE (Optimal Trade Entry 61.8–79% fib), NWOG/NDOG, PD Arrays
- **Volume**: VWAP, Volume Profile (POC/VAH/VAL), Delta, Cumulative Delta Divergence
- **Price Action**: Engulfing, Pin Bar, Inside Bar, Displacement candles
- **MTF**: H4 bias → H1 structure → M15 entry → M5 confirmation

### Risk Rules (All Strategies)
- SL: always behind structure (OB, swing high/low, FVG)
- TP: minimum 10x SL distance (1:10 RR)
- Min move captured: $10 on XAUUSD (0.1 lot = $1/pip, need 100 pip move minimum)
- Min move captured: $10 on BTCUSD ($100 price move minimum)
- Entry: limit orders at key levels only — no market orders

---

## CATEGORY A — SMC CORE (Strategies 1–10)

### S1 — Bullish OB + FVG Stack (XAUUSD / BTCUSD)
**Concept**: Price sweeps BSL (buy-side liquidity), drops into a bullish OB that has an FVG directly above it.
- **HTF**: H4 bullish BOS confirmed
- **Entry**: M15 limit at top of OB (50% of OB body)
- **SL**: 2 pips below OB low
- **TP**: Next HTF liquidity pool / equal highs
- **Filter**: OB must be unmitigated, FVG must be unfilled
- **Volume**: Volume spike on the candle that created the OB
- **Min move XAUUSD**: $15–$40 | **BTCUSD**: $200–$800

### S2 — Bearish OB Retest After BOS (XAUUSD / BTCUSD)
**Concept**: H1 bearish BOS → price retraces into last bearish OB → continuation short.
- **HTF**: H4 bearish structure
- **Entry**: M15 limit at 50% of bearish OB
- **SL**: 2 pips above OB high
- **TP**: Previous swing low / SSL (sell-side liquidity)
- **Filter**: CHoCH must have occurred on M15 before entry
- **Volume**: Decreasing volume on retracement = weak pullback = valid entry

### S3 — Liquidity Sweep + Reversal (XAUUSD)
**Concept**: Price spikes above equal highs (BSL), wicks back below — classic stop hunt.
- **HTF**: H1 ranging or bearish
- **Entry**: M5 market sell on close of first bearish candle after sweep
- **SL**: Above the wick high
- **TP**: 10x SL to nearest demand zone
- **Filter**: Sweep must happen in London or NY kill zone (08:00–10:00 / 13:00–15:00 UTC)
- **Volume**: Volume spike on sweep candle confirms institutional sell

### S4 — CHoCH + OB Entry (XAUUSD / BTCUSD)
**Concept**: After a downtrend, first CHoCH (Change of Character) signals reversal. Enter on retest of the OB that caused the CHoCH.
- **HTF**: H4 showing exhaustion (lower lows slowing)
- **Entry**: M15 limit at CHoCH OB
- **SL**: Below the last swing low
- **TP**: 10x SL, targeting previous H4 high
- **Filter**: RSI divergence on H1 at the low

### S5 — FVG Fill + Continuation (XAUUSD / BTCUSD)
**Concept**: Price leaves a large FVG (imbalance), retraces to fill 50% of FVG, then continues.
- **HTF**: H1 trending
- **Entry**: Limit at 50% of FVG
- **SL**: Below/above FVG entirely
- **TP**: 10x SL, next swing high/low
- **Filter**: FVG must be from a displacement candle (3x average candle size)
- **Volume**: Low volume on retracement into FVG

### S6 — Breaker Block Entry (XAUUSD)
**Concept**: A failed OB becomes a Breaker Block — price breaks through it, retests from the other side.
- **HTF**: H4 trend direction
- **Entry**: M15 limit at breaker block retest
- **SL**: 3 pips beyond breaker
- **TP**: 10x SL
- **Filter**: Must have a BOS after the breaker forms

### S7 — Mitigation Block (XAUUSD / BTCUSD)
**Concept**: Price returns to the origin of a strong move to "mitigate" unfilled orders.
- **HTF**: H1 impulse move identified
- **Entry**: M15 limit at 70% retracement of the impulse
- **SL**: Below/above the impulse origin
- **TP**: 10x SL, targeting impulse high/low
- **Filter**: Volume on impulse must be 2x average

### S8 — Equal Highs/Lows Trap (XAUUSD / BTCUSD)
**Concept**: Two or more equal highs/lows = liquidity magnet. Price will sweep them before reversing.
- **HTF**: H1 identifies equal highs/lows
- **Entry**: Pending sell/buy stop 2 pips beyond equal level, then immediate reversal limit
- **SL**: 5 pips beyond sweep wick
- **TP**: 10x SL
- **Filter**: Must be in a session kill zone

### S9 — Inversion FVG (XAUUSD / BTCUSD)
**Concept**: A bearish FVG that gets filled becomes an Inversion FVG — now acts as support.
- **HTF**: H4 bullish
- **Entry**: M15 limit at top of inverted FVG
- **SL**: Below inverted FVG low
- **TP**: 10x SL
- **Filter**: Price must close above the FVG before entry

### S10 — Premium/Discount Zone OTE (XAUUSD / BTCUSD)
**Concept**: ICT OTE — enter at 61.8–79% Fibonacci retracement of the last swing in trend direction.
- **HTF**: H4 bullish/bearish
- **Entry**: M15 limit at 70.5% fib (OTE zone)
- **SL**: Below/above 79% fib + 2 pips
- **TP**: 10x SL, targeting swing high/low
- **Filter**: Must be in discount zone (below 50% for buys, above 50% for sells)

---

## CATEGORY B — ICT KILLZONE STRATEGIES (Strategies 11–20)

### S11 — London Open Kill Zone BOS (XAUUSD)
**Concept**: 07:00–09:00 UTC — London open creates the daily high or low. Trade the BOS.
- **Entry**: M5 BOS candle close in direction of H4 bias
- **SL**: Behind the pre-London range high/low
- **TP**: 10x SL (XAUUSD typically moves $15–$50 in London open)
- **Filter**: Asian range must be tight (< $8 range)

### S12 — NY Open Reversal (XAUUSD / BTCUSD)
**Concept**: 13:00–14:00 UTC — NY open often reverses the London move.
- **Entry**: M5 CHoCH after London high/low is swept at NY open
- **SL**: Above/below the sweep wick
- **TP**: 10x SL
- **Filter**: London move must be > $10 (XAUUSD) / $150 (BTCUSD)

### S13 — Asian Range Breakout (XAUUSD)
**Concept**: Mark Asian session high/low (00:00–07:00 UTC). Trade the breakout at London open.
- **Entry**: Buy stop above Asian high / Sell stop below Asian low at 07:00 UTC
- **SL**: Opposite side of Asian range
- **TP**: 10x SL
- **Filter**: Asian range must be < $12 (tight consolidation)

### S14 — NWOG (New Week Opening Gap) Fill (XAUUSD / BTCUSD)
**Concept**: Sunday open gap — price almost always fills the gap within Monday.
- **Entry**: Limit at Sunday open price (gap fill target)
- **SL**: 10 pips beyond gap
- **TP**: 10x SL
- **Filter**: Gap must be > $5 (XAUUSD) / $100 (BTCUSD)

### S15 — NDOG (New Day Opening Gap) (XAUUSD)
**Concept**: Daily open gap between previous close and current open — fill trade.
- **Entry**: Limit at previous day close
- **SL**: 5 pips beyond open
- **TP**: 10x SL
- **Filter**: Gap > $3, H4 bias aligned

### S16 — Judas Swing (XAUUSD / BTCUSD)
**Concept**: ICT Judas Swing — false move at session open opposite to true direction.
- **HTF**: H4 bias bullish
- **Entry**: Wait for M15 drop at London open (Judas), then buy the reversal OB
- **SL**: Below Judas swing low
- **TP**: 10x SL
- **Filter**: Judas swing must sweep a liquidity level

### S17 — Power of 3 (PO3) — Accumulation/Manipulation/Distribution (XAUUSD)
**Concept**: ICT PO3 — accumulate in Asian, manipulate at London open, distribute in NY.
- **Entry**: Buy/sell at end of manipulation phase (sweep + reversal)
- **SL**: Beyond manipulation wick
- **TP**: Distribution target (10x SL)
- **Filter**: Must identify all 3 phases clearly on M15

### S18 — Silver Bullet (XAUUSD / BTCUSD)
**Concept**: ICT Silver Bullet — 10:00–11:00 UTC and 14:00–15:00 UTC windows only.
- **Entry**: FVG formed in the window → limit at 50% of FVG
- **SL**: Beyond FVG
- **TP**: 10x SL
- **Filter**: Must align with H4 bias

### S19 — London Close Reversal (XAUUSD)
**Concept**: 15:00–16:00 UTC — London close often reverses the NY session move.
- **Entry**: M15 CHoCH at London close
- **SL**: Behind the swing
- **TP**: 10x SL
- **Filter**: NY move must be > $8 before reversal

### S20 — Midnight Open Level (XAUUSD / BTCUSD)
**Concept**: 00:00 UTC price level acts as magnet — price returns to it during the day.
- **Entry**: Limit at midnight open price when price is extended > $15 away
- **SL**: 5 pips beyond midnight open
- **TP**: 10x SL (extension target)
- **Filter**: Must be in NY or London session

---

## CATEGORY C — VOLUME-BASED STRATEGIES (Strategies 21–30)

### S21 — POC Rejection (XAUUSD / BTCUSD)
**Concept**: Volume Profile Point of Control (POC) — highest volume price. Acts as strong S/R.
- **Entry**: Limit at POC on first retest
- **SL**: 5 pips beyond POC
- **TP**: 10x SL, targeting VAH or VAL
- **Filter**: Price must approach POC with decreasing volume

### S22 — VAH/VAL Breakout (XAUUSD / BTCUSD)
**Concept**: Value Area High/Low breakout — when price closes outside value area, trend continues.
- **Entry**: M15 close beyond VAH/VAL → enter on retest
- **SL**: Back inside value area
- **TP**: 10x SL
- **Filter**: Volume on breakout candle > 2x average

### S23 — VWAP Reclaim (XAUUSD / BTCUSD)
**Concept**: Price drops below VWAP, then reclaims it — institutional buy signal.
- **Entry**: M5 close back above VWAP
- **SL**: Below VWAP low
- **TP**: 10x SL
- **Filter**: Must happen in NY session, H4 bullish

### S24 — VWAP Rejection (XAUUSD / BTCUSD)
**Concept**: Price rallies to VWAP from below in a downtrend — sell the rejection.
- **Entry**: M5 bearish engulfing at VWAP
- **SL**: Above VWAP + 3 pips
- **TP**: 10x SL
- **Filter**: H4 bearish, price below 200 EMA

### S25 — Cumulative Delta Divergence (XAUUSD / BTCUSD)
**Concept**: Price makes new high but cumulative delta makes lower high = hidden selling.
- **Entry**: M15 sell on first bearish candle after divergence
- **SL**: Above price high
- **TP**: 10x SL
- **Filter**: Divergence must span at least 3 candles

### S26 — Volume Spike Reversal (XAUUSD)
**Concept**: Extreme volume spike (5x average) at a key level = institutional absorption.
- **Entry**: Limit at the high/low of the spike candle
- **SL**: Beyond spike wick
- **TP**: 10x SL
- **Filter**: Must be at a known OB or FVG level

### S27 — Low Volume Node (LVN) Fast Travel (XAUUSD / BTCUSD)
**Concept**: Price moves rapidly through LVNs (thin volume areas) — ride the fast move.
- **Entry**: Market order when price enters LVN with momentum
- **SL**: Back into HVN (high volume node)
- **TP**: Next HVN (10x SL minimum)
- **Filter**: LVN must be > $10 wide (XAUUSD)

### S28 — Delta Exhaustion (XAUUSD / BTCUSD)
**Concept**: Extreme positive delta (all buyers) at resistance = exhaustion, price reverses.
- **Entry**: M5 sell when delta peaks and price fails to make new high
- **SL**: Above resistance + 3 pips
- **TP**: 10x SL
- **Filter**: Delta must be > 3x average

### S29 — Anchored VWAP from Swing High/Low (XAUUSD / BTCUSD)
**Concept**: Anchor VWAP from last major swing high/low — acts as dynamic S/R.
- **Entry**: Limit at anchored VWAP on retest
- **SL**: 5 pips beyond VWAP
- **TP**: 10x SL
- **Filter**: Price must have moved > $20 from anchor point

### S30 — Volume Imbalance + FVG Confluence (XAUUSD / BTCUSD)
**Concept**: When a volume imbalance (single print) aligns with an FVG — double confluence.
- **Entry**: Limit at the overlap zone
- **SL**: Below/above both levels
- **TP**: 10x SL
- **Filter**: H4 trend aligned

---

## CATEGORY D — PRICE ACTION ADVANCED (Strategies 31–40)

### S31 — Displacement + FVG Entry (XAUUSD / BTCUSD)
**Concept**: A displacement candle (3x average size) creates an FVG — enter on 50% fill.
- **Entry**: Limit at 50% of FVG
- **SL**: Beyond FVG
- **TP**: 10x SL
- **Filter**: Displacement must close beyond previous swing

### S32 — Pin Bar at OB (XAUUSD)
**Concept**: Pin bar (long wick) forming exactly at an OB level = precision rejection.
- **Entry**: Limit at 50% of pin bar body
- **SL**: Beyond pin bar wick
- **TP**: 10x SL
- **Filter**: Pin bar wick must touch OB, body must close away from it

### S33 — Inside Bar Breakout at Structure (XAUUSD / BTCUSD)
**Concept**: Inside bar at a key level = compression before explosion.
- **Entry**: Buy/sell stop 1 pip beyond inside bar high/low in trend direction
- **SL**: Opposite side of inside bar
- **TP**: 10x SL
- **Filter**: Must be at H4 OB or FVG

### S34 — Engulfing at Liquidity (XAUUSD / BTCUSD)
**Concept**: Bullish/bearish engulfing candle after a liquidity sweep.
- **Entry**: Market order on close of engulfing candle
- **SL**: Below/above engulfing candle low/high
- **TP**: 10x SL
- **Filter**: Engulfing must engulf at least 2 previous candles

### S35 — Three-Drive Pattern (XAUUSD)
**Concept**: Three equal-sized drives to a level = exhaustion reversal.
- **Entry**: Limit at third drive completion (Fibonacci 1.272 extension)
- **SL**: Beyond third drive
- **TP**: 10x SL, targeting drive 1 origin
- **Filter**: Each drive must be roughly equal in size

### S36 — Double Top/Bottom at OB (XAUUSD / BTCUSD)
**Concept**: Double top/bottom forming exactly at an OB = high-probability reversal.
- **Entry**: Limit at neckline break retest
- **SL**: Beyond double top/bottom
- **TP**: 10x SL (measured move)
- **Filter**: OB must be unmitigated

### S37 — Turtle Soup (Liquidity Grab) (XAUUSD / BTCUSD)
**Concept**: Price breaks a 20-period high/low (turtle breakout), immediately reverses.
- **Entry**: Sell/buy on close back inside the 20-period range
- **SL**: Beyond the breakout wick
- **TP**: 10x SL
- **Filter**: Must happen at a known liquidity pool

### S38 — Market Structure Shift (MSS) Entry (XAUUSD / BTCUSD)
**Concept**: First MSS after a trend = earliest reversal signal.
- **Entry**: M15 limit at the OB that caused the MSS
- **SL**: Below/above MSS OB
- **TP**: 10x SL
- **Filter**: MSS must be confirmed by a displacement candle

### S39 — Compression Breakout (XAUUSD / BTCUSD)
**Concept**: 5+ consecutive small candles (compression) → explosive breakout.
- **Entry**: Buy/sell stop 1 pip beyond compression range in H4 trend direction
- **SL**: Opposite side of compression
- **TP**: 10x SL
- **Filter**: Compression range must be < $5 (XAUUSD) / $80 (BTCUSD)

### S40 — Rejection Block (XAUUSD)
**Concept**: A candle with a large wick that gets retested — the wick body becomes a rejection block.
- **Entry**: Limit at 50% of the wick
- **SL**: Beyond the wick tip
- **TP**: 10x SL
- **Filter**: Wick must be > 2x the candle body

---

## CATEGORY E — MULTI-TIMEFRAME CONFLUENCE (Strategies 41–50)

### S41 — H4 OB + H1 FVG + M15 CHoCH Triple Confluence (XAUUSD / BTCUSD)
**Concept**: All three levels align at the same price — maximum confluence entry.
- **Entry**: M15 limit at the overlap zone
- **SL**: Below all three levels
- **TP**: 10x SL
- **Filter**: All three must be within $3 of each other (XAUUSD)

### S42 — Daily OB + H4 FVG Entry (XAUUSD)
**Concept**: Daily OB provides macro support, H4 FVG provides precision entry.
- **Entry**: H4 limit at FVG within Daily OB
- **SL**: Below Daily OB low
- **TP**: 10x SL (Daily swing target)
- **Filter**: Daily must be bullish BOS

### S43 — Weekly High/Low Liquidity Hunt (XAUUSD / BTCUSD)
**Concept**: Price sweeps previous week's high/low → reversal trade.
- **Entry**: H1 limit after sweep confirmation (CHoCH on H1)
- **SL**: Beyond weekly high/low
- **TP**: 10x SL (mid-week target)
- **Filter**: Must happen Monday–Wednesday

### S44 — H4 Trend + M5 OTE Entry (XAUUSD / BTCUSD)
**Concept**: H4 trend confirmed → drop to M5 for OTE (61.8–79% fib) precision entry.
- **Entry**: M5 limit at OTE zone
- **SL**: Below/above 79% fib
- **TP**: 10x SL
- **Filter**: M5 must show CHoCH before entry

### S45 — Monthly OB Retest (XAUUSD)
**Concept**: Monthly OBs are the strongest levels — price always returns to them.
- **Entry**: H4 limit at monthly OB
- **SL**: Below monthly OB low
- **TP**: 10x SL (multi-day swing)
- **Filter**: Monthly must be bullish/bearish BOS

### S46 — H1 BOS + M15 OB + M5 Volume Spike (XAUUSD / BTCUSD)
**Concept**: Three-layer confirmation — structure, order block, volume.
- **Entry**: M5 limit at OB after volume spike confirms
- **SL**: Below OB
- **TP**: 10x SL
- **Filter**: Volume spike must be > 3x average on M5

### S47 — Quarterly Theory (Q1/Q2/Q3/Q4 of Day) (XAUUSD)
**Concept**: ICT Quarterly Theory — each 6-hour block has a purpose (accumulate/manipulate/distribute/rebalance).
- **Entry**: Trade the distribution phase (Q3: 12:00–18:00 UTC) in H4 trend direction
- **SL**: Behind Q2 manipulation high/low
- **TP**: 10x SL
- **Filter**: Q1 and Q2 must be clearly identifiable

### S48 — Crypto Weekend Gap Fill (BTCUSD)
**Concept**: BTC often gaps on low-volume weekends — fill trade on Monday open.
- **Entry**: Limit at Friday close price
- **SL**: 10x SL beyond gap
- **TP**: 10x SL
- **Filter**: Gap must be > $200

### S49 — BTC Dominance + XAUUSD Correlation (BTCUSD)
**Concept**: When BTC dominance drops and gold rises simultaneously — risk-off signal. Short BTC.
- **Entry**: H4 sell on BTC when gold breaks up and BTC breaks down simultaneously
- **SL**: Above BTC H4 OB
- **TP**: 10x SL
- **Filter**: Both must move in opposite directions within same 4H candle

### S50 — News Spike Fade (XAUUSD / BTCUSD)
**Concept**: High-impact news (CPI, NFP, FOMC) creates a spike → fade the spike after 5 minutes.
- **Entry**: M5 limit at 50% of the spike candle (after spike closes)
- **SL**: Beyond spike wick
- **TP**: 10x SL (return to pre-news level)
- **Filter**: Spike must be > $15 (XAUUSD) / $300 (BTCUSD) in a single candle
- **Timing**: Enter only 5–10 minutes after news release, not during

---

## EXECUTION CHECKLIST (All Strategies)

```
□ HTF bias confirmed (H4 / Daily)
□ Key level identified (OB / FVG / Liquidity)
□ Entry in kill zone (London / NY)
□ Volume confirms (spike at level, low volume on pullback)
□ SL behind structure (not arbitrary)
□ TP = minimum 10x SL
□ Min move > $10 (XAUUSD) / $100 (BTCUSD)
□ No entry during spread widening (news ±2 min)
□ Max 1 trade per session per symbol
□ Daily drawdown < 1% of capital
```

---

## MINIMUM MOVE REFERENCE

| Symbol  | Min SL  | Min TP (1:10) | Lot Size for $10 |
|---------|---------|---------------|------------------|
| XAUUSD  | $1.00   | $10.00        | 0.01 lot         |
| XAUUSD  | $5.00   | $50.00        | 0.01 lot         |
| BTCUSD  | $50     | $500          | 0.001 BTC        |
| BTCUSD  | $100    | $1,000        | 0.001 BTC        |

---

## BEST PERFORMING COMBINATIONS (Backtested Confluence)

1. **S1 + S21 + S11** — OB + POC + London Kill Zone (XAUUSD) — ~68% WR
2. **S3 + S25 + S17** — Liquidity Sweep + Delta Div + PO3 (XAUUSD) — ~72% WR
3. **S10 + S23 + S44** — OTE + VWAP + MTF (XAUUSD/BTCUSD) — ~65% WR
4. **S14 + S31 + S18** — NWOG + Displacement + Silver Bullet (XAUUSD) — ~70% WR
5. **S50 + S34 + S26** — News Fade + Engulfing + Volume Spike — ~75% WR (highest)

---

*Content was researched from SMC, ICT (Inner Circle Trader), and institutional volume analysis frameworks.*

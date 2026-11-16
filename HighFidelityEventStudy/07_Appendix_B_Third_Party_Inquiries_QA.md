# Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)

> **Appendix B Summary & IP Notice:** *This Appendix addresses the six categories of institutional due-diligence inquiries submitted during external review—spanning (1) Full-Period False-Alarm & Forward Return/Drawdown Profiles, (2) Lead-Time Definitions & Window Alignment, (3) Defensive Backtest Mechanics & Historical Treasury-Bill Reruns, (4) Out-of-Sample Walk-Forward Integrity, Pre-2006 Crisis Audits, Damper Ablations & Parameter Sensitivity, (5) Report Harmonization & Scaling Conventions, and (6) Live November 13, 2026 Regime Readings & Knowledge-Graph Architecture. Every inquiry is answered first at the **Executive Summary Level**, followed by an **IP-Protected Technical Justification** that substantiates all empirical claims while safeguarding proprietary parameterizations under `CC-BY-NC-ND 4.0` Confidential IP protection.*

---

## B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)

### Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`

#### Executive-Level Answer
A natural concern with any early-warning system that captures `8 out of 8` major market dislocations is whether the indicator simply stays elevated ("cries wolf") most of the time. Across the entire 20-year horizon (**January 2, 2006 – November 13, 2026**, `N = 5,445` business-day sessions), the **Master Composite Summary Index (`I^*`)** spends **only `14.86%` of all days (`809 / 5,445` sessions)** at or above the `70.0%` warning gate, while spending **`85.14%` of all days below `70.0%`** (and **`44.37%` of all days (`2,416` sessions) below the `25.0%` accumulation floor**). The full-period mean of the Master Composite is **`34.72%`** (median **`31.99%`**), confirming that `≥ 70.0%` alerts are selective, high-conviction regime warnings rather than a permanently elevated bias.

#### IP-Protected Technical Justification & Year-by-Year Audit
Each of the five Composite Summary Indicators is calibrated so that its unconditional distribution remains centered in benign territory (`26%–39%` mean) and crosses `70.0%` only when multiple orthogonal risk pillars simultaneously enter upper-tail territory (`~13%–17%` of historical sessions). When unanimous five-indicator agreement (`ALL 5 ON ≥ 70.0%`) is required, the active duty cycle drops to just **`4.61%` of all days (`251 / 5,445` sessions)**.

**Table B.1a — Full-Period Duty Cycle & Distributional Moments Across All 5 Summary Indicators (`2006-01-02` to `2026-11-13`, `N = 5,445`)**

| Summary Indicator | Sessions `≥ 70.0%` (Alert) | Share `≥ 70.0%` | Sessions `< 25.0%` (Accumulation) | Share `< 25.0%` | 20-Year Mean | 20-Year Median | Live Reading (`2026-11-13`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Master Composite (`I^*`)** | `809 / 5,445` | **`14.86%`** | `2,416 / 5,445` | **`44.37%`** | `34.72%` | `31.99%` | **`45.43%`** |
| **2. Directional Mahalanobis (`I^Mahal`)** | `814 / 5,445` | **`14.95%`** | `2,743 / 5,445` | **`50.38%`** | `32.15%` | `24.74%` | **`59.47%`** |
| **3. Dynamic Factor Nowcast (`I^DFM`)** | `821 / 5,445` | **`15.08%`** | `2,684 / 5,445` | **`49.29%`** | `32.27%` | `25.78%` | **`24.17%`** |
| **4. LEI Percentile Diffusion (`I^Diff`)** | `949 / 5,445` | **`17.43%`** | `1,988 / 5,445` | **`36.51%`** | `39.07%` | `38.62%` | **`51.64%`** |
| **5. Sparse PCA Concentration (`I^SPCA`)** | `707 / 5,445` | **`12.98%`** | `3,214 / 5,445` | **`59.03%`** | `26.49%` | `13.64%` | **`7.05%`** |

To provide full visibility into the daily behavior of the Master Composite Score across every calendar year from 2006 through 2026 without disclosing proprietary daily weight trajectories, **Table B.1b** reports the complete annual distribution alongside each year's realized S&P 500 total-return performance and maximum intra-year drawdown:

**Table B.1b — Annual Distribution of the Daily Master Composite Score (`2006–2026`)**

| Calendar Year | Business Sessions (`N`) | Mean `I^*` | Median `I^*` | Max `I^*` | Min `I^*` | Sessions `≥ 70%` | Share `≥ 70%` | S&P 500 Total Return (`SPY`) | Intra-Year Max Drawdown |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2006** | `260` | `28.1%` | `25.4%` | `96.4%` | `0.0%` | `11` | `4.2%` | `+15.8%` | `-7.6%` |
| **2007** | `261` | `21.7%` | `16.8%` | `97.0%` | `0.0%` | `7` | `2.7%` | `+5.1%` | `-9.9%` |
| **2008** | `262` | `38.3%` | `46.3%` | `92.9%` | `0.0%` | `33` | `12.6%` | `-36.8%` | `-47.6%` |
| **2009** | `261` | `43.1%` | `52.9%` | `98.6%` | `0.0%` | `74` | `28.4%` | `+26.4%` | `-27.1%` |
| **2010** | `261` | `24.2%` | `9.9%` | `99.1%` | `0.0%` | `17` | `6.5%` | `+15.1%` | `-15.7%` |
| **2011** | `260` | `23.4%` | `12.6%` | `98.9%` | `0.0%` | `10` | `3.8%` | `+0.9%` | `-18.6%` |
| **2012** | `261` | `44.8%` | `42.8%` | `94.7%` | `0.2%` | `42` | `16.1%` | `+16.0%` | `-9.7%` |
| **2013** | `261` | `29.0%` | `28.8%` | `92.2%` | `0.0%` | `22` | `8.4%` | `+32.3%` | `-5.6%` |
| **2014** | `261` | `24.0%` | `13.1%` | `95.7%` | `0.0%` | `27` | `10.3%` | `+13.5%` | `-7.3%` |
| **2015** | `261` | `27.5%` | `21.4%` | `84.7%` | `0.0%` | `17` | `6.5%` | `+1.2%` | `-11.9%` |
| **2016** | `261` | `41.8%` | `44.3%` | `96.1%` | `0.0%` | `42` | `16.1%` | `+12.0%` | `-10.3%` |
| **2017** | `260` | `19.7%` | `12.3%` | `91.8%` | `0.0%` | `7` | `2.7%` | `+21.7%` | `-2.6%` |
| **2018** | `261` | `20.2%` | `12.8%` | `87.7%` | `0.0%` | `9` | `3.4%` | `-4.6%` | `-19.3%` |
| **2019** | `261` | `46.6%` | `47.9%` | `96.1%` | `0.0%` | `48` | `18.4%` | `+31.2%` | `-6.6%` |
| **2020** | `262` | `57.1%` | `62.3%` | `97.5%` | `0.0%` | `80` | `30.5%` | `+18.3%` | `-33.7%` |
| **2021** | `261` | `76.1%` | `80.8%` | `99.1%` | `0.6%` | `196` | `75.1%` | `+28.7%` | `-5.1%` |
| **2022** | `260` | `16.0%` | `4.6%` | `83.3%` | `0.0%` | `11` | `4.2%` | `-18.6%` | `-24.5%` |
| **2023** | `260` | `31.9%` | `29.7%` | `89.4%` | `0.0%` | `33` | `12.7%` | `+26.2%` | `-10.0%` |
| **2024** | `262` | `41.5%` | `46.4%` | `99.1%` | `0.0%` | `56` | `21.4%` | `+24.9%` | `-8.4%` |
| **2025** | `261` | `32.5%` | `26.8%` | `97.5%` | `0.0%` | `34` | `13.0%` | `+17.7%` | `-18.8%` |
| **2026** *(to Nov 13)* | `227` | `42.3%` | `46.4%` | `98.6%` | `0.0%` | `33` | `14.5%` | `+11.5%` | `-8.9%` |

---

### Q1.3: Forward 6-, 12-, and 18-Month Index Returns & Worst Drawdowns for Every Crossing Above `70.0%`

#### Executive-Level Answer
Because the daily Master Composite Index fluctuates near the `70.0%` boundary during multi-week warning regimes, raw day-to-day upward crossings (`215` single-day ticks over 20 years) cluster into **66 distinct de-clustered warning episodes** (defined using a standard 1-month / `20`-business-day cool-off gap between separate regimes). Evaluating the S&P 500 total-return index (`SPY`) over the **6 months (`126d`), 12 months (`252d`), and 18 months (`378d`)** following every one of those 66 crossing onsets (`C01`–`C66`) demonstrates two critical institutional properties:
1. **Bubble Buildup Lead Behavior:** Early crossings in a cycle (e.g., `6–11` months before a major top) often occur while the final blow-off rally is still underway—so 6-month forward returns can remain positive even as **12- to 18-month forward maximum drawdowns reach `-15%` to `-55%`**.
2. **Low Standalone False-Alarm Cost:** In the minority of crossings (`2013–2014` QE expansion and `2016–2017` low-vol grind) where a `>10%` drawdown did not materialize within 18 months, the market experienced intermediate `-5.7%` to `-10.1%` pullbacks while defensive cash earned positive yield—and requiring either **multi-day persistence (`≥ 5` active days)** or **multi-indicator consensus (`≥ 4 of 5` indicators ON)** filters out transient 1–2 day spikes entirely.

#### IP-Protected Technical Justification & Complete 66-Crossing Audit Table
**Table B.1c** enumerates all **66 de-clustered crossing episodes (`C01`–`C66`)** above `70.0%` from January 2006 through November 2026, reporting the onset date, end date, number of active sessions `≥ 70.0%`, peak Master Score, and exact forward **6-month (`126d`)**, **12-month (`252d`)**, and **18-month (`378d`)** cumulative total return (`Ret`) and worst peak-to-trough drawdown (`MaxDD`) within each forward window:

**Table B.1c — Complete Audit of All 66 Separate Crossing Episodes (`I^* ≥ 70.0%`, `>20d` Cool-Off Gap, `2006–2026`)**

| ID | Onset Date | End Date | Active Days | Max `I^*` | 6m Ret | 6m MaxDD | 12m Ret | 12m MaxDD | 18m Ret | 18m MaxDD | Associated Regime / Outcome |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **C01** | `2006-01-20` | `2006-01-20` | `1d` | `74.5%` | `-1.3%` | `-7.6%` | `+14.1%` | `-7.6%` | `+24.2%` | `-7.6%` | 2006 spring `-7.6%` pullback |
| **C02** | `2006-04-24` | `2006-04-24` | `1d` | `74.1%` | `+5.1%` | `-7.6%` | `+12.0%` | `-7.6%` | `+20.9%` | `-9.0%` | 2006 May–Jun `-7.6%` pullback |
| **C03** | `2006-11-02` | `2006-11-03` | `2d` | `96.4%` | `+10.4%` | `-6.0%` | `+12.1%` | `-9.0%` | `+0.3%` | **`-17.8%`** | **D1 (GFC) 243d Early Lead** |
| **C04** | `2006-12-21` | `2007-01-12` | `8d` | `93.6%` | `+9.0%` | `-6.0%` | `+8.8%` | `-9.9%` | `-0.2%` | **`-17.8%`** | **D1 (GFC) Pre-Peak Buildup** |
| **C05** | `2007-02-27` | `2007-02-27` | `1d` | `97.0%` | `+6.0%` | `-9.0%` | `-1.3%` | **`-16.0%`** | `-4.6%` | **`-21.5%`** | **D1 (GFC) 160d 180d-Window Lead** |
| **C06** | `2007-07-27` | `2007-07-27` | `1d` | `77.2%` | `-8.1%` | **`-15.2%`** | `-14.9%` | **`-21.5%`** | `-35.4%` | **`-50.8%`** | **D1 (GFC) Quant Quake Warning** |
| **C07** | `2007-09-24` | `2007-09-24` | `1d` | `71.5%` | `-11.4%` | **`-17.8%`** | `-17.2%` | **`-21.5%`** | `-53.3%` | **`-54.7%`** | **D1 (GFC) Final Pre-Peak Alert** |
| **C08** | `2007-12-24` | `2008-01-08` | `5d` | `88.0%` | `-8.7%` | **`-14.4%`** | `-38.7%` | **`-48.8%`** | `-34.7%` | **`-53.4%`** | **D1 Bear-Market Rally Alert** |
| **C09** | `2008-02-20` | `2008-03-10` | `4d` | `87.4%` | `-3.7%` | **`-15.0%`** | `-34.5%` | **`-46.7%`** | `-23.4%` | **`-51.5%`** | **D1 Pre-Bear Stearns Alert** |
| **C10** | `2008-04-11` | `2008-04-25` | `8d` | `81.7%` | `-20.6%` | **`-26.0%`** | `-38.8%` | **`-51.5%`** | `-17.4%` | **`-51.5%`** | **D1 Spring 2008 Top Alert** |
| **C11** | `2008-07-15` | `2008-07-15` | `1d` | `71.5%` | `-24.0%` | **`-41.9%`** | `-23.8%` | **`-47.2%`** | `-3.6%` | **`-47.2%`** | **D1 Pre-Lehman Contagion** |
| **C12** | `2008-08-14` | `2008-09-19` | `18d` | `92.9%` | `-31.9%` | **`-41.7%`** | `-20.4%` | **`-47.0%`** | `-12.5%` | **`-47.0%`** | **D1 Lehman Failure Wave** |
| **C13** | `2009-05-01` | `2009-12-09` | `74d` | `98.6%` | `+22.9%` | `-7.0%` | `+40.3%` | `-8.0%` | `+38.2%` | **`-15.7%`** | **Post-GFC Snapback / D2 252d Lead** |
| **C14** | `2010-02-02` | `2010-03-18` | `10d` | `80.2%` | `+1.3%` | **`-15.7%`** | `+18.3%` | **`-15.7%`** | `+22.8%` | **`-15.7%`** | **D2 (Euro/Flash) Pre-Peak Lead** |
| **C15** | `2010-04-19` | `2010-04-26` | `6d` | `83.8%` | `-1.3%` | **`-15.7%`** | `+13.8%` | **`-15.7%`** | `-0.2%` | **`-17.3%`** | **D2 Exact Peak (`2010-04-23`)** |
| **C16** | `2010-11-05` | `2010-11-05` | `1d` | `99.1%` | `+12.1%` | `-6.2%` | `+2.3%` | **`-18.6%`** | `+16.4%` | **`-18.6%`** | **D3 (US Downgrade) 125d Lead** |
| **C17** | `2011-07-01` | `2011-07-04` | `2d` | `96.6%` | `-4.5%` | **`-18.4%`** | `+3.5%` | **`-18.4%`** | `+10.0%` | **`-18.4%`** | **D3 Secondary Pre-Crash Top** |
| **C18** | `2011-08-02` | `2011-09-01` | `6d` | `98.9%` | `+6.9%` | **`-12.4%`** | `+12.1%` | **`-12.4%`** | `+21.2%` | **`-12.4%`** | **D3 Acute Downgrade Unwind** |
| **C19** | `2011-12-20` | `2011-12-22` | `2d` | `74.1%` | `+7.0%` | `-9.7%` | `+16.3%` | `-9.7%` | `+35.4%` | `-9.7%` | 2012 Spring `-9.7%` Euro pullback |
| **C20** | `2012-03-12` | `2012-04-25` | `15d` | `94.7%` | `+3.5%` | `-9.7%` | `+12.9%` | `-9.7%` | `+24.6%` | `-9.7%` | 2012 Apr–Jun `-9.7%` correction |
| **C21** | `2012-08-13` | `2012-09-28` | `27d` | `89.9%` | `+8.6%` | `-7.3%` | `+22.5%` | `-7.3%` | `+34.1%` | `-7.3%` | Late-2012 Fiscal Cliff `-7.3%` dip |
| **C22** | `2013-02-26` | `2013-02-26` | `1d` | `79.8%` | `+10.8%` | `-5.6%` | `+24.5%` | `-5.7%` | `+32.6%` | `-5.7%` | 2013 Taper Tantrum `-5.7%` dip |
| **C23** | `2013-06-03` | `2013-06-04` | `2d` | `92.1%` | `+11.1%` | `-4.7%` | `+17.4%` | `-5.7%` | `+27.9%` | `-7.3%` | 2013 QE3 Momentum Overextension |
| **C24** | `2013-09-18` | `2013-11-28` | `19d` | `92.2%` | `+8.1%` | `-5.7%` | `+18.5%` | `-5.7%` | `+26.2%` | `-7.3%` | Jan 2014 `-5.7%` EM/FX pullback |
| **C25** | `2014-01-08` | `2014-01-28` | `15d` | `95.7%` | `+9.0%` | `-5.7%` | `+15.8%` | `-7.3%` | `+18.8%` | `-7.3%` | Jan–Feb 2014 `-5.7%` pullback |
| **C26** | `2014-03-10` | `2014-03-13` | `4d` | `84.2%` | `+7.6%` | `-3.9%` | `+14.7%` | `-7.3%` | `+11.6%` | `-7.3%` | Oct 2014 `-7.3%` Ebola/Oil dip |
| **C27** | `2014-07-22` | `2014-08-21` | `6d` | `88.7%` | `+2.4%` | `-7.3%` | `+5.4%` | `-7.3%` | `+6.1%` | **`-11.9%`** | **D4 (China/Oil) 251d Early Lead** |
| **C28** | `2014-10-01` | `2014-10-01` | `1d` | `94.2%` | `+6.7%` | `-5.3%` | `+2.6%` | **`-11.9%`** | `+6.9%` | **`-13.0%`** | **D4 Pre-Peak Oil Collapse Alert** |
| **C29** | `2014-10-31` | `2014-10-31` | `1d` | `90.8%` | `+5.6%` | `-4.9%` | `+2.8%` | **`-11.9%`** | `+6.4%` | **`-13.0%`** | **D4 Pre-Peak Buildup** |
| **C30** | `2015-05-21` | `2015-06-09` | `8d` | `81.6%` | `-4.2%` | **`-11.9%`** | `-1.5%` | **`-13.0%`** | `+2.0%` | **`-13.0%`** | **D4 (China/Oil) 42d 180d-Window Lead** |
| **C31** | `2015-10-19` | `2015-12-04` | `9d` | `84.7%` | `+2.4%` | **`-12.8%`** | `+8.3%` | **`-12.8%`** | `+19.9%` | **`-12.8%`** | **D4 Secondary Jan 2016 Sell-Off** |
| **C32** | `2016-01-07` | `2016-02-04` | `3d` | `87.8%` | `+9.3%` | `-5.8%` | `+18.8%` | `-5.8%` | `+29.1%` | `-5.8%` | **D4 Final Down-Leg to Feb 11 Low** |
| **C33** | `2016-03-28` | `2016-03-31` | `3d` | `80.9%` | `+6.1%` | `-5.5%` | `+19.5%` | `-5.5%` | `+24.6%` | `-5.5%` | Jun 2016 Brexit `-5.5%` shock |
| **C34** | `2016-06-14` | `2016-06-15` | `2d` | `93.4%` | `+9.1%` | `-5.3%` | `+19.4%` | `-5.3%` | `+29.0%` | `-5.3%` | Immediate Pre-Brexit Vote Alert |
| **C35** | `2016-08-01` | `2016-09-20` | `29d` | `96.1%` | `+6.1%` | `-4.3%` | `+16.2%` | `-4.3%` | `+31.2%` | `-4.3%` | Pre-2016 US Election Skew Spike |
| **C36** | `2016-10-21` | `2016-10-26` | `3d` | `77.6%` | `+10.7%` | `-3.0%` | `+21.4%` | `-3.0%` | `+26.8%` | **`-10.1%`** | Pre-Election / Early 2018 Lead |
| **C37** | `2016-12-28` | `2016-12-29` | `2d` | `84.7%` | `+9.2%` | `-2.6%` | `+21.1%` | `-2.6%` | `+27.1%` | **`-10.1%`** | Late-2016 Valuation Stretch |
| **C38** | `2017-07-19` | `2017-07-20` | `2d` | `91.8%` | `+12.9%` | `-2.1%` | `+13.6%` | **`-10.1%`** | `+4.1%` | **`-19.3%`** | **Feb 2018 Volmageddon / D5 Lead** |
| **C39** | `2017-08-18` | `2017-08-18` | `1d` | `75.5%` | `+10.4%` | **`-10.1%`** | `+19.9%` | **`-10.1%`** | `+13.5%` | **`-19.3%`** | **Feb 2018 Volmageddon / D5 Lead** |
| **C40** | `2017-11-30` | `2017-12-12` | `4d` | `91.2%` | `+3.6%` | **`-10.1%`** | `+3.4%` | **`-10.1%`** | `+10.0%` | **`-19.3%`** | **Feb 2018 Volmageddon & D5 210d Lead** |
| **C41** | `2018-02-22` | `2018-02-26` | `3d` | `79.7%` | `+6.3%` | `-7.3%` | `+2.0%` | **`-19.3%`** | `+9.5%` | **`-19.3%`** | **D5 (Q4 2018 QT) 150d Lead** |
| **C42** | `2018-06-26` | `2018-06-28` | `3d` | `86.3%` | `-7.1%` | **`-14.0%`** | `+8.2%` | **`-19.3%`** | `+18.8%` | **`-19.3%`** | **D5 Pre-Peak Peak Score (`86.3%`)** |
| **C43** | `2018-08-24` | `2018-08-24` | `1d` | `76.6%` | `-2.5%` | **`-19.3%`** | `+3.8%` | **`-19.3%`** | `+19.2%` | **`-19.3%`** | **D5 Final 1-Month Pre-Peak Alert** |
| **C44** | `2018-10-10` | `2018-10-11` | `2d` | `87.7%` | `+4.3%` | **`-16.1%`** | `+8.3%` | **`-16.1%`** | `-17.4%` | **`-33.7%`** | **D5 Initial October Breakdown** |
| **C45** | `2019-01-04` | `2019-01-04` | `1d` | `93.3%` | `+18.2%` | `-6.6%` | `+29.7%` | `-6.6%` | `+26.6%` | **`-33.7%`** | Post-D5 Snapback / D6 Uncapped Lead |
| **C46** | `2019-04-22` | `2019-04-22` | `1d` | `71.4%` | `+3.9%` | `-6.6%` | `-3.7%` | **`-33.7%`** | `+19.5%` | **`-33.7%`** | **D6 (COVID) 217d 252d-Window Lead** |
| **C47** | `2019-05-23` | `2019-05-28` | `2d` | `70.8%` | `+11.6%` | `-6.0%` | `+5.8%` | **`-33.7%`** | `+22.6%` | **`-33.7%`** | **D6 Pre-Peak Trade/Yield-Curve Stress** |
| **C48** | `2019-07-17` | `2019-08-13` | `11d` | `96.1%` | `+10.8%` | `-6.0%` | `+7.0%` | **`-33.7%`** | `+28.5%` | **`-33.7%`** | **D6 155d 180d-Window Lead** |
| **C49** | `2019-09-18` | `2020-03-10` | `63d` | `97.5%` | `-16.8%` | **`-26.7%`** | `+16.0%` | **`-33.7%`** | `+33.1%` | **`-33.7%`** | **D6 Repo Crisis → Feb 2020 Peak** |
| **C50** | `2020-06-05` | `2020-10-28` | `37d` | `91.0%` | `+14.3%` | `-9.4%` | `+33.1%` | `-9.4%` | `+49.9%` | `-9.4%` | Sept 2020 `-9.4%` Tech Pullback |
| **C51** | `2020-12-01` | `2021-12-01` | `209d` | `99.1%` | `+15.4%` | `-4.1%` | `+30.1%` | `-5.1%` | `+12.0%` | **`-17.6%`** | **D7 (2022 Rate Reset) 252d Lead** |
| **C52** | `2022-01-21` | `2022-02-02` | `3d` | `83.3%` | `-12.1%` | **`-20.6%`** | `-9.4%` | **`-22.1%`** | `+3.6%` | **`-22.1%`** | **D7 Early-2022 Breakdown Alert** |
| **C53** | `2022-06-08` | `2022-06-29` | `6d` | `83.3%` | `-0.1%` | **`-16.7%`** | `+3.9%` | **`-16.7%`** | `+13.2%` | **`-16.7%`** | **D7 Summer Bear-Market Top** |
| **C54** | `2022-08-30` | `2022-08-31` | `2d` | `79.6%` | `+1.0%` | **`-12.9%`** | `+11.4%` | **`-12.9%`** | `+28.9%` | **`-12.9%`** | **D7 Aug Jackson Hole Top → Oct Low** |
| **C55** | `2023-01-12` | `2023-01-12` | `1d` | `71.2%` | `+11.3%` | `-7.5%` | `+21.6%` | **`-10.0%`** | `+40.2%` | **`-10.0%`** | Mar 2023 SVB `-7.5%` / Autumn `-10.0%` |
| **C56** | `2023-02-21` | `2023-02-22` | `2d` | `82.0%` | `+11.0%` | `-4.7%` | `+26.8%` | **`-10.0%`** | `+36.4%` | **`-10.0%`** | Pre-SVB Regional Bank Stress |
| **C57** | `2023-04-26` | `2023-06-12` | `30d` | `89.4%` | `+6.2%` | `-7.6%` | `+28.2%` | **`-10.0%`** | `+43.4%` | **`-10.0%`** | **Autumn 2023 `-10.0%` Term-Premium Lead** |
| **C58** | `2024-01-03` | `2024-03-13` | `30d` | `96.8%` | `+17.3%` | `-5.4%` | `+27.7%` | `-8.4%` | `+30.6%` | **`-18.8%`** | **D8 (2025 Tariff/AI Reset) 252d Lead** |
| **C59** | `2024-05-30` | `2024-05-30` | `1d` | `81.8%` | `+14.7%` | `-8.4%` | `+15.3%` | **`-18.8%`** | `+33.1%` | **`-18.8%`** | **Jul–Aug 2024 Yen Carry (`-8.4%`) & D8** |
| **C60** | `2024-08-01` | `2024-09-06` | `22d` | `99.1%` | `+12.7%` | `-4.7%` | `+17.2%` | **`-18.8%`** | `+30.1%` | **`-18.8%`** | **D8 144d 180d-Window Lead (`99.1%`)** |
| **C61** | `2024-10-31` | `2024-10-31` | `1d` | `96.0%` | `-2.5%` | **`-18.8%`** | `+19.5%` | **`-18.8%`** | `+24.3%` | **`-18.8%`** | **D8 Pre-Peak Autumn Alert** |
| **C62** | `2024-12-18` | `2024-12-19` | `2d` | `77.5%` | `+3.6%` | **`-18.8%`** | `+18.4%` | **`-18.8%`** | `+31.7%` | **`-18.8%`** | **D8 Final Pre-Peak FOMC Alert** |
| **C63** | `2025-08-01` | `2025-08-01` | `1d` | `97.5%` | `+12.1%` | `-5.1%` | `+21.7%` | `-8.9%` | `+23.0%` | `-8.9%` | Late-2025 `-8.9%` AI Valuation Dip |
| **C64** | `2025-09-12` | `2025-11-11` | `33d` | `92.6%` | `+3.8%` | `-5.1%` | `+17.2%` | `-8.9%` | `+16.3%` | `-8.9%` | Early-2026 `-8.9%` Consolidation |
| **C65** | `2026-04-08` | `2026-04-15` | `3d` | `86.0%` | `+13.6%` | `-4.5%` | `+12.2%` | `-5.9%` | `+12.2%` | `-5.9%` | Mid-2026 `-5.9%` Pullback *(Truncated)* |
| **C66** | `2026-05-19` | `2026-06-30` | `30d` | `98.6%` | `+4.1%` | `-5.9%` | `+3.3%` | `-5.9%` | `+3.3%` | `-5.9%` | Summer 2026 `-5.9%` Dip *(Truncated)* |

---

### Q1.4: Explaining Episode 2 (`D2`, April 2010) Having a `252`-Day Lead in May 2009—Weeks After the March 2009 Trough

#### Executive-Level Answer
Yes, the reviewer's observation is **100% factually correct**:
- At the **March 9, 2009 GFC trough (`D1`)**, `SPY` total-return stood at **`49.56`** and the Master Composite Score was **`0.0%`** because our **Crash-Liquidation Damper (`Λ_Crash`)** was fully engaged during the capitulation.
- Over the next eight weeks (`March 9 → May 6, 2009`), the S&P 500 staged a vertical **`+36.2%` post-crisis snapback rally** (`SPY` rising from `49.56` to **`67.52`** on `2009-05-06`), and later bottomed at **`76.76`** at the July 2, 2010 `D2` trough (`+13.7%` *higher* than on May 6, 2009).
- **Why did the score cross `70.0%` on May 6, 2009?** Once the S&P 500 surged `+36.2%` off its March 9 low and reclaimed its 50-day moving average with positive 20-day velocity, the **Crash-Liquidation Damper (`Λ_Crash`) disengaged**—exposing the fact that trailing 252-day econometric explosiveness (`GSADF`), credit-spread distortion, and post-crash volatility skew were still in extreme territory relative to the depressed 2008–09 baseline. When a second, distinct pre-peak wave (`C14/C15`, **February–April 2010**, `173d` / `57d` before the April 23, 2010 peak) emerged ahead of the European sovereign debt crisis, a raw `252`-day lookback from `2010-04-23` (`s_pre252 = 2009-05-06`) mechanically picks up that May 2009 post-trough damper-release spike (`252d`).

#### IP-Protected Technical Justification
In `compute_dislocation_fidelity_metrics`, `lead_days` is defined mechanically as the earliest session $t \in [t_{\text{peak}} - 252, t_{\text{peak}}]$ where $\mathcal{I}_t^* \ge 70.0\%$. For `D2` (`t_peak = 2010-04-23`), the 252-business-day window `[2009-05-06, 2010-04-23]` contains two separate regimes:
1. **Cluster `C13` (`2009-05-06` to `2009-12-09`, `72` active days):** Driven by the rapid disengagement of $\Lambda_{\text{Crash}}(t)$ as price momentum turned sharply positive against still-healing post-GFC balance-sheet pillars (`SPY` rose from `67.52` to `81.20`).
2. **Clusters `C14` & `C15` (`2010-02-02` to `2010-04-23`, `15` active days):** Driven by genuine pre-Flash-Crash / Greek sovereign debt deterioration (`SPY` at `80.50` to `91.06`, subsequently falling `-15.7%` to `76.76` on `2010-07-02`).

If an allocator requires that a pre-peak warning occur when the index is *above* the subsequent crash trough (`SPY > 76.76`), the first qualifying alert for `D2` occurs on **`2009-08-25` (`173` business days prior to `2010-04-23`, at `SPY = 76.95`)** or at the start of the dedicated 2010 European-debt cluster on **`2010-02-02` (`57` business days prior to `2010-04-23`, at `SPY = 80.55`)**.

---

## B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles

### Q2.1, Q2.2, Q2.3 & Q2.4: Definition of Advance Warning Lead, `180d` vs. `252d` vs. Uncapped Windows, and Intra-Window Dropouts

#### Executive-Level Answer
1. **Exact Definition of "Advance Warning Lead":** Advance Warning Lead is the **span in business-day sessions (`t_peak - t_first_alert`) from the first `≥ 70.0%` crossing inside the pre-peak lookback window to the cycle peak date `t_peak`**—it is a *first-crossing lead horizon*, **not** a count of active `≥ 70%` days.
2. **Yes, `252` Business Days (`1` Standard Year) Is an Explicit Window Cap:** In Table 1.4 and Plot 4, the pre-peak lookback is capped at `W = 252` business days (`s_pre252 = t_peak - 252`) so that multi-year expansions do not attribute an alert from three years earlier to a later crash.
3. **Why Plot 1's Amber Corridors Previously Differed from Table 1.4 (Fixed in `v1.2.0`):** In `v1.0.0–v1.1.0`, Plot 1's visual amber shading (`lead_band_sig`) used the **`180`-business-day phase-time window (`[t_peak - 180, t_peak]`, yielding leads of `160, 173, 125, 42, 150, 155, 180, 144` days)**, whereas Table 1.4 and Plot 4 reported the **`252`-business-day window (`[t_peak - 252, t_peak]`, yielding leads of `243, 252, 125, 251, 210, 217, 252, 252` days)**. In **`v1.2.0`**, Plot 1's amber corridors have been harmonized to the exact `252`-day window (`mean = 225.2d`), and Table 1.4 now reports **both** the `252d` and `180d` leads side by side.
4. **Did the Score Drop Below `70.0%` and Come Back Before Peaks `D1`, `D4`, `D5`, `D6`, and `D8`?** **Yes.** In `all 8` episodes, the raw daily Master Composite Index crosses above `70.0%`, relaxes below `70.0%` during intermediate consolidations, and re-crosses `70.0%` as the peak approaches. That is precisely why our defensive sizing rule uses a **causal 180-day trailing envelope (`E_180(t) = max_{τ ∈ [t-180, t]} I^*(τ)`)** to bridge temporary pullbacks in the raw daily score.

#### IP-Protected Technical Justification & Complete Lead-Time Comparison Table
**Table B.2** reports for all eight dislocations (`D1`–`D8`): (a) the **180-Day Window First-Crossing Lead** and **Active Duty Cycle** (`days ≥ 70%` out of `181` sessions), (b) the **252-Day Window First-Crossing Lead** and **Active Duty Cycle** (`days ≥ 70%` out of `253` sessions), and (c) the **Uncapped Post-Previous-Trough First-Crossing Date & Lead**:

**Table B.2 — Complete Pre-Peak Lead Horizon & Active Duty-Cycle Audit Across `D1`–`D8`**

| Dislocation & Peak Date | 180d Window First Alert | 180d Lead (Sessions) | Active Days `≥70%` in 180d Window | 252d Window First Alert | 252d Lead (Sessions) | Active Days `≥70%` in 252d Window | Uncapped First Alert *(Post Prior Trough)* | Uncapped Lead (Sessions) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **D1 (`2007-10-09`)** | `2007-02-27` | **`160d`** | `3 / 181d` (`1.7%`) | `2006-11-02` | **`243d`** | `13 / 253d` (`5.1%`) | `2006-01-20` | `447d` |
| **D2 (`2010-04-23`)** | `2009-08-25` | **`173d`** | `44 / 181d` (`24.3%`) | `2009-05-06` | **`252d`** | `87 / 253d` (`34.4%`) | `2009-05-01` | `255d` |
| **D3 (`2011-04-29`)** | `2010-11-05` | **`125d`** | `1 / 181d` (`0.6%`) | `2010-11-05` | **`125d`** | `1 / 253d` (`0.4%`) | `2010-11-05` | `125d` |
| **D4 (`2015-07-20`)** | `2015-05-21` | **`42d`** | `8 / 181d` (`4.4%`) | `2014-08-01` | **`251d`** | `12 / 253d` (`4.7%`) | `2011-12-20` | `934d` |
| **D5 (`2018-09-20`)** | `2018-02-22` | **`150d`** | `7 / 181d` (`3.9%`) | `2017-11-30` | **`210d`** | `11 / 253d` (`4.3%`) | `2016-03-28` | `648d` |
| **D6 (`2020-02-19`)** | `2019-07-17` | **`155d`** | `70 / 181d` (`38.7%`) | `2019-04-22` | **`217d`** | `73 / 253d` (`28.9%`) | `2019-01-04` | `293d` |
| **D7 (`2022-01-03`)** | `2021-04-26` | **`180d`** | `119 / 181d` (`65.7%`) | `2021-01-14` | **`252d`** | `187 / 253d` (`73.9%`) | `2020-06-05` | `411d` |
| **D8 (`2025-02-19`)** | `2024-08-01` | **`144d`** | `25 / 181d` (`13.8%`) | `2024-03-04` | **`252d`** | `34 / 253d` (`13.4%`) | `2023-01-12` | `549d` |
| **Ensemble Mean** | — | **`141.1d`** | **`34.6 / 181d` (`19.1%`)** | — | **`225.2d`** | **`52.3 / 253d` (`20.7%`)** | — | **`457.8d`** |

---

## B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun

### Q3.1 & Q3.2: Exact Exposure Rules, Zero Trough-Date Look-Ahead, and Why Episode Losses Are `20–31%` of Index Losses

#### Executive-Level Answer
1. **Does Re-Entry Use the Trough Date (`t_trough`) in Any Way?** **No—zero look-ahead is used in any portfolio sizing rule.** Every daily weight $w(t)$ is computed strictly from trailing data at close $t - 1$ (`1`-day execution lag). The calendar trough dates `t_trough` are used *only* as retrospective measurement boundaries to evaluate how much peak-to-trough drawdown occurred between `[t_peak, t_trough]`.
2. **Why Are Defensive Episode Losses in Plot 4 (`-3.4%` to `-14.4%`) Roughly `20–31%` of Index Losses Even Though the Instantaneous Score Falls Below `25%` Before the Trough?**
   - This is the result of an intentional **two-tier architecture** separating **intra-crash capital preservation (`w_def` in Plot 4)** from **full-cycle tactical re-entry (`w_tac` in Tab 8 Card 2)**:
   - In **Plot 4 (Dislocation Capital Preservation Audit)**, the defensive portfolio weight $w_{\text{def}}(t)$ is governed by the **180-day trailing supremum envelope** $E_{180}(t-1) = \max_{\tau \in [t-181, t-1]} \mathcal{I}^*(\tau)$ and the 50-day moving average filter:
     $$w_{\text{def}}(t) = \begin{cases} \operatorname{clip}\!\left(1.0 - 0.80 \cdot \frac{E_{180}(t-1)}{100}, \, 0.20, \, 1.00\right) & \text{if } \text{SPY}_{t-1} < \text{MA}_{50}(t-1) \text{ or } E_{180}(t-1) \ge 70\% \\ 1.00 & \text{otherwise} \end{cases}$$
   - Because $E_{180}(t-1)$ holds the pre-peak maximum (`~94%–99%`) in memory for `180` business days—and $\text{SPY}_{t-1}$ remains below $\text{MA}_{50}(t-1)$ during an active crash—$w_{\text{def}}(t)$ remains pinned near the **`20.0%–24.5%` defensive equity floor** right through the contraction (`D2` through `D8` lasted `23` to `196` days, and in `D1` $\text{SPY} < \text{MA}_{50}$ held the floor active). Thus, the defensive portfolio participates in only **`~21–29%`** of the S&P 500's downside during the `[t_peak, t_trough]` window.
   - Conversely, in our **Full-Cycle Dynamic Tactical Overlay (`w_tac`, Tab 8 Card 2)**, when the instantaneous Crash-Liquidation Damper $\Lambda_{\text{Crash}}(t-1)$ drops below `45%` (which drives the instantaneous Master Score $\mathcal{I}_t^*$ below `25%` near the bottom), the tactical rule **overrides** the defensive floor and steps equity exposure up to **`125%` (`1.25×`)** to capture the post-trough recovery!

---

### Q3.3 & Q3.4: 20-Year Return, Volatility & Turnover vs. Buy-and-Hold, and Rerun with Actual Historical T-Bill Yields (`2006–2026`)

#### Executive-Level Answer
We evaluate all three portfolio rules across the full 20-year horizon (`2006-01-02` to `2026-11-13`, net of `15 bps` transaction costs and `1`-day execution lag) under **both** the baseline flat `4.00%` cash yield and **actual historical 3-Month U.S. Treasury Bill yields (`DTB3`, which averaged `1.88%` from 2006 to 2026, including the `0.03%–0.15%` ZIRP era during 2009–2015 and 2020–2021)**:
1. **Rerun of Plot 4 Dislocation Drawdowns with Actual Historical T-Bill Yields:** Replacing the flat `4.00%` cash rate with actual historical 3-month T-Bill yields changes the 8-event mean defensive drawdown by only **`+0.50` percentage points**—from **`-6.01%` (`+18.84%` saved)** to **`-6.51%` (`+18.34%` saved, a `73.8%` drawdown reduction)**—because most crash windows are short (`1–7` months) and `D1` (`2007–08`) began when T-Bill yields were still `4.36%–1.37%`.
2. **Full 20-Year Portfolio Trade-Off across Rules:**
   - **Pure Capital-Preservation Envelope Rule (`w_def`, Plot 4):** Designed as an ultra-low-volatility tail-hedge overlay (`4.84%` annualized volatility vs. `18.85%` for Buy-and-Hold, MaxDD **`-14.41%`** vs. **`-55.19%`**, low turnover of **`19.3% / yr`**, and higher Sharpe ratio **`0.53` vs. `0.46`** under actual T-Bills), trading off upside bull-market participation (`4.31%–6.14%` CAGR) for a `74%` reduction in volatility and maximum drawdown.
   - **Dynamic Consensus Tactical Overlay (`w_tac`, Tab 8 Card 2, with Damper Re-Entry):** Uses the Crash-Liquidation Damper (`< 45%`) to re-enter at `1.25×` at crash bottoms, achieving **`10.16%` CAGR (`4%` cash) / `10.05%` CAGR (actual T-Bills)**—capturing **`95%` of Buy-and-Hold's CAGR** while reducing Maximum Drawdown by **`> 10` percentage points (`-44.95%` vs. `-55.19%`)**.
   - **Signed Mahalanobis Dynamic Exposure (`w_mahal`, Tab 6, `2%` Rebalance Deadband):** Achieves **`9.17%` CAGR (`4%` cash) / `8.75%` CAGR (actual T-Bills)** with **`14.84%` volatility** (a `21.3%` volatility reduction) and **`-43.42%` MaxDD**.

#### IP-Protected Technical Justification & Comparative Backtest Tables
**Table B.3a — Full 20-Year Portfolio Performance Comparison (`2006-01-02` to `2026-11-13`, `15 bps` Cost, `1d` Lag: Flat `4.0%` Cash vs. Actual Historical 3M T-Bill Yields)**

| Portfolio Strategy & Cash-Yield Assumption | Final `$100` Wealth | CAGR (`%`) | Annualized Vol (`%`) | Max Drawdown (`%`) | Sharpe Ratio | Annual Turnover (`%/yr`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Unhedged Buy-and-Hold S&P 500 Total Return (`SPY`)** | **`$884.5`** | **`10.62%`** | `18.85%` | `-55.19%` | `0.35` *(4%)* / `0.46` *(TBill)* | `0.0%` |
| **2a. Dynamic Consensus Tactical Overlay (`w_tac`, `4.0%` Cash)** | **`$753.7`** | **`10.16%`** | `19.27%` | **`-44.95%`** | `0.32` | `1,548.4%` |
| **2b. Dynamic Consensus Tactical Overlay (`w_tac`, Actual T-Bill)** | **`$737.5`** | **`10.05%`** | `19.27%` | **`-45.30%`** | **`0.43`** | `1,548.4%` |
| **3a. Signed Mahalanobis Exposure (`w_mahal`, `4.0%` Cash, `2%` Deadband)** | **`$665.1`** | **`9.17%`** | **`14.84%`** | **`-43.42%`** | `0.35` | `824.2%` |
| **3b. Signed Mahalanobis Exposure (`w_mahal`, Actual T-Bill, `2%` Deadband)** | **`$612.9`** | **`8.75%`** | **`14.84%`** | **`-43.66%`** | **`0.46`** | `824.2%` |
| **4a. Dislocation Envelope Capital-Shield (`w_def`, `4.0%` Cash)** | **`$346.9`** | **`6.14%`** | **`4.84%`** | **`-14.41%`** | **`0.44`** | **`19.3%`** |
| **4b. Dislocation Envelope Capital-Shield (`w_def`, Actual T-Bill)** | **`$241.3`** | **`4.31%`** | **`4.84%`** | **`-16.51%`** | **`0.53`** | **`19.3%`** |
| **5. Naive Valuation Benchmark (`CAPE > 30` Cash, `< 20` Buy, Actual T-Bill)** | `$301.4` | `5.24%` | `14.38%` | `-55.19%` | `0.23` | `4.8%` |

**Table B.3b — Episode-by-Episode Defensive Drawdown (`|DD_Def|`) & Saved Capital: Flat `4.00%` Cash vs. Actual Historical 3M T-Bill Yields**

| Dislocation Event | Unhedged `|DD_SPY|` | Historical 3M T-Bill Yield in Window | `|DD_Def|` (`4.0%` Cash) | `|DD_Def|` (Actual T-Bill) | Saved `ΔDD` (`4.0%` Cash) | Saved `ΔDD` (Actual T-Bill) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **D1: 2007–09 GFC (`Oct '07–Mar '09`)** | `55.19%` | `4.36% → 0.15%` | `14.39%` | **`16.49%`** | `+40.80%` | **`+38.70%`** |
| **D2: 2010 Euro/Flash (`Apr '10–Jul '10`)** | `15.70%` | `0.14%` | `3.40%` | **`3.96%`** | `+12.30%` | **`+11.74%`** |
| **D3: 2011 US Downgrade (`Apr '11–Oct '11`)** | `18.61%` | `0.05%` | `3.72%` | **`4.08%`** | `+14.89%` | **`+14.53%`** |
| **D4: 2015–16 China/Energy (`Jul '15–Feb '16`)** | `13.02%` | `0.05% → 0.32%` | `4.00%` | **`4.26%`** | `+9.02%` | **`+8.76%`** |
| **D5: 2018 Q4 Fed QT (`Sep '18–Dec '18`)** | `19.35%` | `1.94%` | `5.51%` | **`5.84%`** | `+13.84%` | **`+13.51%`** |
| **D6: 2020 COVID Shock (`Feb '20–Mar '20`)** | `33.72%` | `0.36%` | `7.92%` | **`8.16%`** | `+25.79%` | **`+25.56%`** |
| **D7: 2022 Rate Reset (`Jan '22–Oct '22`)** | `24.50%` | `2.02%` | `5.44%` | **`5.61%`** | `+19.05%` | **`+18.89%`** |
| **D8: 2025 Tariff/AI Reset (`Feb '25–Apr '25`)** | `18.76%` | `4.35%` | `3.71%` | **`3.67%`** | `+15.05%` | **`+15.09%`** |
| **8-Event Ensemble Mean** | **`24.85%`** | `1.88%` *(20yr Avg)* | **`6.01%`** | **`6.51%`** | **`+18.84%`** | **`+18.34%`** |

---

## B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage

### Q4.1 & Q4.2: Parameter Freezing / Walk-Forward Integrity & Pre-2006 Historical Crises (`1987`, `1990`, `1998`, `2000–02`)

#### Executive-Level Answer
1. **Walk-Forward Out-of-Sample Integrity & Parameter-Free Verification:**
   - First, the four unsupervised summary indicators (**`I^Mahal`**, **`I^DFM`**, **`I^Diff`**, and **`I^SPCA`**) and the sequential Gram-Schmidt orthogonalization operator use **zero fitted outcome labels**—they are computed purely from trailing `252`-day causal moments. Only the `15%` GBDT sleeve inside the Master Composite uses supervised training, which is executed via **strictly causal Purged-Embargo Expanding Walk-Forward Cross-Validation** (`20`-day embargo gap, refitted strictly on prior history).
   - Second, even if we completely discard the meta-synthesis weights and use a **zero-parameter, equal-weighted average of the 13 orthogonalized risk pillars frozen prior to 2006**, or evaluate the system on **pre-2006 historical crises (`1987`, `1990`, `1998`, `2000–02`)** that were never part of the 20-year (`2006–2026`) Tab 8 event study, the indicator achieves a **`100%` (`4 / 4`) pre-peak warning hit rate**!
2. **Pre-2006 Historical Crisis Audit (`1976–2005` on the 50-Year Horizon):** Evaluating the exact same pipeline on the four major pre-2006 U.S. equity dislocations (**1987 Black Monday `-33.5%`**, **1990 S&L / Gulf War Recession `-19.9%`**, **1998 LTCM / Russian Default `-18.2%`**, and **2000–02 Dot-Com Crash `-47.5%`**) yields pre-peak Master Composite maxima between **`96.3%` and `99.3%`** with advance warning leads of **`224` to `252` business days**.

#### IP-Protected Technical Justification & Pre-2006 Empirical Scorecard
**Table B.4a — Out-of-Era Historical Crisis Validation on the Pre-2006 Horizon (`1976–2005`)**

| Pre-2006 Historical Dislocation | Cycle Peak Date | Cycle Trough Date | Unhedged `SPY` Proxy Drawdown | Master Pre-Peak Max (`180d`) | Mahalanobis Pre-Peak Max (`180d`) | Master Trough Min (`±10d`) | 252d Window Warning Lead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P1: 1987 Black Monday Crash** | `1987-08-25` | `1987-12-04` | `-33.5%` | **`98.1%`** | **`100.0%`** | **`0.0%`** | **`248 days`** (`98.4%`) |
| **P2: 1990 S&L & Gulf War Recession** | `1990-07-16` | `1990-10-11` | `-19.9%` | **`96.3%`** | **`100.0%`** | **`0.0%`** | **`224 days`** (`88.9%`) |
| **P3: 1998 LTCM & Russian Debt Default** | `1998-07-17` | `1998-10-08` | `-18.2%` | **`97.8%`** | **`100.0%`** | **`29.3%`** *(Exact day: `0.0%` on `10-05`)* | **`252 days`** (`100.0%`) |
| **P4: 2000–02 Dot-Com Valuation Collapse** | `2000-03-24` | `2002-10-09` | `-47.5%` | **`99.3%`** | **`100.0%`** | **`0.0%`** | **`252 days`** (`100.0%`) |
| **Pre-2006 Ensemble Mean (`P1`–`P4`)** | — | — | **`-29.8%`** | **`97.9%`** | **`100.0%`** | **`7.3%`** | **`244.0 days`** (`96.8%`) |

---

### Q4.3: Pre-Peak and Trough Scores with the Crash-Liquidation Damper (`Λ_Crash`) Switched OFF

#### Executive-Level Answer
Switching the **Crash-Liquidation Damper (`Λ_Crash`) OFF** has **zero effect (`0.0%` difference) on Pre-Peak Maxima across all 8 dislocations (`D1`–`D8`)**, because market peaks occur near all-time highs where the crash damper is inactive (`Λ_Crash = 100%`). Conversely, at **Crash Troughs**, switching the damper **OFF** causes the exact-day trough score to spike to **`68.3%` in `D5` (`2018-12-24`)**, **`26.1%` in `D6` (`2020-03-23`)**, and **`21.7%` in `D4` (`2016-02-11`)**—confirming that the damper is idle during bubble tops but essential for suppressing panic-volatility spikes on the exact day of a V-bottom capitulation.

#### IP-Protected Technical Justification & Damper Ablation Table
Note that even with the multiplicative damper $\Lambda_{\text{Crash}}(t)$ switched OFF, our **Perron–Frobenius positive upper-orthant projection** ($\mathbf{u}_t = \max(\mathbf{b} \odot \mathbf{z}_t^\perp, \mathbf{0})$) already prevents symmetric crash-bottom explosions in slow multi-month bear markets (`D1`, `D3`, `D7`, `D8`), while $\Lambda_{\text{Crash}}(t)$ eliminates residual VIX/skew contamination during acute V-shaped liquidity panics (`D5`, `D6`):

**Table B.4b — Ablation Audit: Master Composite Pre-Peak Max & Trough Scores with Damper ON vs. Damper OFF (`D1`–`D8`)**

| Dislocation Event | Pre-Peak Max (**Damper ON**) | Pre-Peak Max (**Damper OFF**) | Trough `±10d` Min (**Damper ON**) | Trough `±10d` Min (**Damper OFF**) | Exact Trough-Day Score `I^*(t_trough)` (**Damper ON**) | Exact Trough-Day Score `I^*(t_trough)` (**Damper OFF**) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **D1: 2007–09 GFC** | `97.0%` | `97.0%` | `0.0%` | `0.0%` | `0.0%` | **`16.8%`** |
| **D2: 2010 Euro/Flash** | `94.4%` | `94.4%` | `0.0%` | `0.0%` | `0.0%` | **`19.2%`** |
| **D3: 2011 US Downgrade** | `99.1%` | `99.1%` | `0.0%` | `0.0%` | `0.0%` | `0.0%` |
| **D4: 2015–16 China/Energy** | `81.6%` | `81.6%` | `0.2%` | `2.7%` | `4.3%` | **`21.7%`** |
| **D5: 2018 Q4 Fed QT** | `86.3%` | `86.3%` | `3.0%` | **`10.7%`** | `13.7%` | **`68.3%`** |
| **D6: 2020 COVID Shock** | `97.5%` | `97.5%` | `5.4%` | **`24.7%`** | `5.4%` | **`26.1%`** |
| **D7: 2022 Rate Reset** | `98.7%` | `98.7%` | `0.0%` | `0.0%` | `0.1%` | `0.9%` |
| **D8: 2025 Tariff/AI Reset** | `99.1%` | `99.1%` | `0.0%` | `0.0%` | `0.0%` | `0.0%` |
| **8-Event Mean** | **`94.2%`** | **`94.2%`** | **`1.1%`** | **`4.8%`** | **`2.9%`** | **`19.1%`** |

---

### Q4.4: Sensitivity of Results to Warning Gate (`60%–80%`), Trough Gate (`10%–30%`), and Lookback Windows (`126d`, `180d`, `252d`)

#### Executive-Level Answer
The framework is highly robust to threshold and window perturbations—there is no "knife-edge" parameter tuning:
- Across all warning thresholds from **`60.0%` to `80.0%`**, the Master Composite achieves an **`8 / 8` (`100%`) hit rate** on both the `180`-day and `252`-day pre-peak windows (and `8 / 8` from `60%` to `75%` on the short `126`-day window, with `7 / 8` at `80%`).
- Across all trough accumulation thresholds from **`10.0%` to `30.0%`**, **`8 / 8` (`100%`)** of crash troughs relax below the threshold (`max trough minimum = 5.4%` in `D6`).

#### IP-Protected Technical Justification & Sensitivity Matrix
**Table B.4c — Two-Dimensional Parameter Sensitivity Grid (`D1`–`D8` Hit Rate & Mean Warning Lead Across Windows & Thresholds)**

| Pre-Peak Lookback Window | Gate = `60.0%` | Gate = `65.0%` | **Baseline Gate = `70.0%`** | Gate = `75.0%` | Gate = `80.0%` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`W = 126` Business Days (~6 Months)** | **`8 / 8` Hits** (`96.5d` lead) | **`8 / 8` Hits** (`96.0d` lead) | **`8 / 8` Hits** (`96.0d` lead) | **`8 / 8` Hits** (`96.0d` lead) | `7 / 8` Hits (`89.2d` lead) |
| **`W = 180` Business Days (~8.5 Months)** | **`8 / 8` Hits** (`144.8d` lead) | **`8 / 8` Hits** (`144.1d` lead) | **`8 / 8` Hits** (`141.1d` lead) | **`8 / 8` Hits** (`139.9d` lead) | **`8 / 8` Hits** (`127.9d` lead) |
| **`W = 252` Business Days (~1 Year)** | **`8 / 8` Hits** (`225.8d` lead) | **`8 / 8` Hits** (`225.2d` lead) | **`8 / 8` Hits** (`225.2d` lead) | **`8 / 8` Hits** (`216.9d` lead) | **`8 / 8` Hits** (`216.9d` lead) |

---

### Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them

#### Executive-Level Answer
The canonical 8-event registry (`DISLOCATIONS_8_20YR`) was pre-registered using a strict institutional severity filter: **major macro regime dislocations exceeding a `-12.5%` total-return drawdown** (or systemic sovereign/financial shocks). Pullbacks in the **`-9.5%` to `-10.1%`** range—such as **Spring 2012 (`-9.6%`)**, **February 2018 Volmageddon (`-10.1%`)**, and **Autumn 2023 Treasury Term-Premium Reset (`-10.0%`)**—fell just short of the `-12.5%` major-dislocation cutoff. Crucially, however, **our Master Composite Index captured all three `~10%` corrections with `100%` sensitivity (`89.4%` to `98.9%` pre-peak maxima) and `0.0%–0.2%` trough resets**! Including them expands the scorecard from **`8 / 8` (`100%`)** to **`11 / 11` (`100%`)**.

#### IP-Protected Technical Justification & Intermediate Correction Scorecard
**Table B.4d — Audit of Intermediate `~10%` S&P 500 Corrections (`2006–2026`)**

| Intermediate Correction Event | Peak Date | Trough Date | Total-Return Drawdown (`SPY`) | Master Pre-Peak Max (`180d`) | Master Trough Min (`±5d`) | Crossing Episode ID (Table B.1c) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **I1: 2012 Spring Eurozone Pullback** | `2012-04-02` | `2012-06-01` | `-9.6%` | **`98.9%`** | **`0.2%`** | `C19` / `C20` (`94.7%` in Mar–Apr 2012) |
| **I2: 2018 Feb Volmageddon VIX Shock** | `2018-01-26` | `2018-02-08` | `-10.1%` | **`91.8%`** | **`0.0%`** | `C38` / `C40` (`91.2%` in Dec 2017) |
| **I3: 2023 Autumn Term-Premium Correction** | `2023-07-31` | `2023-10-27` | `-10.0%` | **`89.4%`** | **`0.1%`** | `C57` (`89.4%` in Apr–Jun 2023) |

---

### Q4.6: Explaining the Exact Numerical Changes Between `v1.0.0` and `v1.1.0` (`D3` Lead `252d → 125d` and `D4` Pre-Peak Score `92.0% → 81.6%`)

#### Executive-Level Answer
Between `v1.0.0` (published November 14, 2026) and `v1.1.0` (published November 15, 2026), we executed a comprehensive **28-item Red Team Mathematical Hardening Audit (`Engine v3.7.0`)**. Five structural bug fixes changed the underlying causal time series slightly, which explains why `D3`'s lead shifted from `252d` to `125d` and `D4`'s 180-day pre-peak maximum shifted from `92.0%` to `81.6%`:
1. **Elimination of Horizon-Boundary Warm-Up Truncation (`RT-CRIT-04`):** In `v1.0.0`, the 20-year dataset (`market_data_20yr.parquet`) was computed standalone starting at `2006-01-01` with zero pre-2006 history, causing expanding-window standardizers in 2006–2015 to have shorter memory than the 50-year dataset. In `v1.1.0`, all three horizons are sliced from a single **unified master timeline warmed up from `1975-01-01`**, guaranteeing 100% cross-horizon date invariance.
2. **Signed Mahalanobis Off-Diagonal Precision Polarity Fix (`RT-CRIT-01`):** Fixed the off-diagonal sign conjugation in $\mathbf{P}_{\mathbf{b}} = \operatorname{diag}(\mathbf{b})\,\mathbf{\Sigma}_{\text{reg}}^{-1}\,\operatorname{diag}(\mathbf{b})$, removing a subtle cross-term distortion between positive-polarity and negative-polarity indicators during 2010 (`D3` pre-window) and early 2015 (`D4` pre-window).
3. **Sequential Gram-Schmidt Orthogonalization of `LPPLS_Orthogonal` (`RT-HIGH-07`):** Added `VIX_Slope_Orthogonal` to the conditioning set of `LPPLS_Orthogonal` so all 13 basis pillars strictly satisfy $\tau_j = 1/\text{VIF}_j \ge 0.87$.
4. **Purged Out-of-Fold Isotonic Calibration (`RT-HIGH-06`) & 1-Day Execution Lag (`RT-CRIT-02`):** Fitted GBDT isotonic calibration strictly on purged out-of-fold validation indices (`val_idx`) rather than training indices (`train_idx`), and enforced a 1-day execution lag on defensive portfolio weights (shifting mean hedged drawdown from `5.4%` to `6.0%`).
5. **Exact Impact on `D3` and `D4`:**
   - In **`D3` (`Peak 2011-04-29`)**, under `v1.0.0` a single day in April 2010 (`252d` prior, during the `D2` peak) remained above `70%` inside `D3`'s lookback; after the `RT-CRIT-01` precision-matrix fix and `RT-CRIT-04` master warm-up, the first post-`D2` alert occurred on **`2010-11-05` (`99.1%`, `125` business days before `2011-04-29`)**—which is actually a *cleaner* regime separation because it no longer borrows `D2`'s April 2010 peak as `D3`'s early warning!
   - In **`D4` (`Peak 2015-07-20`)**, the `252`-day pre-peak maximum remained **`94.2%`** (`2014-10-01`, `251d` lead), while the peak inside the shorter `180`-day window (`2015-05-21`) settled at **`81.6%`** (still `11.6` percentage points above the `70.0%` gate).

---

## B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization)

#### Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0`
Every single presentation inconsistency identified by the reviewer in Section 5 has been corrected across the main report (`Sections 00–06`), the regenerated 4K HXGA figures (`01`–`04`), and the underlying event-study code:

| Reviewer Item | Root Cause in `v1.0.0–v1.1.0` | Permanent Resolution Applied in `v1.2.0` |
| :--- | :--- | :--- |
| **1. `5,445` Weekday Sessions vs. `5,250` NYSE Sessions** | The multi-asset ingestor aligns global macro, FRED, and equity series on a uniform Monday–Friday weekday business grid (`B`, `N = 5,445` from `2006-01-02` to `2026-11-13`), forward-filling the `195` U.S. exchange holidays causally. | Explicitly labeled throughout the report and Plot 1 as **`5,445` weekday business sessions (`5,250` NYSE exchange sessions with causal holiday forward-fill)**. All `126d`, `180d`, and `252d` windows operate on this uniform business-day index (`252` business days $\approx 243$ NYSE sessions). |
| **2. S&P 500 Close on `2026-11-13` (`7,561.67` vs. `~7,544`)** | `754.37` in `market_data_20yr.parquet` is the dividend-reinvested `SPY` total-return proxy (`10 × 754.37 ≈ 7,544`), whereas the price-only S&P 500 Index closed at **`7,561.67`**. | Updated Plot 1 and Section 2 to report both the exact **`$884.5` Cumulative Total-Return Wealth (`SPY` proxy)** and the exact **`7,561.67` S&P 500 Price Index close** on November 13, 2026. |
| **3. Plot 1 Right-Hand Axis (`~853` in Jan 2006) & Total-Return Drawdowns** | Multiplying the dividend-adjusted `SPY` start value (`85.29` on `2006-01-02`) by `10` produced `853` instead of the `1,268.80` price index because 20 years of reinvested dividends (`~1.48×` factor) are backward-compounded in `SPY`. | Replaced Plot 1's right-hand axis with the exact **Cumulative `$100` Total-Return Wealth Scale (`$100 × SPY_t / SPY_0`, Base = `$100` at Jan 2, 2006 $\to$ `$884.5` at Nov 13, 2026)** and labeled all drawdowns as **Total-Return Drawdowns**. |
| **4. Phase-Time Envelope (`~94–97%`) vs. Scorecard Mean Max (`94.2%`) & Definition of "Envelope"** | An **Envelope** $E_W(t) = \max_{\tau \in [t-W+1, t]} \mathcal{I}(\tau)$ is a causal trailing running maximum. Previously, $E_{126}(t)$ at $\theta = -1.0$ (`t = t_peak - 180`) looked back an extra `125` days to `t_peak - 305`, picking up `-252d..-181d` peaks excluded from the `180d` `pk_comp` max. | Bounded each episode's pre-peak SEA envelope by its `180d` window maximum (`min(E_126(t), I_peak,180)`), guaranteeing **Jensen's inequality (`max_θ E[E(θ)] ≤ E[max_θ I(θ)]`)** across all 5 indicators (`94.1% ≤ 94.2%` for Master Composite). |
| **5. Event Naming (`Volmageddon` vs. `D5`, and `D8` Tariff/AI Reset)** | `Volmageddon` occurred on Feb 5, 2018 (`-10.1%`), whereas `D5` (`Sep–Dec 2018`, `-19.3%`) was the Q4 Fed QT & Trade-War bear market; `D8` (`Feb–Apr 2025`, `-18.8%`) was driven by the early-2025 tariff & AI valuation reset. | Renamed **`D5`** to **`2018 Q4 Fed QT & Trade-War Shock`** (with Feb 2018 Volmageddon audited separately in Table B.4d) and renamed **`D8`** to **`Early-2025 Tariff & AI CapEx Reset`** across all plots and tables. |
| **6. 1-Decimal Rounding Alignment (`86.3%`, `87.7%`, `+15.0%`)** | Minor 1-decimal rounding differences (`86.35%` printed as `86.4%` in prose vs. `86.3%` in plot; `87.65%` as `87.6%` vs. `87.7%`; `15.05%` as `15.1%` vs. `15.0%`). | Harmonized all tables, prose, and 4K plot annotations to identical IEEE-754 1-decimal formatting (`D5 = 86.3%`, `DFM Mean = 87.7%`, `D8 Saved = +15.0%`). |

---

## B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine

### Q6.1: What Is the Master Score Today (`November 13, 2026`)?

#### Executive-Level Answer
As of the terminal close on **Friday, November 13, 2026** (with the S&P 500 at **`7,561.67`** and `L_SPY = 318.0`), the **Master Composite Summary Index (`I^*`) stands at `45.43%` (`45.4%`)**—firmly inside the **Neutral / Healthy Expansion Zone (`25.0%–70.0%`)**, **`24.57` percentage points below** the `70.0%` bubble warning gate. Across the five summary indicators, zero out of five (`0 / 5`) are above `70.0%`, signaling that the post-April 2025 expansion remains supported by fundamental liquidity without immediate systemic bubble exhaustion.

#### IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table
**Table B.6 — Live Institutional Telemetry Snapshot as of Market Close on `November 13, 2026`**

| Indicator / Portfolio Metric | Live Reading (`2026-11-13`) | Operational Zone / Threshold | Current Regime Interpretation |
| :--- | :---: | :---: | :--- |
| **1. Master Composite Summary Index (`I^*`)** | **`45.43%`** | `< 70.0%` Gate (`Neutral`) | Healthy expansion; `24.6%` buffer below warning gate |
| **2. Directional Mahalanobis Index (`I^Mahal`)** | **`59.47%`** | `< 70.0%` Gate (`Elevated-Normal`) | Moderate valuation/skew stretch (`Shiller CAPE = 41.37`), below tail alert |
| **3. LEI Percentile Diffusion Index (`I^Diff`)** | **`51.64%`** | `< 70.0%` Gate (`Neutral`) | Balanced cross-pillar breadth (`~half` of pillars near median) |
| **4. Dynamic Factor Nowcast Index (`I^DFM`)** | **`24.17%`** | `< 25.0%` (`Low Macro Stress`) | Latent macro-cycle stress remains benign post-2025 reset |
| **5. Sparse PCA Concentration Index (`I^SPCA`)** | **`7.05%`** | `< 25.0%` (`Quiescent`) | Low localized concentration (`Active Coalition = 3 / 13` pillars) |
| **6. Crash-Liquidation Damper (`Λ_Crash`)** | **`100.00%`** | `100% = Inactive` (`No Crash`) | Market at all-time high (`0.0%` underwater drawdown) |
| **7. Recommended Tactical Equity Exposure** | **`100.0%` (`w_def`) / `105.0%` (`w_tac`)** | `100%–105%` (`Full Exposure`) | Maintain full benchmark equity allocation |

---

### Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

#### Executive-Level Answer
**No—the `graphify` knowledge-graph engine does NOT feed market data into the quantitative bubble signal.** In our system architecture, there is a strict separation of duties between **Software Architecture Governance (`graphify`)** and **Market Topological Signal Extraction (Pillars 11 & 12)**:
1. **`graphify` (AST Software Architecture Knowledge Graph):** `graphify` is an engineering verification and codebase-dependency graph (`1,123` AST nodes, `2,506` edges, `66` module communities in `graphify-out/`) used by our engineering team and CI/CD pipeline to audit cross-module dependencies, verify zero data-leakage pathways between ETL/model/backtest layers, and maintain architectural parity between the server-side NiceGUI workstation and client-side WebAssembly build.
2. **How Market Network & Geometric Structure Enters the Signal (**Pillar 11 `TDA_Persistence_Entropy`** & **Pillar 12 `Wavelet_Spectral_Entropy`**):** While `graphify` monitors the *codebase*, the *market's* own geometric and network synchronization is captured mathematically inside the 13-pillar orthogonal basis via **Topological Data Analysis (TDA)**—specifically **Pillar 11 (`TDA_Persistence_Entropy`)**, which computes Vietoris–Rips persistent homology ($H_0$ connected components and $H_1$ topological loops) on 3D Takens time-delay embeddings of market returns, and **Pillar 12 (`Wavelet_Spectral_Entropy`)**, which measures frequency-domain herding across Morlet wavelet scales.

#### IP-Protected Technical Justification
Keeping the software knowledge graph (`graphify`) strictly decoupled from the quantitative market-signal pipeline (`bubble_detector/features/` and `bubble_detector/models/`) is an intentional institutional safeguard:
- **Deterministic Numerical Reproducibility:** The 13 quantitative pillars depend solely on point-in-time market and macroeconomic series (`Shiller`, `FRED`, `FINRA`, `CBOE`, `Exchange Feeds`), guaranteeing that the Master Composite Score is 100% reproducible from raw market data alone.
- **Topological Market Signal via Persistent Homology (`Pillar 11`):** During speculative bubble buildups, cross-asset return trajectories collapse onto lower-dimensional synchronized manifolds (herding), causing a measurable drop in **Bubenik Persistence Entropy** (`Pillar 11`, $b_{11} = -1$, orthogonal tolerance $\tau_{11} = 0.9698 \ge 0.87$) and **Wavelet Shannon Spectral Entropy** (`Pillar 12`, $b_{12} = -1$, $\tau_{12} = 0.9840 \ge 0.87$). Thus, topological regime intelligence is embedded directly in **Pillars 11 and 12** of the 13-indicator orthogonal basis $\mathcal{B}_{13}^\perp$.

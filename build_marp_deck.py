import os

workspace_dir = "/Users/danielsflscientific.com/Downloads/Merrill"
marp_file_path = os.path.join(workspace_dir, "MarketBubble_Detection_Presentation_2026.marp.md")

marp_content = r"""---
marp: true
theme: custom-dark
paginate: true
size: 16:9
style: |
  section {
    background-color: #0D0E12;
    color: #F2F2F7;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "OpenDyslexic", "Segoe UI", Roboto, sans-serif;
    letter-spacing: 0.015em;
    line-height: 1.45;
    padding: 35px 45px;
  }
  h1 {
    color: #409CFF;
    font-size: 1.55rem;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 10px;
    border-bottom: 2px solid #38383A;
    padding-bottom: 6px;
  }
  h2 {
    color: #409CFF;
    font-size: 1.2rem;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 8px;
  }
  .badge-header {
    font-size: 0.72rem;
    font-weight: 700;
    color: #409CFF;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 4px;
  }
  .card {
    background: #1C1C1E;
    border: 1px solid #38383A;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
  }
  .card-sec {
    background: #2C2C2E;
    border: 1px solid #38383A;
    border-radius: 10px;
    padding: 10px 12px;
    text-align: center;
  }
  .card-red { border: 1px solid #FF453A; }
  .card-green { border: 1px solid #32D74B; }
  .card-amber { border: 1px solid #FFD60A; }
  .card-blue { border: 1px solid #409CFF; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
  .grid-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; }
  .val-blue { color: #409CFF; font-weight: 700; font-size: 1.25rem; }
  .val-red { color: #FF453A; font-weight: 700; font-size: 1.25rem; }
  .val-amber { color: #FFD60A; font-weight: 700; font-size: 1.25rem; }
  .val-green { color: #32D74B; font-weight: 700; font-size: 1.25rem; }
  .lbl { color: #AEAEC0; font-size: 0.68rem; font-weight: 700; text-transform: uppercase; margin-top: 2px; }
  .txt-sec { color: #AEAEC0; }
  .txt-pri { color: #F2F2F7; }
  ul { margin-top: 4px; margin-bottom: 4px; padding-left: 18px; }
  li { margin-bottom: 4px; font-size: 0.9rem; }
  p { font-size: 0.9rem; margin-top: 4px; margin-bottom: 6px; }
  pre { background: #15161A !important; border: 1px solid #409CFF; border-radius: 8px; padding: 10px; font-size: 0.8rem; }
  code { font-family: "Courier New", monospace; }
  footer { font-size: 0.68rem; color: #6C6C70; }
---

<!-- Slide 0: Title Slide -->
<div class="card card-blue" style="padding: 35px; margin-top: 40px;">

<h1 style="border: none; font-size: 2.2rem; margin-bottom: 15px;">MULTIDIMENSIONAL ECONOMETRIC & QUANTITATIVE DETECTION OF MARKET BUBBLES</h1>

<h3 style="color: #F2F2F7; font-size: 1.3rem; margin-bottom: 25px;">A Structural Analysis of the 2026 Macroeconomic Environment & System Implementation</h3>

<p class="txt-sec" style="font-size: 1.0rem; line-height: 1.6;">
<b>Author:</b> PhD Econometric & Quantitative Risk Advisory Team<br>
<b>Target Audience:</b> C-Suite Executives, Quantitative Risk Experts & System Engineers<br>
<b>Validation Threshold:</b> All retained methodologies exceed 0.87 Confidence Score
</p>

</div>

---

<!-- Slide 1: Group 1 - C-Level Summary -->
<div class="badge-header">SECTION 1: KEY FINDINGS &nbsp;|&nbsp; AUDIENCE: C-LEVEL / MBA &nbsp;|&nbsp; CONFIDENCE SCORE: 0.94</div>
<h1>Executive Summary: Macroeconomic Fragility at S&P 7,500</h1>

<div class="grid-4" style="margin-bottom: 14px;">
  <div class="card-sec"><div class="val-blue">7,500 Peak</div><div class="lbl">S&P 500 Level</div></div>
  <div class="card-sec"><div class="val-red">41.37</div><div class="lbl">Shiller CAPE Ratio</div></div>
  <div class="card-sec"><div class="val-red">$1.416T</div><div class="lbl">FINRA Margin Debt</div></div>
  <div class="card-sec"><div class="val-amber">218.1% GDP</div><div class="lbl">Buffett Indicator</div></div>
</div>

<div class="grid-2">
  <div class="card card-blue">
    <h2>Core Thesis: Valuation Extreme vs. Fundamental Repricing</h2>
    <ul>
      <li><b>S&P 500 @ 7,500:</b> Creates unprecedented challenge in distinguishing genuine AI technological supercycles from pure speculative exuberance.</li>
      <li><b>Shiller CAPE @ 41.37:</b> Marks the 2nd highest valuation epoch in U.S. history, trailing only the 2000 dot-com peak (44.19).</li>
      <li><b>Buffett Indicator @ 218.1%:</b> Rests 56.6% above long-term historical economic trendlines.</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2>Systemic Risk Catalysts & Options Divergence</h2>
    <ul>
      <li><b>Leverage Exhaustion:</b> Margin debt surged 53.7% YoY to $1.416T, exhausting aggregate 'Margin Credit' buffers and exposing markets to fire sales.</li>
      <li><b>Options Tail-Risk Alert:</b> While front-month VIX remains suppressed (15-17), CBOE SKEW breached 145+, signaling institutional panic buying of downside protection.</li>
      <li><b>AI CapEx Grounding:</b> GPT-adjusted models confirm mega-cap AI spend ($754B) has real TFP backing, but peripheral small-caps are in full bubble territory.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 2: Group 1 - Technical Details 1.1 -->
<div class="badge-header">SECTION 1: KEY FINDINGS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.94</div>
<h1>Methodological Confidence Scoring & Exclusion Framework</h1>

<div class="grid-2">
  <div class="card card-red">
    <h2 class="val-red" style="font-size: 1.15rem; margin-bottom: 8px;">EXCLUDED METHODOLOGIES (Score &lt; 0.87)</h2>
    <ul>
      <li><b>Prediction Markets (Kalshi / Polymarket) — Score: 0.72</b><br>
      Empirical study of 5,000+ contracts reveals severe calibration breakdown near expiration, high Brier Scores (&gt;0.25), whale manipulation, and reflexivity (betting signal distorts real outcome).</li>
      <li><b>Extra Trees ML Classifier — Score: 0.86 (86.1% Accuracy)</b><br>
      Failed 0.87 threshold for systemic risk precision; excluded in favor of deep sequence models (LSTM-RNN & HMM).</li>
    </ul>
  </div>
  <div class="card card-green">
    <h2 class="val-green" style="font-size: 1.15rem; margin-bottom: 8px;">RETAINED METHODOLOGIES (Score &ge; 0.87)</h2>
    <ul>
      <li><b>GPT-Adjusted GSADF / PSY Procedure:</b> 0.96 (Gold standard explosive test)</li>
      <li><b>Volatility Term Structure Contango:</b> 0.95 (Options pricing mechanics)</li>
      <li><b>FINRA Margin Credit Exhaustion:</b> 0.94 (Out-of-sample $R^2 = 35.68\%$)</li>
      <li><b>Advanced P-CAPE:</b> 0.92 (Explains 35% variance vs 24% standard CAPE)</li>
      <li><b>Topological Data Analysis (TDA) & Wavelets:</b> 0.91 (Persistent homology)</li>
      <li><b>Buffett Indicator:</b> 0.90 (Macro valuation anchor)</li>
      <li><b>Real Estate Metrics:</b> 0.89 (Price-to-Income / Rent disequilibrium)</li>
      <li><b>NLP LSTM-RNN / HMM:</b> 0.89 (Sequence break models)</li>
      <li><b>LPPLS Model:</b> 0.88 (Super-exponential singularity date)</li>
    </ul>
  </div>
</div>

---

<!-- Slide 3: Group 1 - Technical Details 1.2 -->
<div class="badge-header">SECTION 1: KEY FINDINGS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.94</div>
<h1>Macroeconomic & Valuation Extremes in the 2026 Environment</h1>

<div class="grid-3">
  <div class="card card-blue">
    <h2>Shiller CAPE & P-CAPE</h2>
    <ul>
      <li><b>CAPE = 41.37</b> (+10.39% YoY), 2nd highest in U.S. history.</li>
      <li>Top quintile CAPE yields 0.9% 10-yr real return historically.</li>
      <li>Dividend payout ratio fell from 65% (1988) to 35% (2024).</li>
      <li><b>P-CAPE</b> adjusts for retained earnings, explaining 35% variance (vs 24% standard CAPE).</li>
      <li>Earnings yield compressed to ~3.5%, exhausting multiple expansion.</li>
    </ul>
  </div>
  <div class="card card-amber">
    <h2>Buffett Indicator</h2>
    <ul>
      <li><b>Ratio = 218.1%</b> (Wilshire 5000 / Nominal GDP).</li>
      <li>Rests <b>56.6% above</b> long-term historical trendline.</li>
      <li>Globalization argument fails to justify magnitude of deviation.</li>
      <li>Multi-decade future cash flows pulled into present pricing.</li>
      <li>Macro decoupling from real domestic production base.</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2>Real Estate Affordability</h2>
    <ul>
      <li><b>Price-to-Income = 7.11x</b> (vs 1990s baseline 3.2x, 2006 peak 7.0x).</li>
      <li>Demographic gap: Under-40 real home values +30% vs income +9%.</li>
      <li>NAR: $86k income required for starter home vs $75k median income.</li>
      <li>Ownership $3,700-$4,300/mo vs Rent $1,450/mo.</li>
      <li>High Price-to-Rent negatively predicts future price growth.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 4: Group 1 - Technical Details 1.3 -->
<div class="badge-header">SECTION 1: KEY FINDINGS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.94</div>
<h1>Systemic Leverage & Market Microstructure Fragility</h1>

<div class="grid-2">
  <div class="card card-red">
    <h2>FINRA Margin Debt & Credit Exhaustion</h2>
    <ul>
      <li><b>Nominal Zenith:</b> $1.416 Trillion in May 2026 (+53.7% YoY, +8.53% MoM).</li>
      <li><b>Real Expansion:</b> +47.4% inflation-adjusted growth over 12 months.</li>
      <li><b>Velocity Mismatch:</b> Real margin debt grew 550% since 1997 vs 358% equity market real growth.</li>
      <li><b>Margin Credit Exhaustion:</b> Unused borrowing capacity is exhausted. $1\sigma$ credit drop predicts -1.1% lower monthly return (Annual $R^2 = 35.68\%$).</li>
      <li><b>Pingcang Line Dynamics:</b> Leverage near maintenance limits triggers broker liquidations, driving non-linear feedback cascades.</li>
    </ul>
  </div>
  <div class="card" style="text-align: center;">
    <h2>FINRA Real Margin Debt Trajectory</h2>
    <img src="./finra.png" style="max-width: 100%; max-height: 380px; border-radius: 8px; margin-top: 10px;" alt="FINRA Margin Debt">
  </div>
</div>

---

<!-- Slide 5: Group 1 - Implementation Details 1.1 -->
<div class="badge-header">SECTION 1: KEY FINDINGS &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.94</div>
<h1>System Architecture & Logging Engine (`config.py` & `ingestor.py`)</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>Core Setup & Data Engineering</h2>
    <ul>
      <li><b>Logging Hierarchy (`config.py`):</b><br>
      <code>RotatingFileHandler</code> logging strictly to <code>bubble_detector.log</code>.<br>
      Exceptions: <code>DataFetchError</code>, <code>IndicatorComputationError</code>, <code>ModelTrainingError</code>, <code>ValidationError</code>.</li>
      <li><b>Data Ingestion Engine (`ingestor.py`):</b><br>
      Fetches price series via <code>yfinance</code> with fallback synthetic generation.</li>
      <li><b>Polars Schema Downcasting:</b> Enforces <code>float32</code> / <code>int32</code> memory reduction.</li>
      <li><b>Missing Value Imputation:</b> Forward fill for daily prices; cubic spline interpolation for low-frequency macro data (GDP, Margin Debt).</li>
      <li><b>Parquet Storage:</b> Sub-millisecond local caching.</li>
    </ul>
  </div>
  <div class="card">
    <h2 class="val-green" style="font-size: 1.1rem;">Python Implementation Snippet</h2>
```python
# Polars Downcasting & Parquet Storage
import polars as pl

class DataIngestor:
    def optimize_schema(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns([
            pl.col(pl.FLOAT_DTYPES).cast(pl.Float32),
            pl.col(pl.INTEGER_DTYPES).cast(pl.Int32)
        ])

    def impute_macro(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns(
            pl.col('margin_debt').interpolate(method='cubic')
        )
```
  </div>
</div>

---

<!-- Slide 6: Group 2 - C-Level Summary -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: C-LEVEL / MBA &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>Supporting Evidence: Valuation, Econometrics & Machine Learning</h1>

<div class="grid-3">
  <div class="card card-blue">
    <h2>P-CAPE Dividend Correction</h2>
    <ul>
      <li>Corporate shift from dividends to share buybacks distorted classic Shiller CAPE.</li>
      <li>Payout-Adjusted CAPE (P-CAPE) brings forward retained earnings.</li>
      <li>P-CAPE explains 35% of 10-year return variance (vs 24% standard CAPE).</li>
      <li>Confirms valuation remains severely stretched even under growth-adjusted lens.</li>
    </ul>
  </div>
  <div class="card card-green">
    <h2>GPT AI Econometric Filter</h2>
    <ul>
      <li>Standard GSADF / PSY unit-root test suffers size distortion during $754B AI CapEx boom.</li>
      <li>Technology shocks create non-centrality parameters that look like explosive bubbles.</li>
      <li>Two-step fundamental decomposition filters out rational AI repricing, pinpointing speculative excess elsewhere.</li>
    </ul>
  </div>
  <div class="card card-amber">
    <h2>Topological & Wavelet Physics</h2>
    <ul>
      <li>Topological Data Analysis (TDA) embeds price series into high-dimensional geometric space.</li>
      <li>Morlet wavelets act as a mathematical microscope detecting structural phase changes.</li>
      <li>LPPLS models identify super-exponential oscillations preceding critical crash singularities.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 7: Group 2 - Technical Details 2.1 -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>P-CAPE Mathematics & Margin Credit Exhaustion</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>Payout-Adjusted CAPE (P-CAPE) Model</h2>
    <ul>
      <li><b>Formula Logic:</b> Standard $\text{CAPE} = P / E_{10}$. P-CAPE adjusts past earnings by bringing forward retained earnings $(1 - \text{Payout Ratio})$ compounding at the Cyclically Adjusted Earnings Yield (CAEY).</li>
      <li><b>Empirical Proof:</b> Out-of-sample explanatory power $R^2$ increases from 24% to 35% for prospective 10-year real equity returns.</li>
      <li><b>Baseline Implication:</b> Real corporate earnings grew at 2.0% p.a. over 125 years. Current equity yield @ 3.5% leaves zero mathematical runway for further multiple expansion.</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2>Margin Credit Exhaustion & Fire Sale Feedback</h2>
    <ul>
      <li><b>Margin Credit Definition:</b> Unused borrowing capacity collateralized by paper long gains.</li>
      <li><b>Predictive Supremacy:</b> Outperforms P/B and P/E ratios out-of-sample. A $1\sigma$ drop in credit predicts -1.1% monthly return (Annual $R^2 = 35.68\%$).</li>
      <li><b>Pingcang Line Dynamics:</b> Account leverage near maintenance limits forces broker liquidations. Indiscriminate selling depresses asset prices, triggering cascading margin calls.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 8: Group 2 - Technical Details 2.2 -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>GPT-Adjusted Econometric Bubble Detection (GSADF / PSY)</h1>

<div class="card card-blue">
  <h2>Phillips, Shi & Yu (PSY 2015) Procedure & General-Purpose Technology Shock Filtering</h2>
  <ol>
    <li><b>Standard GSADF Test Mechanics:</b><br>
    Sequentially executes right-tailed forward recursive augmented Dickey-Fuller (ADF) unit root tests with flexible, expanding window widths.<br>
    Null Hypothesis $H_0$: Asset price follows random walk with drift. Alternative $H_1$: Mildly explosive process (Evans rational collapsing bubble).</li>
    <li><b>The GPT Size Distortion Problem in 2026:</b><br>
    Hyperscalers' $754B AI CapEx introduces a non-linear, hump-shaped technology adoption shock into the Campbell-Shiller present-value model.<br>
    Fundamental price becomes locally explosive during GPT adoption, contaminating limit distribution with a non-centrality parameter.<br>
    <i>Result:</i> Unadjusted GSADF mistakenly flags rational AI fundamental repricing as an irrational bubble.</li>
    <li><b>Fundamental-versus-Speculative Two-Step Decomposition:</b><br>
    <i>Step 1:</i> Regress asset price $P_t$ on empirical technology proxies: Total Factor Productivity (TFP), IT investment, patent grants.<br>
    <i>Step 2:</i> Run GSADF exclusively on the residual price series $(P_t - \hat{P}_{t,\text{fundamental}})$.<br>
    <i>Outcome:</i> Filters out mega-cap AI false positives while exposing true speculative bubbles in non-earning small-cap tech.</li>
  </ol>
</div>

---

<!-- Slide 9: Group 2 - Technical Details 2.3 -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>Topological Data Analysis (TDA), Wavelets & LPPLS Models</h1>

<div class="grid-2">
  <div class="card card-amber">
    <h2>TDA Persistence & Morlet Wavelets</h2>
    <ul>
      <li><b>Takens' Delay Embedding:</b> Reconstructs 1D return series into high-dimensional geometric point cloud $\mathbf{x}_t = (x_t, x_{t-\tau}, \dots, x_{t-(d-1)\tau})$.</li>
      <li><b>Persistent Homology:</b> Measures appearance/disappearance of topological features (components $k=0$, loops $k=1$, voids $k=2$).</li>
      <li><b>Morlet Wavelet Scaleogram:</b> Automates sliding window size to adaptive 'Goldilocks' resolution.</li>
      <li><b>Early Warning Signal:</b> $L^p$ norms of persistence landscapes exhibit abnormal growth spikes prior to 2000 and 2008 crashes.</li>
    </ul>
  </div>
  <div class="card card-green">
    <h2>LPPLS Singularity & Machine Learning</h2>
    <ul>
      <li><b>Deterministic LPPLS Formula:</b><br>
      $$\ln(P(t)) = A + B(t_c - t)^m + C(t_c - t)^m \cos(\omega \ln(t_c - t) + \phi)$$</li>
      <li><b>Bounded NLS Optimization:</b> Trust-Region Reflective algorithm ($t_c > t, 0.1 < m < 0.9, 6 < \omega < 13$).</li>
      <li>LPPLS captures accelerating log-periodic oscillations driven by noise trader positive feedback.</li>
      <li><b>Deep Sequence ML (LSTM-RNN & HMM):</b> Predicts structural regime breaks using text sentiment, volatility skewness, and macro variables.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 10: Group 2 - Implementation Details 2.1 -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>Quantitative Indicator Module Architecture (`features/`)</h1>

<div class="card card-blue">
  <h2>Modular Quantitative Feature Extraction Pipeline (`features/`)</h2>
  <ul>
    <li><code>technicals.py</code>: Computes Moving Averages (MA20/50/200), RSI (14-day), Bollinger Bands (20-day, 2 std dev), and 20-day rolling volatility.</li>
    <li><code>macro_valuation.py</code>: Calculates Shiller CAPE (41.37), Payout-Adjusted CAPE (P-CAPE), Buffett Indicator (218.1% GDP), and rolling Z-score metrics.</li>
    <li><code>leverage.py</code>: Computes FINRA Margin Debt YoY growth, debt velocity, and excess debt capacity ('Margin Credit Exhaustion Score').</li>
    <li><code>econometric.py</code>: Implements PSY procedure (GSADF t-statistic) integrated with GPT fundamental decomposition to filter out false positive bubble signals on $754B AI CapEx.</li>
    <li><code>topology.py</code>: Executes Takens' delay coordinate embedding, TDA persistence landscape L2 norm, and Morlet wavelet scaleogram complexity score.</li>
  </ul>
</div>

---

<!-- Slide 11: Group 2 - Implementation Details 2.2 -->
<div class="badge-header">SECTION 2: SUPPORTING EVIDENCE &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.93</div>
<h1>Machine Learning Engine & Options Volatility Module</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>ML Predictor (`structural_breaks.py`)</h2>
    <ul>
      <li><b>RobustScaler Preprocessing:</b> Subtracts median and scales by Interquartile Range (IQR), protecting model from extreme outlier volatility spikes.</li>
      <li><b>Gradient Boosting Classifier:</b> Predicts forward 20-day drawdown risk probabilities.</li>
      <li><b>Expanding-Window Walk-Forward CV:</b> Implements <code>TimeSeriesSplit</code> cross-validation, guaranteeing strictly zero look-ahead bias.</li>
    </ul>
  </div>
  <div class="card">
    <h2 class="val-green" style="font-size: 1.1rem;">Python Options Vol Module (`options_vol.py`)</h2>
```python
# Options & Behavioral Tracking Engine
class OptionsVolatilityEngine:
    def compute_contango_slope(self, vix1d, vix3m):
        return (vix3m - vix1d) / vix3m

    def skew_alert_trigger(self, skew_val):
        return skew_val > 145.0  # Tail risk flag

    def cross_asset_vol_ratio(self, ovx, vix):
        return ovx / vix        # Baseline > 3.0
```
  </div>
</div>

---

<!-- Slide 12: Group 3 - C-Level Summary -->
<div class="badge-header">SECTION 3: SECTOR SPECIFIC APPLICATION &nbsp;|&nbsp; AUDIENCE: C-LEVEL / MBA &nbsp;|&nbsp; CONFIDENCE SCORE: 0.91</div>
<h1>Sector Application: AI Supercycle vs. Energy Shock Hazard</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>Tech Sector Concentration Risk</h2>
    <ul>
      <li><b>Semiconductor Concentration:</b> Semi weight in S&P 500 reached 18% (up from 3% a decade ago).</li>
      <li><b>Wall Street Earnings Dependency:</b> S&P 500 2026 earnings growth (15%) is driven almost entirely by 86% semiconductor earnings surge.</li>
      <li><b>AI CapEx Baseline:</b> Hyperscalers committing $754B in 2026 (projected &gt;$900B in 2027).</li>
      <li><b>Small-Cap AI Froth:</b> Russell 2000 & Microcap up 20-25% without TFP gains, creating extreme valuation vulnerability.</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2>Energy Sector Exogenous Threat</h2>
    <ul>
      <li><b>Fundamental Earnings Paradox:</b> Energy forecasted to post strongest Q2 earnings growth (doubling YoY).</li>
      <li><b>Cross-Asset Volatility Spike:</b> CBOE Crude Oil Volatility Index (OVX) spiked 35% in a single session.</li>
      <li><b>OVX/VIX Ratio @ 3.5x:</b> Commodities pricing severe geopolitical & inflation risk while equities remain complacent.</li>
      <li><b>Deleveraging Trigger:</b> Energy inflation spike would force central bank rate hikes, detonating the $1.4T margin debt bubble.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 13: Group 3 - Technical Details 3.1 -->
<div class="badge-header">SECTION 3: SECTOR SPECIFIC APPLICATION &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.91</div>
<h1>Technology Concentration & Small-Cap Speculative Froth</h1>

<div class="card card-blue">
  <h2>Semiconductor Dominance & Valuation Discount Rate Sensitivity</h2>
  <ol>
    <li><b>Index Weight Concentration:</b><br>
    Semiconductors now command 18% of S&P 500 total market cap.<br>
    Mega-cap semiconductor 3-month implied volatility has surged to 73% (more than double 2016 baseline), signaling massive embedded option risk.</li>
    <li><b>Structural Disconnect in Secondary Tier Tech:</b><br>
    Small-cap indices (Russell 2000 & Microcap) surged +20% and +25% in H1 2026.<br>
    The rally is heavily driven by unprofitable companies piggybacking on the AI narrative.<br>
    While hyperscalers' CapEx ($754B) is cointegrated with TFP, secondary tech lacks fundamental cash flow backing.</li>
    <li><b>Discount Rate Vulnerability:</b><br>
    Valuations in non-earning AI stocks rely entirely on long-dated terminal value cash flow assumptions.<br>
    Any upward shift in discount rates (driven by rate hikes or inflation) causes violent valuation contraction in secondary tech.</li>
  </ol>
</div>

---

<!-- Slide 14: Group 3 - Technical Details 3.2 -->
<div class="badge-header">SECTION 3: SECTOR SPECIFIC APPLICATION &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.91</div>
<h1>Energy Volatility & Cross-Asset Shock Transmission</h1>

<div class="card card-red">
  <h2>The OVX / VIX Anomaly & Macro Contagion Mechanics</h2>
  <ol>
    <li><b>Cross-Asset Volatility Divergence:</b><br>
    CBOE Crude Oil Volatility Index (OVX) single-day spike of +35% elevated the OVX-to-VIX ratio to 3.5x.<br>
    Options markets are pricing acute supply-chain disruption and commodity inflation exclusively into commodities, bypassing broad equity indices.</li>
    <li><b>Margin Debt Deleveraging Transmission Channel:</b><br>
    <i>Stage 1:</i> Geopolitical shock triggers sustained energy price surge.<br>
    <i>Stage 2:</i> Energy inflation compresses corporate profit margins across non-tech sectors and elevates CPI.<br>
    <i>Stage 3:</i> Central banks lose monetary easing flexibility, holding interest rates higher for longer.<br>
    <i>Stage 4:</i> High rates increase margin borrowing costs, triggering margin calls at the Pingcang Line and initiating a forced $1.416T deleveraging cascade.</li>
  </ol>
</div>

---

<!-- Slide 15: Group 3 - Technical Details 3.3 -->
<div class="badge-header">SECTION 3: SECTOR SPECIFIC APPLICATION &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.91</div>
<h1>Cross-Sector Contagion & Liquidity Transmission Channels</h1>

<div class="grid-4">
  <div class="card card-red">
    <h2 class="val-red" style="font-size: 1.0rem;">STEP 1: SHOCK</h2>
    <p><b>Energy / Geopolitical Shock</b></p>
    <ul>
      <li>OVX spikes +35%</li>
      <li>Oil volatility ratio OVX/VIX hits 3.5x</li>
      <li>Commodity risk bypasses broad equities initially</li>
    </ul>
  </div>
  <div class="card card-amber">
    <h2 class="val-amber" style="font-size: 1.0rem;">STEP 2: MACRO</h2>
    <p><b>Inflation & Rate Pressure</b></p>
    <ul>
      <li>Energy cost pass-through raises CPI</li>
      <li>Central banks forced into hawkish stance</li>
      <li>Discount rates rise across all asset classes</li>
    </ul>
  </div>
  <div class="card card-blue">
    <h2 class="val-blue" style="font-size: 1.0rem;">STEP 3: LEVERAGE</h2>
    <p><b>Margin Debt Call Trigger</b></p>
    <ul>
      <li>Levered accounts hit Pingcang Line</li>
      <li>$1.416T debt faces broker calls</li>
      <li>Margin Credit fully exhausted</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2 class="val-red" style="font-size: 1.0rem;">STEP 4: CRASH</h2>
    <p><b>Indiscriminate Fire Sale</b></p>
    <ul>
      <li>Broker liquidations hit mega-cap tech</li>
      <li>Implied correlation spikes &lt;8 to &gt;80</li>
      <li>Full systemic market crash</li>
    </ul>
  </div>
</div>

---

<!-- Slide 16: Group 3 - Implementation Details 3.1 -->
<div class="badge-header">SECTION 3: SECTOR SPECIFIC APPLICATION &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.91</div>
<h1>Sector Volatility & Dashboard Tab Implementation (`dashboard.py`)</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>Sector Dashboard Tab 5 Design</h2>
    <ul>
      <li><b>Interactive Tab:</b> 'Sector-Specific Health Dashboard' in NiceGUI application.</li>
      <li><b>Semiconductor Trackers:</b> Monitors concentration ratio (18% threshold) and 3-month rolling IV (73% alert).</li>
      <li><b>Small-Cap TFP Divergence:</b> Real-time monitoring of Russell 2000 GSADF residual vs TFP growth.</li>
      <li><b>Energy Volatility Monitor:</b> Ingests OVX tick data and computes live OVX/VIX ratio with color-coded alert badges (&gt;3.0 = Amber, &gt;3.5 = Red).</li>
    </ul>
  </div>
  <div class="card">
    <h2 class="val-green" style="font-size: 1.1rem;">NiceGUI Component Snippet</h2>
```python
# NiceGUI Sector Tab Implementation
from nicegui import ui

def render_sector_tab(data):
    with ui.tab_panel('Sector-Specific Health'):
        ui.label('Sector Concentration & Cross-Asset Vol')
        ovx_vix = data['ovx'] / data['vix']
        if ovx_vix > 3.5:
            ui.badge('CRUDE OIL VOLATILITY ALERT',
                     color='red')
        # Render Plotly sector dispersion chart
        ui.plotly(fig_sector_health)
```
  </div>
</div>

---

<!-- Slide 17: Group 4 - C-Level Summary -->
<div class="badge-header">SECTION 4: IMPLICATIONS FOR SYSTEMIC STABILITY &nbsp;|&nbsp; AUDIENCE: C-LEVEL / MBA &nbsp;|&nbsp; CONFIDENCE SCORE: 0.95</div>
<h1>Implications for Systemic Stability: Fragility Architecture</h1>

<div class="grid-3">
  <div class="card card-blue">
    <h2>The Concentration Trap</h2>
    <ul>
      <li><b>Narrowing Market Breadth:</b> S&P 500 index gains concentrated in a shrinking handful of mega-caps.</li>
      <li><b>Illusion of Stability:</b> Index volatility (VIX 15-17) appears calm while underlying stock dispersion (DSPX &gt; 46) is at multi-year highs.</li>
    </ul>
  </div>
  <div class="card card-red">
    <h2>Liquidity Illusion</h2>
    <ul>
      <li>Record Margin Debt ($1.416T) has exhausted aggregate unused borrowing capacity.</li>
      <li>Market lacks a marginal buyer buffer.</li>
      <li>Any forced selling will encounter a liquidity void, causing rapid price gapping.</li>
    </ul>
  </div>
  <div class="card card-amber">
    <h2>Institutional Fear</h2>
    <ul>
      <li><b>Smart Money Positioning:</b> CBOE SKEW &gt; 145 reveals aggressive institutional buying of OTM puts.</li>
      <li><b>Implied Correlation Collapse (COR3M &lt; 8.0):</b> Historically precedes sharp volatility regime shifts.</li>
    </ul>
  </div>
</div>

---

<!-- Slide 18: Group 4 - Technical Details 4.1 -->
<div class="badge-header">SECTION 4: IMPLICATIONS FOR SYSTEMIC STABILITY &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.95</div>
<h1>Mechanics of Market Liquidity Exhaustion</h1>

<div class="card card-red">
  <h2>Margin Credit Depletion & Pingcang Maintenance Collateral Limits</h2>
  <ol>
    <li><b>Margin Credit Capacity Limits:</b><br>
    $\text{Margin Credit} = \text{Total Allowable Borrowing Power} - \text{Active Margin Debt}$.<br>
    In May 2026, active debt ($1.416T) reached maximum regulatory limits, reducing unused credit to zero.<br>
    <i>Result:</i> Levered market participants can no longer step in to buy routine pullbacks.</li>
    <li><b>Non-Linear Fire Sale Collateral Dynamics:</b><br>
    When account equity hits broker maintenance thresholds (Pingcang Line), automated risk systems issue margin calls.<br>
    Investors are forced to sell holdings indiscriminately into a thin bid stack.<br>
    Liquidations depress asset prices further, triggering a self-reinforcing liquidation loop (1929 & 2015 crash mechanics).</li>
    <li><b>Structural Vulnerability Matrix:</b><br>
    High Valuation (CAPE 41.37) + High Leverage ($1.416T) + Zero Margin Credit = Maximum Systemic Fragility.</li>
  </ol>
</div>

---

<!-- Slide 19: Group 4 - Technical Details 4.2 -->
<div class="badge-header">SECTION 4: IMPLICATIONS FOR SYSTEMIC STABILITY &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.95</div>
<h1>Options Tail-Risk Pricing & Implied Correlation Collapse</h1>

<div class="grid-2">
  <div class="card card-amber">
    <h2>SKEW & Dispersion Indicators</h2>
    <ul>
      <li><b>CBOE SKEW Index &gt; 145 (Peak 154):</b> Reflects extreme pricing of left-tail crash protection relative to ATM options.</li>
      <li>Normal Bull Range: 100-120. Elevated SKEW while VIX spot remains low (15-17) proves institutional money is aggressively hedging.</li>
      <li><b>CBOE Dispersion Index (DSPX) &gt; 46 vs Implied Correlation (COR3M) &lt; 8.0:</b> Multi-year record divergence.</li>
      <li><b>Structural Interpretation:</b> Individual stocks are moving independently while index is pinned—a classic late-stage terminal bull characteristic.</li>
    </ul>
  </div>
  <div class="card" style="text-align: center;">
    <h2>Options Metric Visualization</h2>
    <img src="./impliedvolatilitymetric.png" style="max-width: 100%; max-height: 380px; border-radius: 8px; margin-top: 10px;" alt="Options Volatility Metric">
  </div>
</div>

---

<!-- Slide 20: Group 4 - Technical Details 4.3 -->
<div class="badge-header">SECTION 4: IMPLICATIONS FOR SYSTEMIC STABILITY &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.95</div>
<h1>Non-Linear Chaos & Phase Transition Forecasting</h1>

<div class="card card-blue">
  <h2>Phase Space Attractors & LPPLS Critical Singularity Date</h2>
  <ol>
    <li><b>Topological Phase Shift Detection:</b><br>
    Dynamic tracking of TDA persistence landscape $L^2$ norms reveals a structural shift from a normal gaussian return distribution to a chaotic attractor regime.<br>
    Scaleogram complexity scores from Morlet wavelets show high-frequency volatility clustering across multiple time horizons.</li>
    <li><b>LPPLS Critical Singularity Estimation:</b><br>
    Super-exponential power-law fits predict critical point $t_c$ where market instability reaches maximum.<br>
    Accelerating log-periodic price oscillations confirm self-reinforcing noise trader imitation.</li>
    <li><b>Operational Risk Regime State Machine:</b><br>
    Regime 0: Low Vol Contango (Complacency) $\rightarrow$ Regime 1: Dispersion & SKEW Spike (Institutional Hedging) $\rightarrow$ Regime 2: Energy/Rate Exogenous Trigger $\rightarrow$ Regime 3: Margin Call Liquidation (Systemic Crash).</li>
  </ol>
</div>

---

<!-- Slide 21: Group 4 - Implementation Details 4.1 -->
<div class="badge-header">SECTION 4: IMPLICATIONS FOR SYSTEMIC STABILITY &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.95</div>
<h1>Systemic Risk Dashboard Application Architecture (`dashboard.py`)</h1>

<div class="card card-blue">
  <h2>5-Tab Interactive Plotly & NiceGUI Integration</h2>
  <ul>
    <li><b>Header Bar & CTA Banner:</b> High-impact typography (600-800 weight) with real-time systemic risk status badge.</li>
    <li><b>Tab 1: Macro Valuation Dashboard:</b> Interactive Plotly time series of Shiller CAPE, P-CAPE, and Buffett Indicator with historical crash overlays.</li>
    <li><b>Tab 2: Liquidity & Leverage Dashboard:</b> FINRA Margin Debt YoY growth, velocity, and live Margin Credit Exhaustion Score gauge.</li>
    <li><b>Tab 3: Econometric Bubble Dashboard:</b> GSADF t-statistic charts with GPT fundamental decomposition toggle.</li>
    <li><b>Tab 4: Sentiment & Volatility Dashboard:</b> VIX contango term structure, SKEW index alert (&gt;145), and DSPX vs COR3M correlation dispersion tracker.</li>
    <li><b>Tab 5: Sector-Specific Health Dashboard:</b> Semiconductor concentration risk and energy volatility ratios.</li>
  </ul>
</div>

---

<!-- Slide 22: Group 5 - C-Level Summary -->
<div class="badge-header">SECTION 5: STRATEGIC RECOMMENDATIONS &nbsp;|&nbsp; AUDIENCE: C-LEVEL / MBA &nbsp;|&nbsp; CONFIDENCE SCORE: 0.96</div>
<h1>Strategic Recommendations: C-Suite Institutional Roadmap</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>1. TDA Wavelet Regime Monitoring</h2>
    <p>Deploy Topological Data Analysis with Morlet wavelets to monitor $L^p$ persistence landscape norms. Systematically reduce equity beta prior to crash onset.</p>
  </div>
  <div class="card card-red">
    <h2>2. Track FINRA Margin Credit Limit</h2>
    <p>Treat unused margin credit as a hard liquidity constraint. As capacity exhausts, aggressively adjust downside volatility targets upward to prepare for Pingcang line fire sales.</p>
  </div>
  <div class="card card-green">
    <h2>3. GPT-Adjusted Tech Allocation</h2>
    <p>Use GPT fundamental decomposition. Allocate strictly to mega-cap tech backed by CapEx & TFP gains; divest from unprofitable small-cap AI speculative froth.</p>
  </div>
  <div class="card card-amber">
    <h2>4. Asymmetric Options & Cross-Asset Hedges</h2>
    <p>Exploit VIX contango via short-term long-gamma positions. Bypass expensive SKEW put options by constructing tail risk hedges using crude oil (OVX) and Treasury (MOVE) volatility.</p>
  </div>
</div>

---

<!-- Slide 23: Group 5 - Technical Details 5.1 -->
<div class="badge-header">SECTION 5: STRATEGIC RECOMMENDATIONS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.96</div>
<h1>Institutional Quantitative Risk Protocols</h1>

<div class="card card-blue">
  <h2>Algorithmic Trigger Rules & Margin Credit Hard Thresholds</h2>
  <ol>
    <li><b>TDA Persistence Landscape Norm Trigger:</b><br>
    <i>Operational Rule:</i> Monitor the $L^2$ norm of the persistent homology landscape daily.<br>
    <i>Action Threshold:</i> When $L^2$ norm breaches +2.5 standard deviations above its 90-day moving median, automatically reduce portfolio equity beta by 30% to 50% within 24 hours.</li>
    <li><b>FINRA Margin Credit Exhaustion Rule:</b><br>
    <i>Operational Rule:</i> Compute aggregate margin credit velocity (Margin Credit YoY%).<br>
    <i>Action Threshold:</i> When Margin Credit YoY drops below -15% while nominal debt is at historical zenith, mandate dynamic VaR scaling and double cash reserves.</li>
    <li><b>Structural Break Walk-Forward Integration:</b><br>
    Integrate <code>structural_breaks.py</code> Gradient Boosting predictions with expanding-window walk-forward CV to update portfolio drawdown probability limits dynamically.</li>
  </ol>
</div>

---

<!-- Slide 24: Group 5 - Technical Details 5.2 -->
<div class="badge-header">SECTION 5: STRATEGIC RECOMMENDATIONS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.96</div>
<h1>GPT-Adjusted Cointegration Asset Allocation Strategy</h1>

<div class="card card-green">
  <h2>Fundamental-versus-Speculative Long/Short Portfolio Construction</h2>
  <ol>
    <li><b>Fundamental Cointegration Decomposition:</b><br>
    Decompose asset price: $P_t = P_{t,\text{fundamental}} + P_{t,\text{speculative}}$.<br>
    <i>Long Leg:</i> Allocate exclusively to mega-cap technology firms whose price trajectory cointegrates with empirical AI CapEx ($754B) and observable TFP growth.<br>
    <i>Short Leg:</i> Short secondary small-cap tech (Russell 2000 AI story stocks) that exhibit explosive unadjusted GSADF unit-root stats without corresponding TFP gains.</li>
    <li><b>Multiple Re-anchoring via P-CAPE:</b><br>
    Replace static forward P/E multiples with Payout-Adjusted CAPE (P-CAPE) to accurately evaluate retained earnings compounding in mega-cap technology balance sheets.</li>
    <li><b>Asymmetric Return Profile:</b><br>
    Protects upside participation in legitimate technological supercycle while insulating portfolio from speculative bubble collapse.</li>
  </ol>
</div>

---

<!-- Slide 25: Group 5 - Technical Details 5.3 -->
<div class="badge-header">SECTION 5: STRATEGIC RECOMMENDATIONS &nbsp;|&nbsp; AUDIENCE: EXPERT / PHD &nbsp;|&nbsp; CONFIDENCE SCORE: 0.96</div>
<h1>Asymmetric Options & Cross-Asset Volatility Hedges</h1>

<div class="card card-amber">
  <h2>Cross-Asset Volatility Proxy Hedging Matrix</h2>
  <ol>
    <li><b>Exploiting Volatility Term Structure Contango:</b><br>
    Front-month VIX1D (&lt;10) vs VIX3M/1Y (19-23) contango allows ultra-cheap short-term long gamma positioning via 1-week straddles/strangles to capture sudden dispersion events.</li>
    <li><b>Cross-Asset Volatility Hedges (Bypassing Overpriced SKEW):</b><br>
    CBOE SKEW &gt; 145 makes standard OTM S&P 500 put protection exorbitantly expensive.<br>
    <i>Solution:</i> Construct cross-asset tail risk hedges using Crude Oil Volatility (OVX) and Treasury Volatility (MOVE) call options.</li>
    <li><b>Payoff Asymmetry & Cost Efficiency:</b><br>
    Reduces negative carry (drag) of hedging by 60% while delivering massive upside payouts during energy/interest rate macroeconomic shock events.</li>
  </ol>
</div>

---

<!-- Slide 26: Group 5 - Implementation Details 5.1 -->
<div class="badge-header">SECTION 5: STRATEGIC RECOMMENDATIONS &nbsp;|&nbsp; AUDIENCE: DATA SCIENCE / ENG &nbsp;|&nbsp; CONFIDENCE SCORE: 0.96</div>
<h1>UI/UX Accessibility Engine & Production Deployment (`ui_theme.py`)</h1>

<div class="grid-2">
  <div class="card card-blue">
    <h2>UI Design System & Accessibility</h2>
    <ul>
      <li><b>WCAG 2.2 AA Programmatic Compliance (`ui_theme.py`):</b><br>
      <code>calculate_contrast_ratio</code> & <code>is_wcag_aa_compliant</code> enforce $\ge 4.5:1$ text contrast and $\ge 3.0:1$ UI element contrast.</li>
      <li><b>Dyslexia-Friendly Typography Stack:</b><br>
      Font Stack: SF Pro Text / Inter / OpenDyslexic.<br>
      Letter Spacing: 0.015em | Line Height: 1.5 body, 1.3 heading.<br>
      Strictly prohibits decorative fonts.</li>
      <li><b>8px Base Grid Rhythm & iOS 13+ Visual Styling:</b><br>
      Spacing tokens: 4px, 8px, 16px, 24px, 32px, 48px.<br>
      14px rounded corners; dynamic CSS variable light/dark switcher.</li>
    </ul>
  </div>
  <div class="card">
    <h2 class="val-green" style="font-size: 1.1rem;">Python Accessibility Checker Snippet</h2>
```python
# ui_theme.py WCAG 2.2 Checker
def calculate_contrast_ratio(hex1, hex2):
    lum1 = relative_luminance(parse_hex_color(hex1))
    lum2 = relative_luminance(parse_hex_color(hex2))
    l1, l2 = max(lum1, lum2), min(lum1, lum2)
    return (l1 + 0.05) / (l2 + 0.05)

def is_wcag_aa_compliant(hex_fg, hex_bg,
                        is_large=False):
    ratio = calculate_contrast_ratio(hex_fg, hex_bg)
    return ratio >= (3.0 if is_large else 4.5)
```
  </div>
</div>
"""

with open(marp_file_path, "w", encoding="utf-8") as f:
    f.write(marp_content)

print(f"Successfully generated Marp Markdown presentation at: {marp_file_path}")

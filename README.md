# Financial Ratios Methodology

This repository documents the methodology used to transform raw financial statement data into comparable investment metrics.

It serves as a transparent technical reference describing how accounting data, price data, and trailing values can be normalized for long-term equity analysis. The objective is reproducibility — not stock recommendations.

---

## Scope

The methodology focuses on fundamental analysis metrics commonly used to evaluate business quality and valuation:

- Profitability
- Leverage
- Growth
- Cash generation
- Valuation multiples

The calculations are designed for multi-year analysis rather than short-term trading signals.

---

## Data Normalization Principles

Financial data contains distortions that must be corrected before comparison.

Typical issues:

- Stock splits altering price history
- Quarterly seasonality
- Earnings restatements
- Negative denominators
- Outlier ratios

Most metrics use **Trailing Twelve Months (TTM)** aggregation instead of single-quarter values:

TTM = sum(last 4 quarters)

This reduces noise and better reflects economic reality.

---

## Price Adjustments

Historical prices must be adjusted for corporate actions:

adjusted_price = raw_price × split_factor × dividend_factor


Without adjustment, long-term returns appear artificially inflated or deflated.

---

## Core Metrics

### Revenue Growth (YoY)
Measures business expansion independent of short-term volatility.

Revenue Growth = (Revenue_q - Revenue_q-4) / Revenue_q-4


### Free Cash Flow (TTM)

FCF = OperatingCashFlow - CapitalExpenditures
FCF_TTM = sum(last 4 quarters)


### Profit Margin (TTM)

ProfitMargin = NetIncome_TTM / Revenue_TTM


### Debt to Equity

DebtToEquity = TotalDebt / ShareholdersEquity


### Price to Earnings (TTM)

PE = Price / EPS_TTM
EPS_TTM = NetIncome_TTM / SharesOutstanding


### PEG Ratio

PEG = PE / EarningsGrowthRate

---

## Industry Comparison Method

Instead of averages, comparisons use the **median**:


industry_value = median(peer_group)


The median avoids distortions caused by extreme values.

---

## Snapshot vs Historical Values

Differences may appear between latest values and historical graphs due to:

- Financial restatements
- Diluted vs non-diluted share counts
- Updated filings

This is expected in real accounting datasets.

---

## Reproducible Example

See `/examples` for step-by-step calculations and a minimal Python implementation demonstrating how raw financial statements can be converted into normalized metrics.

---

## Full Dataset

A continuously updated implementation applying this methodology to hundreds of companies is available at:

https://clarityvesting.com

---

## License

The methodology is public for educational and research purposes.  
Raw financial statement data belongs to its respective providers and issuers.

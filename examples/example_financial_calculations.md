# Example Financial Calculations

This document demonstrates how raw financial statement data is transformed into normalized investment metrics.

The numbers below are fictional but structured like real filings.

---

## Input Data (Quarterly)

| Quarter | Revenue | Net Income | Operating Cash Flow | CapEx | Shares Outstanding | Total Debt | Equity |
|---------|--------|-----------|------------------|-------|------------------|------------|-------|
| Q1      | 10,000 | 1,200     | 1,800            | 400   | 1,000            | 8,000      | 12,000|
| Q2      | 10,800 | 1,350     | 1,900            | 420   | 1,000            | 8,200      | 12,500|
| Q3      | 11,200 | 1,400     | 2,000            | 450   | 1,000            | 8,100      | 12,900|
| Q4      | 12,000 | 1,600     | 2,200            | 500   | 1,000            | 8,300      | 13,400|

Current share price: **$42**

---

## Step 1 — Trailing Twelve Months (TTM)

TTM aggregates the last four quarters.

Revenue_TTM = 44,000
NetIncome_TTM = 5,550
OCF_TTM = 7,900
CapEx_TTM = 1,770


---

## Step 2 — Free Cash Flow


FCF_TTM = OCF_TTM - CapEx_TTM = 7,900 - 1,770 = 6,130


---

## Step 3 — Profit Margin


ProfitMargin = NetIncome_TTM / Revenue_TTM = 5,550 / 44,000 = 12.6%


---

## Step 4 — Earnings Per Share


EPS_TTM = NetIncome_TTM / SharesOutstanding = 5,550 / 1,000 = 5.55$


---

## Step 5 — Price to Earnings Ratio


PE = Price / EPS_TTM = 42 / 5.55 ≈ 7.57



---

## Step 6 — Free Cash Flow Yield


MarketCap = Price × SharesOutstanding = 42 × 1,000 = 42,000
FCF_Yield = FCF_TTM / MarketCap = 6,130 / 42,000 ≈ 14.6%


---

## Step 7 — Debt to Equity

Use the most recent balance sheet (latest quarter).


DebtToEquity = TotalDebt / Equity = 8,300 / 13,400 ≈ 0.62


---

## Step 8 — Revenue Growth (YoY)

Compare Q4 to the same quarter last year (assume previous Q4 revenue = 9,600).

RevenueGrowth = (12,000 - 9,600) / 9,600 = 25%



---

## Interpretation (Example Only)

| Metric | Meaning |
|--------|---------|
| Low P/E | Potential undervaluation |
| High FCF Yield | Strong cash generation |
| Moderate Debt/Equity | Balanced leverage |
| Growing Revenue | Expanding business |



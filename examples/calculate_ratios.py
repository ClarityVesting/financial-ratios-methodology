"""
Example financial ratio calculations

This script demonstrates how raw quarterly financial statement data
can be transformed into normalized investment metrics.

Numbers are fictional and used only for demonstration.
"""

# -------------------------
# INPUT DATA (quarterly)
# -------------------------

quarters = [
    {"revenue": 10000, "net_income": 1200, "ocf": 1800, "capex": 400},
    {"revenue": 10800, "net_income": 1350, "ocf": 1900, "capex": 420},
    {"revenue": 11200, "net_income": 1400, "ocf": 2000, "capex": 450},
    {"revenue": 12000, "net_income": 1600, "ocf": 2200, "capex": 500},
]

shares_outstanding = 1000
share_price = 42
total_debt_latest = 8300
equity_latest = 13400
revenue_same_q_last_year = 9600

# -------------------------
# HELPERS
# -------------------------

def ttm_sum(key):
    return sum(q[key] for q in quarters)

# -------------------------
# CALCULATIONS
# -------------------------

revenue_ttm = ttm_sum("revenue")
net_income_ttm = ttm_sum("net_income")
ocf_ttm = ttm_sum("ocf")
capex_ttm = ttm_sum("capex")

# Free Cash Flow
fcf_ttm = ocf_ttm - capex_ttm

# Profit Margin
profit_margin = net_income_ttm / revenue_ttm

# EPS
eps_ttm = net_income_ttm / shares_outstanding

# PE Ratio
pe_ratio = share_price / eps_ttm

# Market Cap
market_cap = share_price * shares_outstanding

# FCF Yield
fcf_yield = fcf_ttm / market_cap

# Debt to Equity
debt_to_equity = total_debt_latest / equity_latest

# Revenue Growth YoY (latest quarter vs same quarter last year)
latest_revenue = quarters[-1]["revenue"]
revenue_growth = (latest_revenue - revenue_same_q_last_year) / revenue_same_q_last_year

# -------------------------
# OUTPUT
# -------------------------

print("=== Calculated Metrics ===")
print(f"Revenue TTM: {revenue_ttm}")
print(f"Net Income TTM: {net_income_ttm}")
print(f"Free Cash Flow TTM: {fcf_ttm}")
print(f"Profit Margin: {profit_margin:.2%}")
print(f"EPS (TTM): {eps_ttm:.2f}")
print(f"P/E Ratio: {pe_ratio:.2f}")
print(f"FCF Yield: {fcf_yield:.2%}")
print(f"Debt to Equity: {debt_to_equity:.2f}")
print(f"Revenue Growth YoY: {revenue_growth:.2%}")

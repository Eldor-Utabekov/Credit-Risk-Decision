import pandas as pd
import sqlite3

# 1. Load the data with PD scores
conn = sqlite3.connect('data/banking_risk.db')
df = pd.read_sql("SELECT * FROM fact_loans_engineered", conn)

# 2. Financial Assumptions (Senior Move: Define these clearly)
LGD = 0.70  # Loss Given Default: Assume 70% of the loan is unrecoverable

# 3. Calculate Financial Metrics
# Expected Loss (EL)
df['expected_loss'] = df['prob_default'] * LGD * df['loan_amnt']

# Expected Interest Income
# We divide by 100 because loan_int_rate is a percentage (e.g., 11.0)
df['expected_interest_income'] = df['loan_amnt'] * (df['loan_int_rate'] / 100)

# Net Expected Profit
df['expected_profit'] = df['expected_interest_income'] - df['expected_loss']

# 4. Break-even Interest Rate
# This is the rate the bank MUST charge just to cover the risk
df['breakeven_rate'] = (df['expected_loss'] / df['loan_amnt']) * 100

# 5. Save the final "Golden Table" back to SQL
df.to_sql('fact_loans_final', conn, if_exists='replace', index=False)

# 6. Quick Portfolio Audit
total_loss = df['expected_loss'].sum()
total_profit = df['expected_profit'].sum()

print("--- PORTFOLIO FINANCIAL FORECAST ---")
print(f"Total Expected Loss:   ${total_loss:,.2f}")
print(f"Total Expected Profit: ${total_profit:,.2f}")
print(f"\nFinancial Layer sync complete. Database table 'fact_loans_final' is ready for Power BI.")

conn.close()
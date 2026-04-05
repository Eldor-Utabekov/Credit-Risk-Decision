import pandas as pd
import sqlite3

# 1. Load data from the database
conn = sqlite3.connect('data/banking_risk.db')

# We join the tables to get all features in one view
query = """
SELECT f.*, 
       c.person_age, c.person_income, c.person_emp_length, c.person_home_ownership,
       ch.cb_person_default_on_file, ch.cb_person_cred_hist_length, ch.loan_grade
FROM fact_loans f
JOIN dim_customers c ON f.customer_id = c.customer_id
JOIN dim_credit_history ch ON f.customer_id = ch.customer_id
"""
df = pd.read_sql(query, conn)

# Remove any duplicate columns that might have slipped through the join
df = df.loc[:,~df.columns.duplicated()].copy()

print(f"Processing {len(df)} records for feature engineering...")

# 2. Professional Imputation
df['person_emp_length'] = df['person_emp_length'].fillna(0)
# Use median of the loan grade to fill missing interest rates
df['loan_int_rate'] = df.groupby('loan_grade')['loan_int_rate'].transform(lambda x: x.fillna(x.median()))

# 3. Create Senior Features
# Ratio 1: Monthly Debt-to-Income (DTI) 
# Logic: How much of their monthly paycheck goes to this loan?
df['monthly_income'] = df['person_income'] / 12
df['monthly_debt_ratio'] = (df['loan_amnt'] / 12) / df['monthly_income']

# 4. Save the "Model-Ready" data
# We use 'replace' to ensure a clean start
df.to_sql('fact_loans_engineered', conn, if_exists='replace', index=False)

conn.close()
print("Feature Engineering Complete: Ratios created and missing values imputed.")
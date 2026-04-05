import pandas as pd
import sqlite3
import os

# 1. Setup Paths
raw_data_path = 'data/credit_risk_dataset.csv'
db_path = 'data/banking_risk.db'

if not os.path.exists(raw_data_path):
    print(f"Error: Could not find {raw_data_path}")
else:
    df = pd.read_csv(raw_data_path)
    df = df.dropna()
    
    df['customer_id'] = range(1001, 1001 + len(df))
    df['loan_id'] = range(5001, 5001 + len(df))

    # 2. NEW: Create the Risk Segment Metadata
    # This acts as a 'Mapping' table
    risk_data = {
        'loan_grade': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'risk_segment': ['Elite', 'Prime', 'Near-Prime', 'Subprime', 'Deep Subprime', 'Deep Subprime', 'Deep Subprime'],
        'risk_level': [1, 2, 3, 4, 5, 5, 5] # Numeric rank for sorting in Power BI
    }
    df_risk_segments = pd.DataFrame(risk_data)

    # 3. Connect to SQLite
    conn = sqlite3.connect(db_path)

    # Dimension: Customers
    df[['customer_id', 'person_age', 'person_income', 'person_emp_length', 'person_home_ownership']].to_sql('dim_customers', conn, if_exists='replace', index=False)

    # Dimension: Credit History
    df[['customer_id', 'cb_person_default_on_file', 'cb_person_cred_hist_length', 'loan_grade']].to_sql('dim_credit_history', conn, if_exists='replace', index=False)

    # NEW Dimension: Risk Segments (The lookup table)
    df_risk_segments.to_sql('dim_risk_segments', conn, if_exists='replace', index=False)

    # Fact Table: Loans
    df[['loan_id', 'customer_id', 'loan_amnt', 'loan_int_rate', 'loan_status', 'loan_percent_income']].to_sql('fact_loans', conn, if_exists='replace', index=False)

    conn.close()
    print(f"Star Schema created in {db_path}")
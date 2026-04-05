import pandas as pd
import os

# 1. Setup Paths
raw_data_path = 'data/credit_risk_dataset.csv'

if not os.path.exists(raw_data_path):
    print(f"Error: Could not find {raw_data_path}. Ensure you are in the project root.")
else:
    df = pd.read_csv(raw_data_path)
    initial_count = len(df)

    # Duplicate Audit
    exact_duplicates = df.duplicated().sum()
    after_dedup_count = len(df)

    #Missing Value Audit
    missing_values = df.isnull().sum()
    
    #Default Rate (The 'Target' Signal)
    default_rate = df['loan_status'].mean()

    #Output Report
    print("--- DATA QUALITY AUDIT ---")
    print(f"Initial Rows:       {initial_count}")
    print(f"Duplicates Removed: {exact_duplicates}")
    print(f"Final Row Count:    {after_dedup_count}")
    print(f"\nDefault Rate (Imbalance Check): {default_rate:.2%}")
    print("\nMissing Values per Column:")
    print(missing_values[missing_values > 0])
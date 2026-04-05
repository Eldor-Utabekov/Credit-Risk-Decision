import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Load the engineered data
conn = sqlite3.connect('data/banking_risk.db')
df = pd.read_sql("SELECT * FROM fact_loans_engineered", conn)

# 2. Define Features (X) and Target (y)
features = [
    'person_income', 
    'loan_amnt', 
    'loan_int_rate', 
    'person_emp_length', 
    'monthly_debt_ratio'
]

# Ensure we only use rows where these features exist
df_model = df.dropna(subset=features + ['loan_status'])

X = df_model[features]
y = df_model['loan_status']

# 3. Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train the Model (Balanced handles the 22% default rate)
model = LogisticRegression(class_weight='balanced')
model.fit(X_scaled, y)

# 5. Generate PD (Probability of Default)
df_model['prob_default'] = model.predict_proba(X_scaled)[:, 1]

# 6. Save back to SQL (Overwrite the engineered table with PD included)
df_model.to_sql('fact_loans_engineered', conn, if_exists='replace', index=False)

# 7. Output the "Senior" Insight: Coefficients
importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.coef_[0]
}).sort_values(by='Importance', ascending=False)

print("\n--- RISK DRIVERS (RANKED) ---")
print(importance)
print("\nPD Model successful. Probabilities synced to database.")

conn.close()
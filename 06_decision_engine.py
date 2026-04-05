import sqlite3

conn = sqlite3.connect(r'C:\Users\Talixo\projects\Credit-Risk-Decision\data\banking_risk.db')
cursor = conn.cursor()

sql_gold_layer = """
DROP VIEW IF EXISTS view_gold_loan_strategy;
CREATE VIEW view_gold_loan_strategy AS
SELECT 
    f.loan_id,
    f.customer_id as applicant_id,
    f.loan_amnt as loan_amount,
    f.loan_int_rate as interest_rate,
    f.prob_default,
    0.70 AS lgd, -- Loss Given Default (Assumption)
    f.expected_loss,
    f.expected_profit,
    -- Senior Field: Break-even Rate (The rate needed to cover the risk)
    (f.expected_loss / f.loan_amnt) * 100 AS break_even_rate,
    f.loan_status as default_flag,
    f.risk_segment,
    -- Income Segmentation
    CASE 
        WHEN c.person_income < 30000 THEN 'Low Income'
        WHEN c.person_income < 70000 THEN 'Middle Income'
        ELSE 'High Income' 
    END AS income_segment,
    -- Debt-to-Income Segmentation
    CASE 
        WHEN f.loan_percent_income < 0.15 THEN 'Low DTI'
        WHEN f.loan_percent_income < 0.30 THEN 'Mid DTI'
        ELSE 'High DTI'
    END AS dti_segment,
    -- Thin File Flag (Less than 3 years of history)
    CASE WHEN ch.cb_person_cred_hist_length < 3 THEN 1 ELSE 0 END AS thin_file_flag,
    c.person_home_ownership,
    ch.loan_grade
FROM fact_loans_final f
JOIN dim_customers c ON f.customer_id = c.customer_id
JOIN dim_credit_history ch ON f.customer_id = ch.customer_id;
"""

cursor.executescript(sql_gold_layer)
conn.commit()
conn.close()
print("Complete")
-- 1. Create a Clean Reporting View
-- This joins everything into a single 'Gold' table for the BI tool
DROP VIEW IF EXISTS view_gold_loan_strategy;

CREATE VIEW view_gold_loan_strategy AS
SELECT 
    f.loan_id,
    f.loan_amnt,
    f.loan_int_rate,
    f.prob_default,
    f.expected_loss,
    f.expected_profit,
    f.risk_segment,
    -- Senior Logic: Categorize loans into actionable 'buckets' via SQL
    CASE 
        WHEN f.prob_default < 0.10 THEN 'Tier 1: Core'
        WHEN f.prob_default < 0.25 THEN 'Tier 2: Growth'
        WHEN f.prob_default < 0.50 THEN 'Tier 3: High Yield'
        ELSE 'Tier 4: Toxic'
    END AS strategic_tier,
    -- Financial Health Flag
    CASE 
        WHEN f.expected_profit > 0 THEN 'Profitable'
        ELSE 'Loss-Making'
    END AS profit_status,
    c.person_income,
    c.person_home_ownership,
    ch.loan_grade
FROM fact_loans_final f
JOIN dim_customers c ON f.customer_id = c.customer_id
JOIN dim_credit_history ch ON f.customer_id = ch.customer_id;
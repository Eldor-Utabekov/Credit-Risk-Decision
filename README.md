# 📊 Credit Risk Strategy & Profit Optimization Dashboard

This project presents a decision-oriented analytical framework designed to evaluate and optimize loan approval strategies within a retail banking environment. Rather than focusing on static reporting, the goal is to simulate how different credit policies influence profitability, risk exposure, and portfolio composition in real time. The dashboard reflects how experienced data analysts contribute to credit strategy by translating raw data into actionable financial decisions.

At the current state, the portfolio reveals a structurally negative outcome. While approved loans generate a small positive return of approximately **$49K**, the overall portfolio performance is significantly negative, with projected losses of **$84.91M** and a net result of **-53.53M**. At the same time, the approval rate remains extremely low at **7%**, paired with an average probability of default of **1.45%**.

This combination is critical. A low approval rate typically indicates a conservative strategy, yet losses remain disproportionately high. This suggests that the issue is not simply how many loans are approved, but **which loans are being approved**. In other words, the selection mechanism is inefficient ⚠️.

---

## 🔍 Analytical Approach

The core of the solution is built around **Probability of Default (PD)** as the central decision variable. By introducing a dynamic threshold, the dashboard allows simulation of different approval strategies and their direct financial impact.

This transforms the analysis from:
- retrospective (“what happened”)  
to  
- prescriptive (“what should we do”)  

As the PD threshold increases, approval rates grow steadily, but losses accelerate much faster. This creates a clear **non-linear risk-return relationship**, where profitability reaches a peak and then declines sharply 📉.

---

## 📈 Profitability Dynamics

The profit optimization curve reveals a key insight:  
there exists a **narrow optimal zone** where the trade-off between risk and return is balanced.

- At very low thresholds → approvals are minimal → profit is limited  
- At moderate thresholds → profit reaches maximum  
- At high thresholds → losses dominate → profit collapses  

This behavior highlights a classic issue in credit portfolios:  
**growth beyond a certain point destroys value instead of creating it**.

---

## 💣 Loss vs Volume Trade-off

One of the most important findings comes from comparing portfolio loss with approval volume.

While approval rate increases roughly linearly, losses grow in a **convex manner**, meaning:

> Each additional approved loan adds disproportionately more risk than revenue.

This indicates that marginal borrowers (those just above the threshold) are significantly riskier and contribute heavily to losses. In practical terms, the bank is **overexposed to tail risk**.

---

## 🧩 Segment-Level Insights

A deeper breakdown of the portfolio uncovers structural inefficiencies in how capital is allocated.

The majority of exposure is concentrated in:
- High Risk segments  
- Speculative (Reject) segments  

Meanwhile, lower-risk (prime) customers represent a relatively small portion of approved exposure.

This imbalance suggests that the portfolio is **not optimized for stability or long-term profitability**. Instead of leveraging safer segments, capital is disproportionately tied to high-risk borrowers, which amplifies volatility and loss potential.

Additionally, segmentation by income and debt-to-income (DTI) reveals further inefficiencies:
- Higher-risk profiles are not sufficiently filtered out  
- Stronger borrower profiles are underutilized  

This points to a lack of **segment-specific strategy**, where all customers are treated under a similar threshold rather than differentiated policies.

---

## ⚖️ Strategy Inefficiency

Perhaps the most important insight is the contradiction between:
- Low approval rate (7%)  
- High total losses ($84.91M)  

In a well-functioning system, stricter approvals should reduce losses significantly. The fact that this is not happening indicates:

1. Weak risk ranking (model limitation)  
2. Misaligned threshold strategy  
3. Lack of proper risk-based pricing  

This is a strong signal that the issue lies in **decision quality, not decision quantity**.

---

## 💡 Strategic Interpretation

From a business perspective, the current portfolio behaves as if:
- Risk is underestimated in key segments  
- High-risk loans are not sufficiently compensated  
- Approval decisions are not aligned with financial outcomes  

The data suggests that simply tightening or loosening approvals is not enough. What is required is a **more intelligent allocation of approvals**, where decisions are guided by both risk and expected value.

---

## 🚀 Key Recommendations

The analysis supports several strategic directions.

First, the PD threshold should be calibrated closer to the observed profitability peak, where the marginal trade-off between risk and return is optimal. Operating outside this zone leads to rapid deterioration in performance.

Second, the portfolio should be actively rebalanced toward lower-risk segments. Increasing exposure to prime customers would stabilize returns and reduce sensitivity to default spikes.

Third, the current loss dynamics strongly indicate a need for **risk-based pricing**. High-risk borrowers appear underpriced, meaning the interest rates do not adequately compensate for expected losses.

Finally, the results suggest an opportunity to improve the underlying risk model. The inability to reduce losses despite low approval rates typically reflects limited predictive power. Enhancing feature sets or recalibrating the model would directly improve decision quality.

---

## 🏗️ Technical Implementation

The project is built using a structured analytical pipeline:

- Python for data extraction and transformation  
- SQL for building a clean analytical layer  
- Power BI for delivering an interactive decision interface  

A Python-based connector is used to load data directly into Power BI, ensuring reproducibility and simplifying integration between the data layer and the reporting environment.

---

## 🎯 Business Impact

This project demonstrates how data analysis can move beyond reporting and become a **decision-making tool**.

It enables:
- Real-time simulation of credit policies  
- Quantification of financial trade-offs  
- Identification of structural inefficiencies in the portfolio  

Most importantly, it shows how a data analyst can bridge the gap between **risk metrics and business strategy**, which is a critical capability in banking and fintech environments.
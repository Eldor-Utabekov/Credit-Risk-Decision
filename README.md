# 📊 Credit Risk Analytics & Exposure Coverage Dashboard

## Overview

This project presents a **decision-oriented credit risk analytics framework** designed to evaluate loan portfolio quality and support risk-aware decision-making.

The solution focuses on **Probability of Default (PD)** as the primary risk signal and extends the analysis to include **Exposure at Default (EAD)** and **basic collateral coverage**, reflecting how credit risk is monitored in real-world financial environments.

The dashboard is built to move beyond static reporting by enabling **interactive exploration of risk thresholds, portfolio composition, and expected loss dynamics**.

---

## 🎯 Objective

To analyze how borrower risk (PD) translates into **portfolio-level exposure and expected loss**, and to assess whether these risks are sufficiently supported by collateral.

---

## 📈 Executive Insight: Portfolio Risk Imbalance

The analysis reveals a structural imbalance in the portfolio:

* A relatively **low approval rate**
* Yet **disproportionately high projected losses**
* Risk is concentrated in a **small subset of high-PD exposures**

This suggests that:

> The issue is not the volume of approvals, but the **quality of risk selection**

---

## 🔍 Analytical Approach

### 1. PD-Centric Risk Analysis

The core of the framework is built around **Probability of Default (PD)**:

* Used to segment borrowers
* Identify high-risk cohorts
* Evaluate risk distribution across the portfolio

A dynamic **PD threshold parameter** allows simulation of different approval strategies, helping answer:

> *What happens to portfolio risk if we accept more or fewer borrowers?*

---

### 2. Exposure & Expected Loss

Risk is translated into financial impact using:

[
\text{Expected Loss (EL)} = PD \times EAD
]

This enables:

* Quantification of **risk in monetary terms**
* Identification of **loss-driving segments**
* Prioritization of high-risk exposures

---

### 3. Collateral Awareness (Supporting Layer)

To make the analysis more realistic, a **basic collateral layer** is included.

The goal is not to model collateral in depth, but to answer a practical question:

> *Are risky exposures sufficiently covered?*

Key elements:

* Collateral value vs exposure comparison
* Coverage ratio (Collateral / EAD)
* Identification of **under-collateralized loans**

This reflects how collateral is used in practice:

> as a **risk mitigant**, not a standalone analytical system

---

## 🧩 Key Insights

### Risk Concentration

* A small portion of loans contributes disproportionately to **Expected Loss**
* Portfolio exhibits a **fat-tail risk distribution**

### Segment-Level Differences

* Certain loan purposes and borrower profiles show consistently higher PD
* Borrower characteristics (income, DTI, employment length) influence risk levels

### Exposure vs Coverage

* Some high-risk loans are also **weakly collateralized**
* These represent the most critical risk pockets

---

## 🚀 Practical Implications

* **Risk Selection Improvement**
  Refine approval thresholds to reduce concentration of high-risk exposures

* **Portfolio Monitoring**
  Track Expected Loss as a core risk KPI alongside PD

* **Collateral Awareness**
  Use coverage metrics to flag potentially vulnerable positions

---

## 🏗️ Technical Implementation

### Python

Used for:

* Data cleaning and transformation
* Feature preparation (PD, exposure-related fields)
* Exploratory analysis

> Since this is a personal project based on a public dataset, Python was used as the primary environment for flexibility and speed of iteration.

**In a production setting:**

* Data transformations would typically be handled via **SQL pipelines or data warehouse layers**
* Python would be used selectively for advanced analysis or modeling

---

### SQL

* Logical data structuring
* Preparation of analysis-ready tables (conceptually modeled)

---

### Power BI

* Interactive dashboard
* DAX measures for:

  * Expected Loss (SUMX-based)
  * Risk segmentation
  * Dynamic threshold analysis

---

## 🎯 Role Alignment

This project reflects the work of a **Data Analyst operating in a credit risk context**, with responsibilities such as:

* Analyzing and interpreting **risk model outputs (PD)**
* Translating risk into **business-relevant metrics (Expected Loss)**
* Supporting decision-making through **data visualization**
* Incorporating **basic collateral awareness** to enhance analysis realism

It also demonstrates an interest in expanding toward:

* **Exposure and collateral analysis**
* Broader financial risk frameworks

---

## 💡 Key Takeaway

> The project demonstrates how credit risk metrics (PD) can be translated into actionable insights by combining exposure analysis and simple collateral context—bridging the gap between raw model outputs and business decision-making.

---

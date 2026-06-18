# 📊 Task 3: Interactive Executive Dashboard (Power BI)

## 📌 Project Overview
This module converts clean transactional data into an enterprise-grade business intelligence dashboard using **Power BI Desktop**. The design prioritizes quick scanning via an intuitive, corporate-ready layout.

---

## 💡 1. Core Analytics Metrics (DAX Engine)
Rather than using basic column drops, the dashboard relies on custom **Data Analysis Expressions (DAX)** to calculate precise operational health metrics:

* **Total Revenue:** Gross line value metrics.
  $$Total\ Revenue = \sum(cleaned\_amazon\_sales[Total\_Sales\_Value])$$
* **Total Orders:** Distinct transactional traffic velocity.
  $$Total\ Orders = DISTINCTCOUNT(cleaned\_amazon\_sales[Order\ ID])$$
* **Average Order Value (AOV):** Dynamic basket check sizing.
  $$Average\ Order\ Value = \frac{[Total\ Revenue]}{[Total\ Orders]}$$

---

## 🎨 2. Streamlined Dashboard Matrix

### Header & Controls
* **Semantic Title:** Bold top banner instantly establishing report scope.
* **Control Panels (Slicers):** Top-right interactive tiles filtering the entire canvas by **Order Urgency** (High Priority vs. Standard) and **B2B Profiles** (Corporate vs. Retail).

### 📈 Executive KPI Row
* **Core Scorecards:** High-impact metric cards positioned horizontally across the top line for instant health checks:
  * **Total Revenue:** Gross financial sales performance (₹75.51M).
  * **Total Orders:** Transactional order volume (120K).
  * **Average Order Value (AOV):** Average retail basket size (₹631.46).

### Analytical Views
* **Product Engine (Center-Left):** Horizontal Bar Chart ranking top-performing product categories.
* **Logistics Split (Bottom-Left):** Donut Chart showing fulfillment reliance (FBA: **72.06%** vs. Merchant: **27.94%**).
* **Demographic Density (Right-Wing):** Proportional TreeMap highlighting market share across Indian states (Primary hubs: Maharashtra, Karnataka, and Telangana).
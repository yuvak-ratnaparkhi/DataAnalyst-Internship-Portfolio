# 📊 Task 3: Interactive Executive Dashboard & Business Intelligence

## 📌 Project Overview
This module transforms processed e-commerce transactional data into an interactive, enterprise-grade executive dashboard using **Power BI Desktop**. The project focuses on converting raw sales metrics into structured, scannable business insights via an optimized user interface, enabling stakeholders to make data-driven supply chain and regional market decisions.

---

## 🛠️ Core Technical Competencies
* **Advanced DAX Engineering:** Created explicit measures rather than relying on default implicit column summaries.
* **UI/UX Dashboard Design:** Built a clean, executive-ready dashboard following modern corporate design principles (synchronized layouts, color contrast preservation, and high data-to-ink ratio).
* **Data Granularity Management:** Implemented performance-focused visuals by filtering out low-velocity dimensions (Top N filtering) to highlight macro-level business drivers.

---

## 💡 1. Analytical Metrics (DAX Engine)
To monitor operational health and transaction velocity across the retail network, the following primary Key Performance Indicators (KPIs) were engineered:

* **Total Revenue:** Measures gross top-line commercial scale.
  $$Total\_Revenue = \sum(cleaned\_amazon\_sales[Total\_Sales\_Value])$$
* **Total Orders:** Tracks transaction volume density independent of price fluctuations.
  $$Total\_Orders = DISTINCTCOUNT(cleaned\_amazon\_sales[Order\_ID])$$
* **Average Order Value (AOV):** Quantifies the financial weight of an average consumer basket.
  $$Average\_Order\_Value = \frac{[Total\_Revenue]}{[Total\_Orders]}$$

---

## 🎨 2. Executive Dashboard Architecture

### 🎛️ Navigation & Control Filters
* **Interactive Slicers:** Features responsive, clean tile controls at the top-right to dynamically filter the entire canvas by **Order Urgency** (High Priority vs. Standard) and **B2B Profiles** (Corporate vs. Retail).

### 📈 Balanced Health Metric Cards
* **High-Impact Scorecards:** Placed horizontally across the top line for immediate visual scannability:
  * **Total Revenue:** ₹75.51M
  * **Total Orders:** 120K
  * **Average Order Value (AOV):** ₹631.46

### 🔍 Deep-Dive Analytical Visuals
* **Product Performance (Center-Left):** A horizontal bar chart identifying product line concentration. Features explicit data labels for fast reading, showing that *Sets and Kurtas drive over 75% of total revenue*.
* **Logistics Distribution (Bottom-Left):** A clean donut chart breaking down fulfillment reliance, highlighting a **72.06%** usage rate of the **Amazon FBA** network.
* **Geographical Market Shares (Right-Wing):** A tailored, clutter-free **Top 10 State TreeMap** mapping national distribution density. It instantly flashes major sales hubs (led by *Maharashtra and Karnataka*) without microscopic tail-end clutter.

---

## 🔗 3. Project Deliverables
* 🌐 **Interactive Workbook:** [Download Power BI Dashboard File (Amazon_Executive_Dashboard.pbix)](./Amazon_Executive_Dashboard.pbix) *(Download and open in Power BI Desktop to interact with the live model)*
* 📝 **Technical Report:** `Deep_Dive_Report.md` — Formal business intelligence documentation detailing core insights and strategic recommendations.
# 📁 Task 1: Data Dictionary (Amazon Sales Report)

## 📌 Data Architecture Overview
* **Target Dataset:** Raw Amazon Seller Central Fulfillment Report
* **Dataset Shape:** 128,968 initial rows | 24 core transactional attributes
* **Pipeline Focus:** Type casting, null imputation, artifact removal, and feature engineering

---

## 📊 Core Operational Schema

| Column Name | Data Type | Key Functional Description | Business Metric Focus |
| :--- | :--- | :--- | :--- |
| `Order ID` | String | Unique transaction hash | Tracks unique volume & receipts |
| `Date` | Datetime | Standarized order placement timestamp | Powers velocity & trend seasonality |
| `Status` | String | Operational/Delivery status | Monitors bottlenecks & cancellations |
| `Fulfilment` | String | Shipping route channel (FBA vs. FBM) | Evaluates third-party reliance metrics |
| `SKU` | String | Warehouse Stock Keeping Unit ID | Identifies core inventory movement |
| `Category` | String | Product line high-level grouping | Guides high-level marketing strategy |
| `Qty` | Integer | Total invoice unit count | Tracks stock depletion rates |
| `Amount` | Float | Base product price per single unit | Measures baseline unit margins |
| `Total_Sales_Value`| Float | **Engineered Feature:** `Qty` $\times$ `Amount` | Isolates true gross line item revenue |
| `Order_Urgency` | String | **Engineered Feature:** Logistics speed bracket | Groups and monitors courier priority |

---

## 🛠️ Automated Transformation Highlights
* **Artifact Stripping:** Dropped structural database remnants (`index`, `Unnamed: 22`).
* **Format Standardization:** Cast highly volatile mixed-string date variants into a single strict `YYYY-MM-DD` datetime index.
* **Smart Gaps Imputation:** Filled structural blanks in categorical text fields cleanly with default operational flags (**"No Promo"**, **"FBA Logistics"**).
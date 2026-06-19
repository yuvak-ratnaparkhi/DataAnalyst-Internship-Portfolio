# 📊 Task 2: Exploratory Data Analysis (EDA) Report

## 📌 Objective
To uncover deep structural distributions, core trends, and performance dependencies within the cleaned Amazon E-Commerce dataset using combined programmatic Python processing and a local live PostgreSQL relational database server.

---

## 🛠️ 1. Data Engineering & Descriptive Architecture
The exploration split into univariate distribution checks and descriptive metrics using Pandas pipelines (`eda_bi_analysis.py`) to systematically map metrics out before loading the schema into an enterprise PostgreSQL engine via SQLAlchemy.

### Saved Analytical Plot Deliverables:
* `sales_distribution.png`: Evaluates baseline unit transaction sizing distributions.
* `category_revenue.png`: Highlights category concentration dominance (Led heavily by `Set` and `Kurta`).
* `top_states_revenue.png`: Measures geographical density patterns across core destination hubs.
* `urgency_vs_value.png`: Explores operational logistics correlation variations.

---

## 💾 2. Relational Database Extraction (Production PostgreSQL Engine Results)
To satisfy database systems compliance, SQL queries were executed against a live PostgreSQL server inside VS Code (`amazon_business_queries.sql`) to extract clean, formatted transaction metrics:

### Q1: Macro Financial Performance

total_gross_revenue | total_unique_orders | average_order_value
--------------------+---------------------+--------------------
76,130,093.20 INR   | 120,378             | 632.43 INR

### Q2: Top 5 Product Categories by Revenue

category      | category_revenue    | total_orders
--------------+---------------------+--------------
Set           | 37,982,764.00 INR   | 47,845
kurta         | 20,706,954.00 INR   | 46,561
Western Dress | 10,710,908.00 INR   | 14,994
Top           |  5,245,007.20 INR   | 10,155
Ethnic Dress  |    762,949.00 INR   |  1,148

### Q.3: Fulfillment Model Split

fulfilment | fulfillment_revenue | revenue_percentage
-----------+---------------------+-------------------
Amazon     | 54,809,834.20 INR   | 71.99%
Merchant   | 21,320,259.00 INR   | 28.01%

### Q4: Top 5 Indian States by Transaction Traffic

state         | state_revenue       | order_count
--------------+---------------------+-------------
MAHARASHTRA   | 12,936,412.00 INR   | 20,780
KARNATAKA     | 10,222,900.00 INR   | 16,182
TELANGANA     |  6,705,327.00 INR   | 10,405
UTTAR PRADESH |  6,555,128.00 INR   | 10,062
TAMIL NADU    |  6,326,578.00 INR   | 10,519

### Q5: B2B Commercial Accounts vs B2C Retail Profiles

customer_segment | total_orders | segment_revenue    | average_order_value
-----------------+--------------+--------------------+--------------------
B2C Retail       | 119,584      | 75,512,913.20 INR  | 589.50 INR
B2B Commercial   | 794          |    617,180.00 INR  | 708.59 INR

### Q6: Order Urgency Impact on Transaction Basket Value

order_urgency    | total_orders | urgency_revenue    | average_basket_value
-----------------+--------------+--------------------+--------------------
High Priority    | 82,922       | 54,674,057.00 INR  | 617.03 INR
Standard         | 37,456       | 21,456,036.20 INR  | 531.62 INR
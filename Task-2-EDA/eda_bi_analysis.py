import pandas as pd
import numpy as np

# Load the clean dataset generated in Task 1
print("--- Loading Cleaned Amazon Dataset ---")
df = pd.read_csv('Task-1-Data-Wrangling/cleaned_amazon_sales.csv', low_memory=False)

print(f"Successfully loaded {len(df)} production-ready records.")

# ==========================================================
# STEP 1: DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS
# ==========================================================
print("\n=== Summary Statistics for Numerical Fields ===")
print(df[['Qty', 'Amount', 'Total_Sales_Value']].describe())

# ==========================================================
# STEP 2: SQL FOR BUSINESS QUESTIONS (Using Pandas Aggregations)
# ==========================================================
print("\n=== Executing Business Intelligence Queries ===")

# Q1: Top Product Categories by Total Revenue
print("\n[Q1] Top Product Categories by Revenue:")
q1_revenue = df.groupby('Category')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
q1_revenue['Percentage'] = (q1_revenue['Total_Sales_Value'] / q1_revenue['Total_Sales_Value'].sum()) * 100
print(q1_revenue.head(5).to_string(index=False))

# Q2: Sales Channel Distribution
print("\n[Q2] Revenue by Sales Channel:")
q2_channel = df.groupby('Sales Channel')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
print(q2_channel.to_string(index=False))

# Q3: Fulfillment Strategy Performance
print("\n[Q3] Fulfillment Method Analysis:")
q3_fulfilment = df.groupby('Fulfilment').agg(
    Total_Revenue=('Total_Sales_Value', 'sum'),
    Total_Orders=('Order ID', 'nunique')
).reset_index()
print(q3_fulfilment.to_string(index=False))

# Q4: Top 5 Consumer States by Revenue
print("\n[Q4] Top 5 States by Revenue Contribution:")
# Clean up state strings to fix case issues
df['ship-state'] = df['ship-state'].str.upper().str.strip()
q4_states = df.groupby('ship-state')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
print(q4_states.head(5).to_string(index=False))

# Q5: B2B vs Consumer Market Share
print("\n[Q5] B2B Transaction Share Evaluation:")
q5_b2b = df.groupby('B2B')['Order ID'].nunique().reset_index(name='Order_Count')
q5_b2b['Share_Percentage'] = (q5_b2b['Order_Count'] / q5_b2b['Order_Count'].sum()) * 100
print(q5_b2b.to_string(index=False))

# Q6: Order Urgency vs Average Transaction Amount (Multivariate Check)
print("\n[Q6] Average Order Value (AOV) by Shipping Priority:")
q6_urgency = df.groupby('Order_Urgency')['Total_Sales_Value'].mean().reset_index(name='Average_Order_Value')
print(q6_urgency.to_string(index=False))

print("\n--- Business Intelligence Extraction Pipeline Complete ---")
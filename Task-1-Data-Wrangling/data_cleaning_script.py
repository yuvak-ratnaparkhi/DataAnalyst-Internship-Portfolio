import pandas as pd
import numpy as np

# ==========================================
# PHASE 1 & 2: LOADING & ASSESSMENT
# ==========================================
print("--- Loading Raw Amazon Dataset ---")
raw_path = 'Task-1-Data-Wrangling/Amazon Sale Report.csv'
df = pd.read_csv(raw_path, low_memory=False)

print(f"\n[Assessment] Total Initial Records: {len(df)}")
print("\n[Assessment] Missing Values Breakdown:")
print(df.isnull().sum())

# ==========================================
# PHASE 3: CLEANING & PIPELINE TRANSFORMATION
# ==========================================
print("\n--- Executing Cleaning Operations ---")

# 1. Drop useless indexing and artifact columns
cols_to_drop = ['index', 'Unnamed: 22']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# 2. Strip any accidental trailing whitespaces from column headers
df.columns = df.columns.str.strip()

# 3. Handle duplicates
duplicate_count = df.duplicated(subset=['Order ID', 'SKU']).sum()
print(f"-> Found and removing {duplicate_count} duplicate item transactions...")
df = df.drop_duplicates(subset=['Order ID', 'SKU'])

# 4. Standardize Date Formats
print("-> Standardizing order timelines...")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')

# 5. Handle missing values in numerical currency metrics
# If Amount is missing but Qty is present, we impute the missing price using the median price of that category
df['Amount'] = df.groupby('Category')['Amount'].transform(lambda x: x.fillna(x.median()))
# Fallback for any leftover missing amounts
df['Amount'] = df['Amount'].fillna(df['Amount'].median())

# Fix the blank spaces in promotions and fulfillment methods
df['promotion-ids'] = df['promotion-ids'].fillna('No Promo')
df['fulfilled-by'] = df['fulfilled-by'].fillna('FBA Logistics')

# 6. Fill categorical gaps with explicit placeholders
df['Courier Status'] = df['Courier Status'].fillna('Unknown')
df['currency'] = df['currency'].fillna('INR')

# ==========================================
# PHASE 4: FEATURE ENGINEERING
# ==========================================
print("\n--- Engineering Strategic Business Features ---")

# Feature 1: Total Sales Revenue Formula
df['Total_Sales_Value'] = df['Qty'] * df['Amount']

# Feature 2: Logistic Categorization Map
def segment_urgency(service_level):
    if pd.isna(service_level): 
        return 'Standard'
    elif 'Expedited' in str(service_level): 
        return 'High Priority'
    else: 
        return 'Standard'

df['Order_Urgency'] = df['ship-service-level'].apply(segment_urgency)

# ==========================================
# PHASE 5: EXPORT PRODUCTION EXCEL/CSV
# ==========================================
cleaned_path = 'Task-1-Data-Wrangling/cleaned_amazon_sales.csv'
df.to_csv(cleaned_path, index=False)

print(f"\nSuccess! Cleaned, analysis-ready dataset saved to: {cleaned_path}")
print(f"Final safe record count: {len(df)}")
print("\n--- Pipeline Check (First 5 Rows) ---")
print(df[['Order ID', 'Date', 'Qty', 'Amount', 'Total_Sales_Value', 'Order_Urgency']].head())
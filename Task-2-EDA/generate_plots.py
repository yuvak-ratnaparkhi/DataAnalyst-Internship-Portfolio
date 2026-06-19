import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean visualization style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load dataset
df = pd.read_csv('../Task-1-Data-Wrangling/cleaned_amazon_sales.csv', low_memory=False)
df['ship-state'] = df['ship-state'].str.upper().str.strip()

print("--- Generating Synchronized Task 2 Visualization Assets ---")

# 1. Distribution of Total Sales Value (Univariate Analysis Chart)
plt.figure()
sns.histplot(df[df['Total_Sales_Value'] < 2000]['Total_Sales_Value'], bins=40, kde=True, color='teal')
plt.title('Distribution of Total Sales Value (Filtered < 2000 INR for Clarity)')
plt.xlabel('Total Sales Value (INR)')
plt.ylabel('Transaction Count')
plt.tight_layout()
plt.savefig('assets/sales_distribution.png')
plt.close()

# 2. Revenue by Product Category (Bar Chart - Matches Q2)
plt.figure()
q2_data = df.groupby('Category')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
sns.barplot(x='Total_Sales_Value', y='Category', data=q2_data.head(5), palette='Blues_r')
plt.title('Top 5 Product Categories by Generated Revenue')
plt.xlabel('Total Revenue (INR)')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('assets/category_revenue.png')
plt.close()

# 3. Top States by Revenue (Bar Chart - Matches Q4)
plt.figure()
q4_data = df.groupby('ship-state')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
sns.barplot(x='Total_Sales_Value', y='ship-state', data=q4_data.head(5), palette='viridis')
plt.title('Top 5 Consuming States by Total Sales Revenue')
plt.xlabel('Total Revenue (INR)')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('assets/top_states_revenue.png')
plt.close()

# 4. Shipping Urgency vs Average Order Value (Multivariate Chart - Matches Q6)
plt.figure()
# Filtered < 2000 INR to eliminate outliers and show a clean distribution boxplot
sns.boxplot(x='Order_Urgency', y='Total_Sales_Value', data=df[df['Total_Sales_Value'] < 2000], palette='Set2')
plt.title('Transaction Value Spread by Shipping Urgency Priority')
plt.xlabel('Shipping Priority Class (High Priority vs Standard)')
plt.ylabel('Total Sales Value (INR)')
plt.tight_layout()
plt.savefig('assets/urgency_vs_value.png')
plt.close()

print("🚀 Success! All 4 analytics charts synchronized and updated in 'Task-2-EDA/assets/'.") 
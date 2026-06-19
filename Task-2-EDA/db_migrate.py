import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

# 1. Load your local Task 1 dataset
csv_path = "../Task-1-Data-Wrangling/cleaned_amazon_sales.csv"
df = pd.read_csv(csv_path, low_memory=False)

# 2. Clean column headers for strict SQL compliance (lowercase, no spaces, no hyphens)
df.columns = [c.lower().replace("-", "_").replace(" ", "_") for c in df.columns]

raw_password = "Yuvak@2027"
safe_password = urllib.parse.quote_plus(raw_password)

# 2. Generate the safe connection engine string
engine = create_engine(f"postgresql://postgres:{safe_password}@localhost:5432/amazon_analytics_db")

# 4. Stream rows directly into a new target table
print("⏳ Migrating 120k+ records to PostgreSQL target table...")
df.to_sql("amazon_sales", engine, index=False, if_exists="replace")
print("✅ Success! The 'amazon_sales' table is now live in your database.")
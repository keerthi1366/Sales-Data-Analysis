# data_cleaning.py
# --------------------------------------------------
# Author: Lella Sai Keerthi
# Project: Sales Data Analysis for Power BI
# Description: This script cleans the Sample Superstore dataset
#              and saves a cleaned version for Power BI Dashboard.

import pandas as pd

# Load dataset
print("📥 Loading dataset...")
df = pd.read_csv(r"C:\Users\keert\Downloads\supermarket-data\Sample - Superstore.csv", encoding='latin1')

# Inspect the first few rows
print("✅ Data loaded successfully. Shape:", df.shape)

# Step 1: Remove duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Step 2: Strip column names (remove spaces)
df.columns = df.columns.str.strip()

# Step 3: Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Step 4: Ensure numeric columns are properly formatted
numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 5: Save the cleaned dataset
cleaned_file = "cleaned_sales_data.csv"
df.to_csv(cleaned_file, index=False)

print(f"🎉 Cleaned dataset saved as {cleaned_file}")
print("Rows and columns after cleaning:", df.shape)
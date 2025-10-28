# Sales Data Analysis using Python
This project performs exploratory data analysis (EDA) and sales forecasting using Python on the Sample Superstore dataset.
It helps uncover sales trends, top-performing products, and profit insights — and prepares a cleaned dataset for Power BI visualization.
Sales Data Analysis and Dashboard — A complete data analytics project using Python and Power BI to clean, analyze, forecast, and visualize Superstore sales data for actionable business insights.
# 📊 Sales Data Analysis Dashboard

This project showcases an **end-to-end Sales Data Analysis** pipeline built using **Python (for data cleaning)** and **Power BI (for interactive dashboard visualization)**.  
The goal is to extract insights into sales performance, profit trends, and regional performance using a real-world dataset.

---

## 📁 Project Overview

### 🔹 Tools & Technologies Used
- **Python** (Pandas, NumPy, Matplotlib)
- **Power BI Desktop**
- **Microsoft Excel / CSV**
- **GitHub** for version control

### 🔹 Objectives
- Clean and preprocess raw sales data using Python.
- Build calculated measures (DAX) for KPIs like:
  - Total Sales  
  - Total Profit  
  - Profit Margin  
  - Total Quantity
- Create an **interactive Power BI dashboard** with filters and insights.

---

## 🧰 Steps & Workflow

### 🧩 Step 1 — Data Cleaning (Python)
- Loaded raw `Sample Superstore.csv`
- Removed duplicates and null values
- Standardized column names
- Converted `Order Date` and `Ship Date` columns to datetime format
- Saved the cleaned dataset as: cleaned_sales_data.csv
### 📊 Step 2 — Data Modeling in Power BI
Imported cleaned_sales_data.csv into Power BI.

Created calculated measures:
- Total Sales = SUM('cleaned_sales_data'[Sales])
- Total Profit = SUM('cleaned_sales_data'[Profit])
- Total Quantity = SUM('cleaned_sales_data'[Quantity])
- Profit Margin = DIVIDE([Total Profit], [Total Sales])
Verified relationships and ensured correct data types (Dates, Numbers, Categories).

### 📈 Step 3 — Dashboard Creation
<img width="1019" height="569" alt="Screenshot 2025-10-28 171611" src="https://github.com/user-attachments/assets/275c9829-d5fb-4fb5-b5f5-263221bac861" />

### 📚 Key Insights
 - 📈 Highest Sales from the West Region and Technology Category.
 - 💰 Office Supplies had lower profit margins despite high sales volume.
 - 🚚 Same Day ship mode was most cost-efficient for profit.
 - 🧭 California and New York were top-performing states.

### Repository Structure

📦 Sales-Data-Analysis
├── Cleaned_Superstore_Sample.csv
├── Sample Superstore.csv
├── analysis.pbix
├── data_cleaning.py
├── dashboard_preview.png
└── README.md

### 🚀 How to Use
1. Clone this repository:
    git clone https://github.com/keerthi1366/Sales-Data-Analysis.git
2. Open data_cleaning.py and run to generate the cleaned CSV.
3. Open sales_dashboard.pbix in Power BI Desktop.
4. Explore the interactive dashboard with filters and insights.



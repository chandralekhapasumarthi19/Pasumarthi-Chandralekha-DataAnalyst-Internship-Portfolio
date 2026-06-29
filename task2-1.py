import os
import pandas as pd
import sqlite3

base_dir = os.path.dirname(os.path.dirname(__file__))   # go up from python_files to data analytics
csv_path = os.path.join(base_dir, "datasets", "transactions_cleaned.csv")
df = pd.read_csv(csv_path)


# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Load the dataframe into the database as a table
df.to_sql("transactions", conn, index=False, if_exists="replace")

# 1. Top 5 products by revenue in the last 6 months
query1 = """
SELECT ProductCategory, SUM(Amount) AS TotalRevenue
FROM transactions
WHERE TransactionDate >= date('now','-6 months')
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC
LIMIT 5;
"""
print("Top 5 Products by Revenue (Last 6 Months):")
print(pd.read_sql(query1, conn), "\n")

# 2. Monthly user acquisition trend
query2 = """
SELECT strftime('%Y-%m', TransactionDate) AS Month,
       COUNT(DISTINCT CustomerID) AS NewUsers
FROM transactions
WHERE TransactionDate IS NOT NULL
GROUP BY Month
ORDER BY Month;
"""
print("Monthly User Acquisition Trend:")
print(pd.read_sql(query2, conn), "\n")

# 3. Average spend per customer
query3 = """
SELECT CustomerID, AVG(Amount) AS AvgSpend
FROM transactions
GROUP BY CustomerID
ORDER BY AvgSpend DESC;
"""
print("Average Spend per Customer:")
print(pd.read_sql(query3, conn), "\n")

# 4. Revenue by product category
query4 = """
SELECT ProductCategory, SUM(Amount) AS Revenue
FROM transactions
GROUP BY ProductCategory
ORDER BY Revenue DESC;
"""
print("Revenue by Product Category:")
print(pd.read_sql(query4, conn), "\n")

# 5. Age vs product preference
query5 = """
SELECT CustomerAge, ProductCategory, COUNT(*) AS Purchases
FROM transactions
GROUP BY CustomerAge, ProductCategory
ORDER BY CustomerAge, Purchases DESC;
"""
print("Age vs Product Preference:")
print(pd.read_sql(query5, conn), "\n")

# Close connection
conn.close()
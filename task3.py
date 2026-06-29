import os
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
base_dir = os.path.dirname(os.path.dirname(__file__))   # go up from python_files to data analytics
csv_path = os.path.join(base_dir, "datasets", "sales.csv")
df = pd.read_csv(csv_path)

# Display Dataset
print("===== DATASET =====")
print(df)

# KPI Calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["OrderID"].count()

average_sales = df["Sales"].mean()

print("\n===== KPI RESULTS =====")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Sales:", round(average_sales, 2))

# Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum()

print("\n===== REGION WISE SALES =====")
print(region_sales)

# Category-wise Profit
category_profit = df.groupby("Category")["Profit"].sum()

print("\n===== CATEGORY WISE PROFIT =====")
print(category_profit)

# Top Products by Sales
top_products = df.sort_values(by="Sales", ascending=False)

print("\n===== TOP PRODUCTS =====")
print(top_products[["Product", "Sales"]])

# -----------------------------
# Visualization 1
# Region Wise Sales
# -----------------------------
plt.figure(figsize=(6,4))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# -----------------------------
# Visualization 2
# Category Wise Profit
# -----------------------------
plt.figure(figsize=(6,4))
category_profit.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Wise Profit")
plt.ylabel("")
plt.show()

# -----------------------------
# Visualization 3
# Product Sales
# -----------------------------
plt.figure(figsize=(8,4))
plt.bar(df["Product"], df["Sales"])
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

print("\nTask 3 Completed Successfully!")
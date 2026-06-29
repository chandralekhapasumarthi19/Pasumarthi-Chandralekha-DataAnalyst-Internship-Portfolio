import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.dirname(__file__))   # go up from python_files to data analytics
csv_path = os.path.join(base_dir, "datasets", "transactions_cleaned.csv")

# Load the cleaned dataset
df = pd.read_csv(csv_path)

# --- Correlation Heatmap ---
corr = df[['Amount', 'CustomerAge']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# --- Scatter Plot: Age vs Amount ---
sns.scatterplot(x='CustomerAge', y='Amount', data=df)
plt.title("Customer Age vs Transaction Amount")
plt.show()

# --- Pair Plot: Explore multiple relationships ---
sns.pairplot(df[['Amount', 'CustomerAge']])
plt.show()

# --- Grouped Analysis: Spend by Product Category ---
sns.boxplot(x='ProductCategory', y='Amount', data=df)
plt.title("Spending by Product Category")
plt.xticks(rotation=45)
plt.show()
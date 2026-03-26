import os

import pandas as pd

# Load the sales file for a summary-table example.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_clean.csv"))
sales_df = pd.read_csv(file_path)

print(sales_df)
print()

# Create revenue first so the pivot table has a clear target value.
sales_df["revenue"] = sales_df["quantity"] * sales_df["unit_price"]

print("Original data:")
print(sales_df[["region", "category", "quantity", "unit_price", "revenue"]])

print()

# pivot_table() gives a matrix-style summary for analysis.
revenue_pivot = pd.pivot_table(sales_df,
                               values="revenue",
                               index="region",
                               columns="category",
                               aggfunc="sum",
                               fill_value=0,
                               margins=True)

print("Revenue pivot table:")
print(revenue_pivot)

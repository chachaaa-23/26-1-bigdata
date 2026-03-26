import os

import pandas as pd

# Reuse the sales file from the case study.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_clean.csv"))
sales_df = pd.read_csv(file_path)

print(sales_df)

# shape and columns are quick first checks.
print("Shape:", sales_df.shape)
print("Columns:", sales_df.columns.tolist())

print()

# describe() summarizes numeric columns.
print("Summary statistics:")
print(sales_df[["quantity", "unit_price"]].describe())

print()

# value_counts() is useful for category exploration.
print("Category counts:")
print(sales_df["category"].value_counts())

print()

# normalize=True converts counts to ratios.
print("Customer type ratio:")
print(sales_df["customer_type"].value_counts(normalize=True))

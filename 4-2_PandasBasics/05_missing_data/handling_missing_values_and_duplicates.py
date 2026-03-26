import os

import pandas as pd

# Read the raw sales file again for cleaning practice.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_raw.csv"))

sales_df = pd.read_csv(file_path)

print(sales_df)
print()

sales_df.columns = (sales_df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(" ", "_"))

sales_df["region"] = sales_df["region"].str.strip().str.title()
sales_df["product_name"] = sales_df["product_name"].str.strip()
sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce")
# Mixed date formats are handled with format="mixed".
sales_df["order_date"] = pd.to_datetime(sales_df["order_date"], errors="coerce", format="mixed")

print()

print("Rows before cleaning:", len(sales_df))
print("Duplicate order_id count:", sales_df.duplicated(subset=["order_id"]).sum())

print()

# Fill missing quantity with the median quantity.
sales_df["quantity"] = sales_df["quantity"].fillna(sales_df["quantity"].median())

# Remove duplicated orders and sort by date.
sales_df = sales_df.drop_duplicates(subset=["order_id"])
sales_df = sales_df.sort_values("order_date")
sales_df["quantity"] = sales_df["quantity"].astype(int)

print("Rows after cleaning:", len(sales_df))

print()

print("Cleaned and sorted data:")
print(sales_df[["order_id", "order_date", "region", "product_name", "quantity"]])

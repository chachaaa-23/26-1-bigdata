import os

import pandas as pd

# Load the same raw sales file used in the session.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_raw.csv"))

sales_df = pd.read_csv(file_path)

print("Original Data:")
print(sales_df)

print()

# Standardize column names to snake_case.
sales_df.columns = (sales_df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(" ", "_"))

print("Cleaned columns:")
print(sales_df.columns.tolist())

print()

# Clean text columns so the same value is written consistently.
sales_df["region"] = sales_df["region"].str.strip().str.title() #string 앞뒤의 공백제거, 앞대문자 형식으로 변경
sales_df["category"] = sales_df["category"].str.strip().str.title()
sales_df["customer_type"] = sales_df["customer_type"].str.strip().str.title()
sales_df["channel"] = sales_df["channel"].str.strip().str.title()
sales_df["product_name"] = sales_df["product_name"].str.strip()

# Remove the dollar sign, then convert to numbers.
sales_df["unit_price"] = pd.to_numeric(
    sales_df["unit_price"].str.replace("$", "", regex=False),
    errors="coerce" #NaN
)
sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce")

# Mixed date formats are common in raw files.
sales_df["order_date"] = pd.to_datetime(sales_df["order_date"], errors="coerce", format="mixed")

print("Cleaned preview:")
print(sales_df[["order_id", "order_date", "region", "category", "quantity", "unit_price"]])

print()

print("Cleaned types:")
print(sales_df.dtypes)

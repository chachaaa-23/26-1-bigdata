import os

import pandas as pd

# Read the raw sales file again for cleaning practice.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_raw.csv"))

sales_df = pd.read_csv(file_path)

print(sales_df)
print()

sales_df.columns = (sales_df.columns
                    .str.strip() #앞뒤공백 제거
                    .str.lower() #소문자 변경
                    .str.replace(" ", "_")) #change space into _ (단어 사이의 공백 남아있음)

sales_df["region"] = sales_df["region"].str.strip().str.title() #title() : 앞만 대문자인 형식으로 변경
sales_df["product_name"] = sales_df["product_name"].str.strip()
sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce")
# Mixed date formats are handled with format="mixed".
sales_df["order_date"] = pd.to_datetime(sales_df["order_date"], errors="coerce", format="mixed")

print()

print("Rows before 중복치 제거:", len(sales_df)) #행의 개수
print("Duplicate order_id count:", sales_df.duplicated(subset=["order_id"]).sum()) #order id 기준으로 중복치 제거
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

import sqlite3

import pandas as pd

# Load SQL results into pandas for table analysis.
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create a small sales table and sample rows.
cursor.execute("""
CREATE TABLE sales (
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price INTEGER,
    month INTEGER
)
""")

# Prepare sample sales rows.
sales_rows = [
    ("Mouse", "Accessory", 3, 25, 1),
    ("Keyboard", "Accessory", 2, 45, 1),
    ("Monitor", "Display", 1, 180, 2),
    ("Laptop Stand", "Accessory", 4, 30, 2),
    ("Tablet", "Device", 2, 220, 3)
]

cursor.executemany("""
INSERT INTO sales (product_name, category, quantity, unit_price, month)
VALUES (?, ?, ?, ?, ?)
""", sales_rows)

sales_df = pd.read_sql_query("SELECT * FROM sales", connection)
sales_df["sales"] = sales_df["quantity"] * sales_df["unit_price"]

print("Sales DataFrame:")
print(sales_df)

print()

# pandas can summarize the SQL result after loading.
print("Sales by category:")
print(sales_df.groupby("category")["sales"].sum())

connection.close()

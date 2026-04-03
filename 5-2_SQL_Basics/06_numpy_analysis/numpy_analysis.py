import sqlite3

import numpy as np
import pandas as pd

# Load SQL results, then analyze them as NumPy arrays.
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

# Let SQL calculate sales first.
sales_df = pd.read_sql_query("""
SELECT quantity * unit_price AS sales
FROM sales
""", connection)

sales_array = sales_df["sales"].to_numpy()

print("Sales array:", sales_array)

print()

# NumPy handles simple numeric summaries.
print("Mean:", np.mean(sales_array))
print("Max:", np.max(sales_array))
print("Total:", np.sum(sales_array))

print()

# Build monthly totals, then compare the changes.
monthly_df = pd.read_sql_query("""
SELECT month, SUM(quantity * unit_price) AS total_sales
FROM sales
GROUP BY month
ORDER BY month
""", connection)

monthly_sales = monthly_df["total_sales"].to_numpy()

print("Monthly sales:", monthly_sales)
print("Monthly change:", np.diff(monthly_sales))

connection.close()

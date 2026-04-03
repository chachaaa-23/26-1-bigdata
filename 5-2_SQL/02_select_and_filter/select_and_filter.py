import sqlite3

# Use an in-memory database for quick query practice.
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

# Read only the columns we need.
print("Product and quantity:")
for row in cursor.execute("""
SELECT product_name, quantity
FROM sales
"""):
    print(row)

print()

# Filter rows and sort the result.
print("Products with price >= 50:")
for row in cursor.execute("""
SELECT product_name, unit_price
FROM sales
WHERE unit_price >= 50
ORDER BY unit_price DESC
"""):
    print(row)

connection.close()

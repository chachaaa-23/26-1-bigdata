import sqlite3

# Use an in-memory table for summary practice.
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

# Sample rows for summary practice.
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

# Basic summary functions work on the whole table.
print("Row count:", cursor.execute("SELECT COUNT(*) FROM sales").fetchone()[0])
print("Total quantity:", cursor.execute("SELECT SUM(quantity) FROM sales").fetchone()[0])
print("Average price:", cursor.execute("SELECT AVG(unit_price) FROM sales").fetchone()[0])

print()

# GROUP BY summarizes rows by category.
print("Sales by category:")
for row in cursor.execute("""
SELECT category, SUM(quantity * unit_price)
FROM sales
GROUP BY category
"""):
    print(row)

connection.close()

import sqlite3

# Use an in-memory table for INSERT, UPDATE, and DELETE practice.
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create a small sales table and starting rows.
cursor.execute("""
CREATE TABLE sales (
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price INTEGER,
    month INTEGER
)
""")

# Start with a few sample rows.
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

# Add, update, and delete data.
cursor.execute("""
INSERT INTO sales (product_name, category, quantity, unit_price, month)
VALUES ('Webcam', 'Accessory', 3, 70, 3)
""")

cursor.execute("""
UPDATE sales
SET unit_price = 50
WHERE product_name = 'Keyboard'
""")

cursor.execute("""
DELETE FROM sales
WHERE product_name = 'Monitor'
""")

connection.commit()

# Check the final table after the changes.
print("Sales table after changes:")
for row in cursor.execute("""
SELECT product_name, quantity, unit_price, month
FROM sales
ORDER BY month
"""):
    print(row)

connection.close()

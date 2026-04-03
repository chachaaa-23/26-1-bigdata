import os
import sqlite3

# Build a database file in a generated folder.
base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
db_path = os.path.join(generated_dir, "store_sales.db")

os.makedirs(generated_dir, exist_ok=True)

# Open the database and start with a fresh sales table.
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute("""
CREATE TABLE sales (
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price INTEGER,
    month INTEGER
)
""")

# Insert a few sample sales rows.
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

connection.commit()

# Check the saved file and rows.
print("Database file:")
print(db_path)

print()

print("Sales table:")
for row in cursor.execute("SELECT * FROM sales"):
    print(row)

connection.close()

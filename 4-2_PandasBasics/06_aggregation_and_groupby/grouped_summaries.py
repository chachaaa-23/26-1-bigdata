import pandas as pd

# groupby() is a key tool for analysis.
order_df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "A", "C"],
    "product": ["Mouse", "Keyboard", "Mouse", "Monitor", "Monitor", "Keyboard"],
    "sales": [50, 80, 55, 200, 180, 90],
    "quantity": [5, 4, 6, 2, 1, 3]
})

print("Orders:")
print(order_df)

print()

# groupby() gathers rows by category, then summarizes them.
print("Sales and quantity by team:")
print(order_df.groupby("team")[["sales", "quantity"]].sum())

print()

# We can choose one column and compute a different statistic.
print("Average sales by team:")
print(order_df.groupby("team")["sales"].mean())

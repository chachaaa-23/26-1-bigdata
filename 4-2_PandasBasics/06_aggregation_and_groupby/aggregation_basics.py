import pandas as pd

# Use monthly sales to practice summary functions.
sales_df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "online": [120, 135, 150, 160],
    "store": [80, 90, 85, 95]
})

print("Sales data:")
print(sales_df)

print()

# Basic aggregation works column by column.
print("Total online sales:", sales_df["online"].sum())
print("Average store sales:", sales_df["store"].mean())
print("Maximum online sales:", sales_df["online"].max())

print()

# We can also add a total column before later analysis.
sales_df["total"] = sales_df["online"] + sales_df["store"]

print("Monthly totals:")
print(sales_df[["month", "total"]])

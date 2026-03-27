import pandas as pd

# This table will be used for filtering practice.
sales_df = pd.DataFrame({
    "employee": ["Minji", "Joon", "Hana", "Taeho", "Sora"],
    "team": ["A", "B", "A", "B", "A"],
    "sales": [120, 95, 140, 110, 80]
})

print("Original DataFrame:")
print(sales_df)

print()

# A comparison creates True/False values.
print("sales['sales'] >= 100:")
print(sales_df["sales"] >= 100)

print()

# We can use that mask to keep matching rows.
print("sales[sales['sales'] >= 100]:")
print(sales_df[sales_df["sales"] >= 100])

print()

# Combine conditions with & or |.
high_sales_team_a_mask = (sales_df["sales"] >= 100) & (sales_df["team"] == "A")

print("Team A with sales >= 100:")
print(sales_df[high_sales_team_a_mask])

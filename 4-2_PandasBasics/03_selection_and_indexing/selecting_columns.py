import pandas as pd

# Build a simple score table first.
score_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "score": [88, 76, 93, 85],
    "attendance": [95, 82, 98, 90]
})

print("Original DataFrame:")
print(score_df)

print()

# Selecting one column returns a Series.
print("df['name']:")
print(score_df["name"])

print()

# Selecting a list of columns keeps a DataFrame.
print("df[['name', 'score']]:")
print(score_df[["name", "score"]])

import pandas as pd

# Missing values are common in real data.
student_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "score": [88, None, 95, 76],
    "city": ["Seoul", "Busan", None, "Incheon"]
})

print("Original DataFrame:")
print(student_df)

print()

# isna() marks missing cells as True.
print("Missing values:")
print(student_df.isna())

print()

# sum() counts how many missing values each column has.
print("Missing value count:")
print(student_df.isna().sum())

print()

# dropna() removes rows with missing values in selected columns.
print("Rows without missing scores:")
print(student_df.dropna(subset=["score"]))

print()

# fillna() replaces missing values with chosen values.
filled_df = student_df.copy()
filled_df["score"] = filled_df["score"].fillna(filled_df["score"].mean())
filled_df["city"] = filled_df["city"].fillna("Unknown")

print("After fillna():")
print(filled_df)

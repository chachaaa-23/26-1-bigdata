import pandas as pd

# A DataFrame is a 2D table with rows and columns.
student_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "age": [20, 21, 22, 20],
    "major": ["Data Science", "AI", "Economics", "Design"]
})

print("DataFrame:")
print(student_df)

print()


# shape shows row and column counts.
print("Shape:", student_df.shape)
print("Columns:", student_df.columns.tolist())

print()

# dtypes shows the data type of each column.
print("Column types:")
print(student_df.dtypes)

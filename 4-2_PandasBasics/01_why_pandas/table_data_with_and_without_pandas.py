import pandas as pd

# Start with plain Python table-like data.
student_rows = [
    {"name": "Minji", "python": 78, "sql": 85},
    {"name": "Joon", "python": 92, "sql": 88},
    {"name": "Hana", "python": 85, "sql": 94},
]

python_total = 0

# In plain Python, we loop manually to compute an average.
for student in student_rows:
    python_total += student["python"]

print("Raw data:", student_rows)
print("Manual Python average:", python_total / len(student_rows))

print()

# Pandas turns the same data into a DataFrame.
student_df = pd.DataFrame(student_rows)

print("DataFrame:")
print(student_df)

print()

# Column-based calculations are shorter and clearer.
print("Python average with Pandas:", student_df["python"].mean())
print("SQL scores above 90:")
print()
print(student_df["sql"] > 90)
print()
print(student_df[student_df["sql"] > 90])

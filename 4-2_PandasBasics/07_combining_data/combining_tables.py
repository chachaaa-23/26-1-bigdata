import pandas as pd

# Prepare two small tables with the same columns.
midterm_df = pd.DataFrame({
    "name": ["Minji", "Joon"],
    "score": [82, 91]
})

final_df = pd.DataFrame({
    "name": ["Hana", "Taeho"],
    "score": [95, 87]
})

# concat() stacks rows vertically.
combined_scores_df = pd.concat([midterm_df, final_df], ignore_index=True)

print("Concatenated DataFrame:")
print(combined_scores_df)

print()

# This second table has extra student information.
student_info_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "major": ["Data Science", "AI", "Economics", "Design"]
})

# merge() joins tables by a shared key column.
merged_df = pd.merge(combined_scores_df, student_info_df, on="name", how="left")

print("Merged DataFrame:")
print(merged_df)

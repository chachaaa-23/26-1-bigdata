import pandas as pd

# Create a score table for column operations.
score_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "midterm": [82, 75, 91, 84],
    "final": [88, 79, 94, 86],
    "attendance": [95, 78, 100, 88]
})

print("Before adding columns:")
print(score_df)

# New columns can come from existing columns.
score_df["total"] = score_df["midterm"] + score_df["final"]
score_df["passed"] = score_df["total"] >= 160 #boolean 값들을 dictionary 처럼 넣기

print("After adding columns:")
print(score_df)

print()

# loc updates only the rows we choose.
score_df.loc[score_df["attendance"] < 90, "passed"] = False

print("After attendance rule:")
print(score_df)

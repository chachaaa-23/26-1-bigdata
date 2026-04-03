import pandas as pd

# Add custom row labels to make loc examples clear.
student_df = pd.DataFrame({
    "name": ["Minji", "Joon", "Hana", "Taeho"],
    "score": [88, 76, 93, 85],
    "department": ["Data", "AI", "Data", "Design"]
}, index=["st_1", "st_2", "st_3", "st_4"])

print("Original DataFrame:")
print(student_df)

print()

# loc uses row and column labels. <-- loc = location, user defined index location으로 바꾸기
print("df.loc['st_2']:")
print(student_df.loc["st_2"]) #slicing with index (which can be string)

print()

# A label slice includes both ends.
print("df.loc['st_1':'st_3', ['name', 'score']]:")
print(student_df.loc["st_1":"st_3", ["name", "department"]])

print()

# iloc uses row and column positions.
print("df.iloc[1]:") # 이상:미만
print(student_df.iloc[1])

print()

print("df.iloc[0:2, 0:2]:")
print(student_df.iloc[0:2, 0:2])

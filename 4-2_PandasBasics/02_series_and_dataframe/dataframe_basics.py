import pandas as pd

# A DataFrame is a 2D table with rows and columns.
student_df = pd.DataFrame({ # 행값= items, 각각의 feature DataFrame 에 저장됨. row & col transposed 뒤집힘
    "name": ["Minji", "Joon", "Hana", "Taeho"],  #각각의 col 정보. col 점근하기 위해, key값("name")으로 접근 가능 
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
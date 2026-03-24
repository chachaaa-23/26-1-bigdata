import numpy as np

# Each row is one student and each column is one feature.
# Features: study hours, attendance rate, gaming hours, exam score
student_data = np.array([[1, 65, 9, 60],
                         [2, 90, 4, 68],
                         [3, 72, 8, 66],
                         [4, 88, 3, 80],
                         [5, 70, 7, 72],
                         [6, 95, 2, 88],
                         [7, 68, 8, 70],
                         [8, 85, 4, 84]], dtype=float)

feature_names = ["study_hours", "attendance_rate", "gaming_hours", "exam_score"]

print("Feature names:")
print(feature_names)

print()

print("Student data:")
print(student_data)

print()

# rowvar=False means each column is treated as one feature.
correlation_matrix = np.corrcoef(student_data, rowvar=False)

print("Correlation matrix for the 4 features:")
print(correlation_matrix)

print()

# The off-diagonal values show pairwise correlations between features.
print("study_hours vs exam_score:", correlation_matrix[0, 3])
print("attendance_rate vs exam_score:", correlation_matrix[1, 3])
print("gaming_hours vs exam_score:", correlation_matrix[2, 3])
print("study_hours vs attendance_rate:", correlation_matrix[0, 1])

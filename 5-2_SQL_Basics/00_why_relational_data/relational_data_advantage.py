import sqlite3

# Use two related tables to avoid repeating the same department info.
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE students (
    student_name TEXT,
    major TEXT
)
""")

cursor.execute("""
CREATE TABLE departments (
    major TEXT,
    building TEXT
)
""")

# The same major can appear in many student rows.
# 매핑관계 확실한 데이터끼리 묶음. 
student_rows = [ 
    ("Mina", "CS"),
    ("Jisoo", "Math"),
    ("Kevin", "CS")
]

# Department info is stored once per major.
department_rows = [
    ("CS", "Engineering Hall"),
    ("Math", "Science Hall")
]

cursor.executemany("""
INSERT INTO students (student_name, major)
VALUES (?, ?)
""", student_rows)

cursor.executemany("""
INSERT INTO departments (major, building)
VALUES (?, ?)
""", department_rows)

connection.commit()

print("Students table:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print()

print("Departments table:")
for row in cursor.execute("SELECT * FROM departments"):
    print(row)

print()

# JOIN lets us read the two tables together.
print("Joined result:")
for row in cursor.execute("""
SELECT students.student_name, students.major, departments.building
FROM students
JOIN departments
ON students.major = departments.major
"""):
    print(row)

print()

# One update can affect many joined results.
cursor.execute("""
UPDATE departments
SET building = 'AI Center'
WHERE major = 'CS'
""")

connection.commit()

print("After one department update:")
for row in cursor.execute("""
SELECT students.student_name, students.major, departments.building
FROM students
JOIN departments
ON students.major = departments.major
"""):
    print(row)

connection.close()

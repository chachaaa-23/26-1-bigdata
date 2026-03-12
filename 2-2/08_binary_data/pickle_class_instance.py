import os
import pickle


# This class has three properties and two custom methods.
class Student:
    def __init__(self, name, major, year):
        self.name = name
        self.major = major
        self.year = year

    def introduce(self):
        return f"{self.name} studies {self.major}."

    def is_senior(self):
        return self.year >= 4


base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
file_path = os.path.join(generated_dir, "student.pkl")

os.makedirs(generated_dir, exist_ok=True)

student = Student("Mina", "Big Data", 4)

# Save the object as binary data.
with open(file_path, "wb") as f:
    pickle.dump(student, f)

# Load the object again and check its values.
with open(file_path, "rb") as f:
    loaded_student = pickle.load(f)

print(loaded_student.name)
print(loaded_student.major)
print(loaded_student.year)
print(loaded_student.introduce())
print(loaded_student.is_senior())

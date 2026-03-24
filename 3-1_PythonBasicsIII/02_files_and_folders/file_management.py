import os

# Make simple paths for one folder and one file.
base_dir = os.path.dirname(__file__)
work_dir = os.path.join(base_dir, "_generated")
folder_path = os.path.join(work_dir, "example_folder")
file_path = os.path.join(work_dir, "note.txt")

# Make a working folder for this example.
os.makedirs(work_dir, exist_ok=True)

# Check the folder before making it.
print(os.path.exists(folder_path))

# Make one folder.
try:
    os.mkdir(folder_path)
except:
    pass

# Check the folder after making it.
print(os.path.exists(folder_path))
print(os.path.isdir(folder_path))

print()

# Make one text file.
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello")

# Check whether the file exists.
print(os.path.isfile(file_path))

print()

# Remove the file and folder.
os.remove(file_path)
os.rmdir(folder_path)

print(os.path.exists(folder_path))
print(os.path.isfile(file_path))

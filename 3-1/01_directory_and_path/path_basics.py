import os

# Get the folder that contains this Python file.
dir_path = os.path.dirname(__file__)
file_name = "sample.txt"

# Join a folder and a file name.
path_test = os.path.join(dir_path, file_name)

# Move to the parent folder.
dir_parent = os.path.abspath(os.path.join(dir_path, ".."))

print(dir_path)
print(path_test)
print(dir_parent)

print()

# basename() gets only the file name.
print(os.path.basename(path_test))

# splitext() separates the name and extension.
print(os.path.splitext(file_name))

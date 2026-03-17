import os

# Build a text file path in this folder.
base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
file_path = os.path.join(generated_dir, "test.txt")

os.makedirs(generated_dir, exist_ok=True)

# Write new text data.
text_data = "Test"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text_data)

# Add more text to the same file.
additional_text_data = "\nadd_test"

with open(file_path, "a", encoding="utf-8") as f:
    f.write(additional_text_data)

# Read the whole file at once.
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print(content)

print()

# Read the file line by line.
content_lines = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        content_lines.append(line.strip())

print(content_lines)

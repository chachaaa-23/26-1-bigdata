import os
import pickle

# Save a simple list as binary data.
data = [1, 2, 3]
base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
file_path = os.path.join(generated_dir, "numbers.pkl")

os.makedirs(generated_dir, exist_ok=True)

with open(file_path, "wb") as f: # binary 숫자로 저장- write binary
    pickle.dump(data, f)

# Load the saved data back into Python.
with open(file_path, "rb") as f:
    data_loaded = pickle.load(f)

print(data_loaded)
print(type(data_loaded))

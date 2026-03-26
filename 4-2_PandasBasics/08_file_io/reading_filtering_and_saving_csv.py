import os

import pandas as pd

# Build file paths in this folder.
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "sample_scores.csv")
generated_dir = os.path.join(base_dir, "_generated")
output_path = os.path.join(generated_dir, "passed_students.csv")

os.makedirs(generated_dir, exist_ok=True)

# read_csv() loads a CSV file into a DataFrame.
score_df = pd.read_csv(file_path)

print("CSV data:")
print(score_df)

print()

# Once loaded, we can analyze it like any other DataFrame.
print("Average score:", score_df["score"].mean())

print()

# Filter rows, then save the result to a new CSV file.
passed_df = score_df[score_df["score"] >= 85]
passed_df.to_csv(output_path, index=False)

print("Passed students:")
print(passed_df)

print()

print("Saved file:", output_path)

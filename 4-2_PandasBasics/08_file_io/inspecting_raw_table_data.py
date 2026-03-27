import os

import pandas as pd

# Read the raw sales file used across this lesson.
base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "sample_data", "retail_sales_raw.csv"))

raw_df = pd.read_csv(file_path)

print("Raw data:")
print(raw_df)

print()

# Start by checking the size of the table.
print("Shape:", raw_df.shape)

# Column names are the first clue about structure.
print("Columns:", raw_df.columns.tolist())

print()

# Data types tell us what needs cleaning.
print("Column types:")
print(raw_df.dtypes)

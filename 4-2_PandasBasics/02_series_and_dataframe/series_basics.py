import pandas as pd

# A Series stores one labeled column of data.
temperature_series = pd.Series([21, 23, 20, 24],
                               index=["Mon", "Tue", "Wed", "Thu"],
                               name="temperature")

print("Series:")
print(temperature_series)

print()

# We can read one label, compute a mean, and inspect labels.
print("temperature_series['Tue']:", temperature_series["Tue"])
print("Mean:", temperature_series.mean())
print("Index labels:", temperature_series.index.tolist())

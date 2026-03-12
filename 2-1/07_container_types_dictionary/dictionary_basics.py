# Make a simple dictionary.
a = {"Pikachu": "yellow", "Charmander": "red", "Squirtle": "blue"}
b = "Pikachu"

# Read a value with a key.
print(a[b])

# Add a new key and value.
a["Eevee"] = "brown"
print(a["Eevee"])
print(a)

# Delete one key.
del a["Pikachu"]
print(a)
print(len(a))

print()

# keys() and items() are useful.
print(a.keys())
print(a.items())
print(list(a.keys()))
print(list(a.items()))

print()

# get() is useful when a key might not exist.
print(a.get("Mew"))

# A Python dictionary (dict) is a hashmap —
# a collection of key-value pairs where each key is unique
# and hashable, allowing fast O(1) average-time lookup, insertion,
# and deletion.

# Creating a dictionary of chai types
chai_type = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Print full dictionary
print("Full dictionary:", chai_type)

# Access values by key
print("Masala chai:", chai_type["Masala"])

# Safe access using get()
print("Ginger chai:", chai_type.get("Ginger"))
print("Gingery chai:", chai_type.get("Gingery"))          # None
print("Masalaa chai (with default):", chai_type.get("Masalaa", "Not Found"))

# Loop through keys
for key in chai_type:
    print(key)

# Loop through keys and values
for key in chai_type:
    print(key, chai_type[key])

# Loop using items()
for key, value in chai_type.items():
    print(key, value)

# Check if key exists
if "Masala" in chai_type:
    print("I have Masala")

# Adding a new key-value pair
chai_type["Earl Grey"] = "Citrus"
print(chai_type)

# Removing a key
chai_type.pop("Ginger")
print(chai_type)

# Remove last inserted item
chai_type.popitem()
print(chai_type)

# Nested dictionary (fixed syntax)
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Mild", "Black": "Strong"}
}
print(tea_shop)

# How to access the value in the nested object
print(tea_shop["chai"]["Ginger"])  # Output: Zesty

# Dictionary comprehension — creating a dictionary of squares
squared_num = {x: x**2 for x in range(6)}
print(squared_num)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using dict.fromkeys() — create a dictionary with default values
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

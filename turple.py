# A tuple in Python is an immutable ordered collection of items — similar to a list, 
# but cannot be changed (no adding, removing, or modifying elements once created).
# It’s often used for fixed data or as dictionary keys.

# [] -> list , {} -> dictionary , () -> tuple
tea_types = ("Black", "Green", "Oolong")
print("Original Tuple:", tea_types)

#  Tuples are immutable — this line would cause an error
# tea_types[0] = "green"  #  TypeError: 'tuple' object does not support item assignment

# ✅ Correct way — create a new tuple instead
new_tea_types = ("Green",) + tea_types[1:]
print("Modified Tuple (new):", new_tea_types)

# Add more tuples (concatenation)
more_tea = ("Herbal", "Earl Grey")
all_tea = tea_types + more_tea
print("All tea types:", all_tea)



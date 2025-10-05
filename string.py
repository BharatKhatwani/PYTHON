# Length of string
print(len(chai))  # Prints number of characters in 'chai'

# Iterating through each character
for letter in chai:
    print(letter)

# Using escape sequences to include quotes inside a string
chai = "He Said , \"Masala chai is awesome \" "
print(chai)  # Output: He Said , "Masala chai is awesome "

# Raw string: escape sequences are not processed
chai = r"Masala\nchai"
print(chai)  # Output literally: Masala\nchai


chai = 'Lemon Chai'
print(chai)  # Prints the full string: Lemon Chai

# Accessing the first character
first_char = chai[0]
print(first_char)  # L

# Slicing
slice_chai = chai[0:6]
print(slice_chai)  # Lemon

# String of numbers
num_list = "0123456789"
print(num_list[3:])    # 3456789
print(num_list[:2])    # 01
print(num_list[0:7:3]) # 036

# Removing spaces
chai = "      masala chai   "
print(chai.strip())  # masala chai

# Replace substring after strip
print(chai.strip().replace("masala", "Ginger"))  # Ginger chai

# Splitting strings
chai = "Lemon , Ginger, Masala"
print(chai.split())      # ['Lemon', ',', 'Ginger,', 'Masala']
print(chai.split(", "))  # ['Lemon', 'Ginger', 'Masala']

# Find substring
chai = "Masala chai"
print(chai.find("chai"))  # 7

# Count occurrences
print(chai.count("a"))  # 4

# String formatting
chai_type_str = "Masala"
quality = 2
order = "I ordered {} cups of {} chai"
print(order.format(quality, chai_type_str))  # I ordered 2 cups of Masala chai

# Iterating over string
for letter in chai:
    print(letter)

# Escaping quotes
chai = "He said, \"Masala chai is awesome\""
print(chai)

# Raw string
chai = r"Masala\nchai"
print(chai)  # Prints: Masala\nchai
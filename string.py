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

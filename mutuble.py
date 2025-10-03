username = "Bharat"  # username points to "Bharat"
print(username)      # prints: Bharat

username = "Hitesh"  # username now points to "Hitesh", "Bharat" is unreferenced
print(username)      # prints: Hitesh



# Same thing happen here 
x = 10
y = x 
print(x)
print(y)

x = 15 
print(x)
print(y)
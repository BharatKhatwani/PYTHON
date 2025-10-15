# x = "global"

# def outer():
#     x = "enclosing"
    
#     def inner():
#         x = "local"
#         print("Inner:", x)
    
#     inner()
#     print("Outer:", x)

# outer()
# print("Global:", x)



def outer_function(msg):
    def inner_function():
        print("Message:", msg)
    return inner_function  # returning inner function

# create closure
greet = outer_function("Hello Bharat!")

greet()  # calling inner function

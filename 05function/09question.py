
# def print_kwargs(name , power):
#     print("Name", name , "Power", power)
# print_kwargs(name = "shaktiman", power ="lazer")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name = "shaktiman", power = "lazer")
print_kwargs(name= "shaktiman")
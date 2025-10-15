def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        
        print(f"Calling {func.__name__} with:")
        if args_value:
            print(f"  Positional args → {args_value}")
        if kwargs_value:
            print(f"  Keyword args → {kwargs_value}")
        
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully!\n")
        return result
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="Hanji")

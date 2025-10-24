import math

def calculator():
    print("\n--- Python CLI Calculator ---")
    
    try:
        a = float(input("Enter the first number: "))
        b = None  # b might not be needed for some operations
        operator = input("Enter the operator (+, -, *, /, ^, sqrt): ").strip()
        
        if operator != "sqrt":
            b = float(input("Enter the second number: "))

        if operator == '+':
            print("Result:", a + b)
        elif operator == '-':
            print("Result:", a - b)
        elif operator == '*':
            print("Result:", a * b)
        elif operator == '/':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero")
        elif operator == '^':
            print("Result:", a ** b)
        elif operator == 'sqrt':
            if a >= 0:
                print("Result:", math.sqrt(a))
            else:
                print("Error: Cannot take square root of negative number")
        else:
            print("Invalid operator")
            
    except ValueError:
        print("Error: Please enter valid numbers.")

# Loop for multiple calculations
while True:
    calculator()
    cont = input("\nDo you want to calculate again? (y/n): ").lower()
    if cont != 'y':
        print("Exiting calculator. Goodbye!")
        break

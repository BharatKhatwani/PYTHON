import random
import math

# Generate a random number between 1 and 100
element = math.floor(random.random() * 100) + 1

print("🎯 Guess the number between 1 and 100!")

while True:
    try:
        number = int(input("Enter your guess: "))

        if number > 100 or number < 1:
            print("⚠️ Enter a valid number between 1 and 100!")
        elif number == element:
            print("🎉 Congrats! You guessed the correct number.")
            break
        elif number > element:
            print("📉 Try a lower number.")
        else:
            print("📈 Try a higher number.")

    except ValueError:
        print("❌ Please enter a valid integer!")

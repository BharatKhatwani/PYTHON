import random

subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Elon Musk",
    "Taylor Swift",
    "Narendra Modi",
    "Cristiano Ronaldo",
    "Iron Man",
    "Spider-Man",
    "Bill Gates",
    "Messi",
    "Sundar Pichai",
    "APJ Abdul Kalam",
    "Dr. Strange",
    "Captain America",
    "The Rock",
    "Tom Cruise",
    "Selena Gomez",
    "Ranbir Kapoor",
    "Alia Bhatt",
    "MS Dhoni",
    "Steve Jobs",
    "Mark Zuckerberg",
    "Harry Potter",
    "Batman",
    "Thanos"
]

actions = [
    "launches a new company",
    "cancels a concert",
    "dances with a robot",
    "eats 20 pizzas",
    "builds a rocket in his backyard",
    "buys Twitter again",
    "teaches Python to kids",
    "starts a cricket team",
    "visits Mars for a selfie",
    "makes a viral meme",
    "writes a new book",
    "learns to cook Maggi",
    "runs a marathon barefoot",
    "opens a gym in space",
    "creates an AI assistant",
    "plays chess with aliens",
    "starts a YouTube channel",
    "becomes a stand-up comedian",
    "wins a cooking competition",
    "creates a new social media app",
    "hosts a reality show",
    "sings at a wedding",
    "joins the army",
    "buys a zoo",
    "starts teaching coding"
]

places_or_things = [
    "at the Red Fort",
    "in Mumbai local trains",
    "during IPL matches",
    "at the Taj Mahal",
    "inside a spaceship",
    "at Gateway of India",
    "in the metaverse",
    "inside a classroom",
    "on top of Mount Everest",
    "at Marine Drive",
    "inside a video game",
    "in a secret lab",
    "on a live TV show",
    "at a tech conference",
    "in a parallel universe"
]

# Fake News Headline Generator
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}!"
    print("\n", headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake Headline Generator. Have a fun day! 😄")

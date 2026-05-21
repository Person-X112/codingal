# Ask username
print("Hello! I am AI Bot. What's your name? : ")

# Input name
username = input()

# Greet with username
print(f"Nice to meet you, {username}!")

# Take input
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

# Use conditional statements to answer with input
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {username}. Goodbye!")
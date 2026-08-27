first_name = "Steinar"
favorite_language = input("What is your favorite language:")

if favorite_language.lower() == "italian":
    greeting = "Buiongiorno"
elif favorite_language.lower() == "english":
    greeting = "Welcome"
elif favorite_language.lower() == "spanish":
    greeting = "Buoenos dias"
elif favorite_language.lower() == "german":
    greeting = "Guten tag"
else:
    greeting = "Perhaps you can teach me some ?"

print(f"Hi {first_name}, welcome to GA")
print(f"I hear your favourite language is {favorite_language}")
print(greeting)
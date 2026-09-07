# Guess a number or binary search

correct_guessed: bool = False
lower_limit: int = 1
upper_limit: int = 30
counter: int = 0

while not correct_guessed and counter < 5:
    middle_of_limits: int = ((lower_limit + upper_limit) // 2)
    print(f"Jeg gjetter på {middle_of_limits}")
    print("Var det korrekt ?")
    user_input: str = input('''
    Tast (k) for korrekt
    Tast (h) for høyere
    Tast (l) for lavere
    Tast (a) for å avslutte
    Ditt svar: ''')

    if user_input.lower() == "a":
        print("Program avsluttes")
        break
    elif user_input.lower() == "k":
        correct_guessed = True
    elif user_input.lower() == "l":
        upper_limit = middle_of_limits - 1
    elif user_input.lower() == "h":
        lower_limit = middle_of_limits + 1
    else:
        print("Du tastet et ugyldig valg")
        continue

    counter += 1
    if correct_guessed:
        print(f"Programmet gjettet rett på {counter} forsøk")
    elif counter == 5:
        print("Ingen flere forsøk")
        break



# with n guesses you can distinguish at most
# 2ⁿ − 1 numbers.
# 2⁴ − 1 = 15, which is less than 30.
# 2⁵ − 1 = 31, which is enough
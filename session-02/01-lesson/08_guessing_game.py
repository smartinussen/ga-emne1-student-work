# Guessing game
secret_number = 88
attempts_left = 5

while attempts_left > 0:
    guess = int(input("Tast inn et tall:"))
    attempts_left -= 1
    if guess == secret_number:
        print("Korrekt!")
        attempts_left = -1
    elif guess > secret_number:
        print(f"Det var for høyt. Prøv igjen. {attempts_left} forsøk igjen")
    else:
        print(f"Det var for lavt. Prøv igjen. {attempts_left} forsøk igjen")

print("Programmet er ferdig!")
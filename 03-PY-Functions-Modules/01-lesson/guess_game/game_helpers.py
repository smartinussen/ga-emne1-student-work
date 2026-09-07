def read_guess():
    guess = input("Guess a number 1-30: ")
    return int(guess)

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"

def show_feedback(result: str) -> None:
    if result == "correct":
        print("You guessed correctly")
    elif result == "high":
        print("Your guess was too high")
    elif result == "low":
        print("Your guess was too low")
    else:
        print(f"Something wrong happened. '{result}' is unknown")
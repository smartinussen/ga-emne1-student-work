# The great guessing game

import random
from game_helpers import read_guess, check_guess, show_feedback


def main() -> None:
    secret_number: int = random.randint(1,30)
    result = ""

    while result != "correct":
        guess = read_guess()
        result = check_guess(guess, secret_number)
        show_feedback(result)

if __name__ == "__main__":
    main()
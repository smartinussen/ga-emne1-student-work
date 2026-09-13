# Tall analyse

def read_number() -> int:
    """Ask until the user gives a valid whole number."""
    while True:
        user_input: str = input("Tast inn et heltall: ")
        try:
            return int(user_input)
        except ValueError:
            print("Feil input: Kun heltall kan benyttes. Prøv igjen")


def describe_sign(number: int) -> str:
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def is_even(number: int) -> bool:
    return number % 2 == 0


def show_analysis(number: int, sign: str, even: bool) -> None:
    print(f"Your chosen number is {number}")
    print(f"The number is {sign}")
    if even:
        print("The number is even")
    else:
        print("The number is odd")


def run_number_analyzer() -> None:
    input_number = read_number()
    input_number_sign = describe_sign(input_number)
    even = is_even(input_number)
    show_analysis(input_number, input_number_sign, even)


if __name__ == "__main__":
    show_analysis(56, describe_sign(56), is_even(56))
    show_analysis(-27, describe_sign(-27), is_even(-27))
    show_analysis(0, describe_sign(0), is_even(0))

    run_number_analyzer()

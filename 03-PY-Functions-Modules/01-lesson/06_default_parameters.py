# Functions with default parameters

def show_welcome(name: str = "GA elev"):
    print(f"Velkommen på kurs {name}")


def greet(name, greeting: str = "Hello"):
    print(f"{greeting} {name}!")

greet("Erna")
greet("Jonas", greeting = "Good Morning")


# Welcome to the course

def show_welcome(name: str = "GA elev"):
    print(f"Velkommen på kurs {name}")

def show_total(price: float, quantity: int):
    total = price * quantity
    print(f"Total: {total:.2f} kr")

show_welcome("Steinar")
show_welcome()
show_total(12.5, 5)


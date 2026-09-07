# Return values from functions


def get_total(price: float, quantity: int):
    total: float = price * quantity
    return total


order_total: float = get_total(10, 5)
print(f"Totalen er: {get_total(10, 5)} kr")

print(order_total)

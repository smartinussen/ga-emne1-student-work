# Valgfri valuta

def show_price(price: float, currency: str = "NOK"):
    print(f"The price is {price} in {currency}")

show_price(5, "EUR")
show_price(8)
show_price(10.5)
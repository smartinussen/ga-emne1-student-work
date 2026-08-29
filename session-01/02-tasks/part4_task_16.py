# Pris med rabatt
unit_price = float(input("Skriv inn enhetspris: "))
discount_factor = int(input("Skriv inn rabatt prosent: "))
discount = (unit_price * discount_factor) / 100
new_price = unit_price - discount

print(f"Din rabatt er {discount:.2f} kr")
print(f"Produkt pris er {new_price:.2f} kr")

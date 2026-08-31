purchase_value = float(input("Beløp: "))

if purchase_value >= 1000:
    purchase_value *= 0.8
    print(f"Ny pris {purchase_value}")
elif purchase_value >= 500:
    purchase_value *= 0.9
    print(f"Ny pris er: {purchase_value}")
else:
    print(purchase_value)
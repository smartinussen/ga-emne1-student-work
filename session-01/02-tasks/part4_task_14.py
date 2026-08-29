# Enkel valutaomregning

value = float(input("Skriv inn beløp: "))
rate = float(input("Skriv in kurs: "))
new_currency = value * rate


print(f"Du får {new_currency:.2f} enheter i ny valuta for {value} ved {rate} kurs")

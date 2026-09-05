# Be om et gyldig tall

while True:
    number_input = input("Tast inn et postivt heltall: ")
    if not number_input.isdigit() or int(number_input) <= 0:
        print("Feil input.Vennligst tast inn et positivt heltall")
    else:
        print(f"Bra. Du tastet inn: {number_input}")
        break
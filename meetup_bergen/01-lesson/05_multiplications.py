# Multiplikator test

while True:
    print("Tast inn 0 for å avslutte")
    factor_1: str = input("Tast inn faktor 1: ")
    if factor_1 == "0":
        break
    elif not factor_1.isdigit():
        print("Skriv inn et gyldig tall. Prøv igjen")
        continue
        
    factor_2: str = input("Tast inn faktor 2: ")
    if factor_2 == "0":
        break
    elif not factor_2.isdigit():
        print("Skriv inn et gyldig tall. Prøv igjen")
        continue

    if factor_1.isdigit() and factor_2.isdigit():
        factor_1 = int(factor_1)
        factor_2 = int(factor_2)
        print(f"{factor_1} * {factor_2} = {factor_1 * factor_2}")

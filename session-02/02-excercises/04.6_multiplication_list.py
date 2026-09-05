# Gangetabell

print("Dette programmet lese ut gangetabellen 1-10 for et valgt heltall")

while True:
    factor = input("Tast inn et heltall: ")
    if not factor.isdigit():
        print("Feil input. Du må taste inn et tall")
    else:
        for i in range(1,11):
            print(f"{factor} x {i} = {int(factor) * i}")  #Caster i f-string for å redusere linjer
        break

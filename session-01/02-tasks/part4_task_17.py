# Sekunder til timer, minutter og sekunder
seconds = abs(int(input("Skriv inn sekunder: ")))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print(f"{hours} timer, {minutes} minutter og {seconds} sekunder")

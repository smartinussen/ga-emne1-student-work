# Sekunder til timer, minutter og sekunder
seconds = abs(int(input("Skriv inn sekunder: ")))
total_hours = seconds // 3600
total_minutes = (seconds % 3600) // 60
total_seconds = (seconds % 3600) % 60

print(f"{total_hours} timer, {total_minutes} minutter og {total_seconds} sekunder")

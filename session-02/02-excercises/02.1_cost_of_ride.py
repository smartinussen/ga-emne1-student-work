# Calculate cost of ride

fuel_usage_100km = 6
price_fuel = 28
trip_distance = int(input('Skriv inn kjørelengde i km: '))
total_fuel = (trip_distance * fuel_usage_100km) / 100
total_price = total_fuel * price_fuel

print(f'Du bruker {total_fuel}L drivstoff '
      f'\nog har en kostnad på {total_price:.2f} kr '
      f'\nfor en tur på {trip_distance} km')

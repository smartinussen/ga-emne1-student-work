number_of_tickets = int(input("How many tickets? "))
ticket_price = 180
service_fee = 35

subtotal = number_of_tickets * ticket_price
total_price = subtotal + service_fee
price_pr_person = total_price / number_of_tickets

print(f"Total pris: {total_price:.2f} kr, som er {price_pr_person:.2f} kr pr. person")


# Summer tall

temp_sum = 0

for i in range(1,11):
    print(f"Subtotal: {temp_sum}")
    print(f"Vi legger til tall {i}")
    temp_sum += i
    if i < 10:
        print(f"Ny subtotal: {temp_sum}")
        print("----------------------")
    else:
        print(f"Endelig sum: {temp_sum}")
        print("======================")

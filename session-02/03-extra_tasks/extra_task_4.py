# Prime numbers
print("This program checks if input is a prime number")

while True:
    is_prime: bool = True
    user_input: str = input("Enter a positive integer (q to quit): ")
    if user_input.lower() == "q":
        print("Program has ended")
        break
    elif not user_input.isdigit():
        print("Invalid input. Try again")
        continue

    intput = int(user_input)  # intput is NOT a typo, it's a pun

    if intput <= 1:
        is_prime = False
    else:
        for i in range(2, int(intput**0.5) + 1):
            if (intput % i) == 0:
                is_prime = False
                break
    if is_prime:
        print(f"{intput} is a prime number")
    else:
        print(f"{intput} is not a prime number")

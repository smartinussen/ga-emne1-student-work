# Prime numbers

is_prime = True

while True:
    user_input = (input('Enter an integer (q to quit): '))

    if user_input == 'q':
        break

    user_input = int(user_input)

    if user_input <= 1:
        print(f'{user_input} is not a prime number')

    elif user_input > 1:
            for i in range(2, int(user_input ** 0.5) + 1):
                if (user_input % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f'{user_input} is a prime number')
            else:
                print(f'{user_input} is not a prime number')

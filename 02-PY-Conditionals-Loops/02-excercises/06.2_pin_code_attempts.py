# Pin kode med x antall forsøk

secret_pin: str = "2468"  # Changed to string, as a pin of 0007 is different to 7
attempts_left: int = 3
is_authenticated: bool = False

while attempts_left > 0 and not is_authenticated:
    pinput: str = input("Vennligst tast inn PIN kode: ")
    if not pinput.isdigit():
        print("PIN must contain only digits")

    if pinput == secret_pin:
        is_authenticated = True
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Wrong PIN. You have {attempts_left} attempts left")

if is_authenticated:
    print("Access granted")
else:
    print("Access denied")

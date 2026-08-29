# Convert temperatures between C and F
# Second variant
while True:
    print("Option 1 to convert from C to F, Option 2 to convert from F to C")
    user_input = input("Please enter 1 or 2: ").strip()
    if user_input in ["1", "2"]:
        break
    print("Error: Input must be 1 or 2.")

if user_input == "1":
    celsius = float(input("Please enter degrees in C: "))
    print(f"{celsius} degrees Celsius is {celsius * 9 / 5 + 32:.2f} degrees Fahrenheit")

if user_input == "2":
    fahrenheit = float(input("Please enter degrees in F: "))
    print(
        f"{fahrenheit} degrees Fahrenheit is {(fahrenheit - 32) * 5 / 9:.2f} degrees Celsius"
    )

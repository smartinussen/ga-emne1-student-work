#%% Loops
# Print odd numbers between 1-20
for i in range(1, 20, 2):
    print(i, end=',')

#%% Print string
name: str = "Steinar"
for c in name:
    print(c, end='.')

#%% Pattern printing

pattern_symbol: str = "*"

for star in range(10):
    print(pattern_symbol)
    pattern_symbol += "*"

#%% Pattern printing 2

pattern_char = "*"

for i in range(1,11):  # Kontrollerer linjer
    for length in range(11 - i): #
        print(pattern_char, end="")
    print()  # Tvinger ny linje

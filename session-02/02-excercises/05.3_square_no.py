# Kvadrat tall

upper_limit = int(input("Tast inn et tall: "))

for i in range(1, upper_limit+1):
    sum_round = i * i
    if sum_round < upper_limit:
        print(f"Kvadratet av {sum_round} er mindre enn {upper_limit}")
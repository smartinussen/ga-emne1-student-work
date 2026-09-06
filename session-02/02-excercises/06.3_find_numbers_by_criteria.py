# Finn tall som oppfyller flere kriterier
counter: int = 0

for i in range(1,101):
    if i % 3 == 0 and 20 < i < 80:
        print(f"Tallet {i} passer kriteriene")
        counter += 1

print(f"Total antall tall funnet er: {counter}")
# Tell oppover

print("Serie 1:")
for serie1 in range(10):
    print(serie1, end=" ")
print('\n')
print("Serie 2:")
for serie2 in range(16):  # Alternativ løsning da jeg misforstod hintet
    if serie2 < 5:
        continue
    print(serie2, end=" ")
print('\n')
for serie3 in range(20):  # Test av alternativ løsning uten stopp verdi
    print(f"{serie3+1}", end=" ")
# Potens og partall
input_number = int(input('Tast inn et heltall: '))

print(f'{input_number}² er {input_number**2}')
print(f'{input_number}³ er {input_number**3}')
if input_number % 2 == 0:
    print('Ditt tall er et partall')
else:
    print('Ditt tall er et oddetall')

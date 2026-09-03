# Regning med to tall

input_number_1 = int(input('Tast inn første heltall: '))
input_number_2 = int(input('Tast inn andre heltall: '))

print('Addisjon:')
print(f'{input_number_1} + {input_number_2} = {input_number_1 + input_number_2}')
print()
print('Subtraksjon:')
print(f'{input_number_1} - {input_number_2} = {input_number_1 - input_number_2}')
print()
print('Multiplikasjon:')
print(f'{input_number_1} * {input_number_2} = {input_number_1 * input_number_2}')
print()

if input_number_1 > 0 and input_number_2 > 0:
    print('Divisjon:')
    print(f'{input_number_1} / {input_number_2} = {input_number_1 / input_number_2}')
    print()
    print('Heltalls divisjon:')
    print(f'{input_number_1} // {input_number_2} = {input_number_1 // input_number_2}')
    print()
    print('Rest etter divisjon:')
    print(f'{input_number_1} % {input_number_2} = {input_number_1 % input_number_2}')
    print()
else:
    print('Divisjon med 0 ikke mulig')

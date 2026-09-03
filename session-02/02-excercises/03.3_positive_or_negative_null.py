# Positivt, negativt eller null

intput = int(input('Tast inn et heltall:'))

if intput == 0:
    print('Du har tastet inn tallet null')
elif intput > 0:
    print('Du har tastet inn et positivt tall')
else:
    print('Du har tastet inn et negativt tall')

if intput != 0:
    if intput % 2 == 0:
        print('Ditt tall er et partall')
    else:
        print('Ditt tall er et oddetall')

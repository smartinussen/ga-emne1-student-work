# Beregn fraktkostnad

print('''\033[40;38;5;196m                                                                                     \033[0m
########                      ##                  ##   ###    :##:    ##        ##   ###
########                      ##          ##      ##   ##      ##     ##        ##   ## 
##                            ##          ##      ## :##:     ####    ##        ## :##: 
##         ##.####   :####    ##   ##:  #######   ##.##:      ####    ##        ##.##:  
##         #######   ######   ##  ##:   #######   #####      :#  #:   ##        #####   
#######    ###.      #:  :##  ##:##:      ##      #####       #::#    ##        #####   
#######    ##         :#####  ####        ##      #####:     ##  ##   ##        #####:  
##         ##       .#######  #####       ##      ##::##     ######   ##        ##::##  
##         ##       ## .  ##  ##.###      ##      ##  ##    .######.  ##        ##  ##  
##         ##       ##:  ###  ##  ##:     ##.     ##  :##   :##  ##:  ##        ##  :## 
##         ##       ########  ##  :##     #####   ##   ##   ###  ###  ########  ##   ## 
##         ##         ###.##  ##   ###    .####   ##   :##  ##:  :##  ########  ##   :##
''')

weight_input = float(input('Registrer pakkevekt: '))
price_tier3 = 199
price_tier2 = 129
price_tier1 = 79

if weight_input > 10:  # Check for over limit
    print('Pakken kan ikke registreres med FraktKalk')
elif weight_input > 5:  # Check for price tier 3
    print(f'Pris for forsendelsen er {price_tier3}')
elif weight_input > 2:  # Check for price tier 2
    print(f'Pris for forsendelsen er {price_tier2}')
else:
    print(f'Pris for forsendelsen er {price_tier1}')

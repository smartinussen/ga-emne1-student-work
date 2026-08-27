# Tips og totalpris
print('''
                                                                                   
888888888888  88                          88      a8P               88  88         
     88       ""                          88    ,88'                88  88         
     88                                   88  ,88"                  88  88         
     88       88  8b,dPPYba,   ,adPPYba,  88,d88'       ,adPPYYba,  88  88   ,d8   
     88       88  88P'    "8a  I8[    ""  8888"88,      ""     `Y8  88  88 ,a8"    
     88       88  88       d8   `"Y8ba,   88P   Y8b     ,adPPPPP88  88  8888[      
     88       88  88b,   ,a8"  aa    ]8I  88     "88,   88,    ,88  88  88`"Yba,   
     88       88  88`YbbdP"'   `"YbbdP"'  88       Y8b  `"8bbdP"Y8  88  88   `Y8a  
                  88                                                               
                  88                                                                                                                                                                                                                                                                   
''')
innpris = float(input("Tast inn regningens sum: "))
tips_15 = round((innpris * 1.15) - innpris, 2)

print(f"Regning sub-total: {innpris:.2f} kr")
print(f"15% tips: {tips_15:.2f} kr")
print(f"Ny total: {innpris + tips_15:.2f} kr")

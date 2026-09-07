# Minutter til timer og minutter
inn_minutter = int(input("Hvor mange minutter?: "))
hele_timer = inn_minutter // 60
rest_minutter = inn_minutter % 60
if rest_minutter != 0:
    print(f"{inn_minutter} minutter er {hele_timer} timer og {rest_minutter} minutter")
else:
    print(f"{inn_minutter} minutter er {hele_timer} timer")

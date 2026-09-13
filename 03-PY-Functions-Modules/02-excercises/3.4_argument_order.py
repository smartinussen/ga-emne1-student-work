# Rekkefølge på argumenter

def show_profile(name: str, age: int, city: str):
    print(f"Dette er {name}, som holder til i {city} og er {age} år")


show_profile(47, "Steinar", "Laksevåg")
show_profile("Steinar", 49, "Bergen")

# Ved å kalle feil rekkefølge blir også verdiene printet feil plass.
# Ty og Pycharm melder også feil type i forhold til forventet
# som f.eks str istedetfor int
# Regne ut rektangler


def calculate_area(width: float, height: float):
    return width * height


room1: float = calculate_area(3, 4)
print(f"Rom 1: {room1} m2")
room2: float = calculate_area(2, 2)
print(f"Rom 2: {room2} m2")
room3: float = calculate_area(2.5, 4.5)
print(f"Rom 3: {room3} m2")
house: float = room1 + room2 + room3

print(f"Hus areal er {house} m2")

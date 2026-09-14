persons: list = ["Steinar", "Vivian", "Ruben", "Oda"]

print(persons[0])
print(persons[2])
print(persons[-1])
print(persons[-2])
# print(persons[-11])
# print(persons[9])

persons[3] = "Monika"
print(persons)

persons.append("Gonzo")
persons.append("Gonzo")
persons.append("Gonzo")

print(persons)

persons.remove("Gonzo")
print(persons)
print(f"We have {len(persons)} guests")

persons.insert(2, "Etter Vivian")
print(persons)
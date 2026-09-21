# Value errors
# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("Computer says 'noooooo'")
# else:
#     print(f"Age next year {age + 1}")
#
# print("Sist")
inputok = False

while not inputok:
    try:
        global age
        age = int(input("Age: "))
    except ValueError:
        print("Kun integer")
    else:
        inputok = True

print(age + 1)


# Fibonacci

limit = int(input("Show the fibonacci numbers up to: "))
last = 0
lastest = 1
next = 0

print(last)
print(lastest)


while next <= limit:
    next = last + lastest
    print(next)
    last = lastest
    lastest = next

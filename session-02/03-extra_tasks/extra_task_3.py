# Fibonacci

limit = int(input("Show the fibonacci numbers up to: "))
last = 0
prev_number = 1
next_number = 0

if limit >= 0:
    print(last)
if limit >= 1:
    print(prev_number)

# Iteration 1:
# while True:
#     next_number = last + prev_number
#     if next_number > limit:
#         break
#     print(next_number)
#     last = prev_number
#     prev_number = next_number

# Iteration 2
while next_number <= limit:
    print(next_number)
    last = prev_number
    prev_number = next_number
    next_number = last + prev_number
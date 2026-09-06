# Fibonacci

limit = int(input("Show the fibonacci numbers up to: "))
last: int = 0
prev_number: int = 1
next_number: int = 1

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

# Simplest iteration (assisted, concepts not learnt yet)
# limit = int(input("Show the fibonacci numbers up to: "))
# current = 0
# following = 1
#
# while current <= limit:
#     print(current)
#     current, following = following, current + following

n = int(input("plz enter n "))

first = 0
second = 1

for i in range(n):
    print(first , " ")
    next_number = first + second
    first = second
    second = next_number

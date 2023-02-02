from random import randint as RAND

x, y = RAND(1, 1000), RAND(1, 1000)
s, p = x + y, x * y

i = s//2
while i:
    if s - i == p / i:
        print(f"Загадали числа {s - i} и {i}.")
    i -= 1

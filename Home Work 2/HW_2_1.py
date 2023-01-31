from random import randint as RAND

n = int(input("Введи кол-во монет: "))
count = 0
for _ in range(n):
    coin = RAND(0, 1)
    if coin:
        count += 1

print(f"Нужно повернуть монет - {n - count}")

from random import randint as r
garden_len = int(input("Введи количество кустов с ягодами: "))

garden = [r(1, 10) for _ in range(garden_len)]
print(*garden, sep=', ')

step = 3
max_sum = sum(garden[:3])
temp_sum = max_sum
i = 1
for _ in range(garden_len-1):
    left = i - 1
    right = i + (step - 1)
    if right >= garden_len:
        right = (right + 1) % garden_len - 1
    temp_sum = temp_sum - garden[left] + garden[right]
    max_sum = max_sum if temp_sum < max_sum else temp_sum
    i = (i + 1) % garden_len

print(f"Наибольшая сумма ягод с ближайших 3-х кустов = {max_sum}")

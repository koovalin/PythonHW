def sum_numbers(a: int, b: int):
    if b == 0: return a
    return sum_numbers(a + 1, b - 1)


print(sum_numbers(1, 99))

def degree(a: int, b: int):
    if b == 0: return 1
    return a * degree(a, b - 1)


print(degree(2, 1))

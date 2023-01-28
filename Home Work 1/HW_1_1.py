# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6(1 + 2 + 3)
# 100 -> 1(1 + 0 + 0)


def sum_all(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_all(n // 10)


a = 123
b = 100

print(sum_all(a))
print(sum_all(b))


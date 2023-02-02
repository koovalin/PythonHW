n = int(input("Максимальное число степени двойки: "))
x = 0
list_ = []
while 2 ** x < n:
    list_.append(2 ** x)
    x += 1
print(*list_, sep=",")

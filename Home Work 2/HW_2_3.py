n = int(input("Максимальное число степени двойки: "))
my_list = []
x = 0
while 2 ** x < n:
    my_list.append(2**x)
    x += 1
print(*my_list, sep=", ")

from random import randint as RAND

list_range = int(input("Введи размер массива: "))
find_number = int(input("Какое число ищем: "))

my_list = [RAND(1, 100) for _ in range(list_range)]

if find_number in my_list:
    print(f"Число {find_number} было найдено {my_list.count(find_number)} раз(а)!")
else:
    close_number = -1
    while True:
        lower_number = higher_number = find_number
        lower_number -= 1
        higher_number += 1
        if lower_number in my_list:
            close_number = lower_number
            break
        if higher_number in my_list:
            close_number = higher_number
            break
    print(f"Числа {find_number} нет в списке. Ближайшее число {close_number} ")

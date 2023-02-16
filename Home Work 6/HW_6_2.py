# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
my_list = [29, 0, 9, 21, 67, 2, 83, 32, 37, 2]

quations_list = ['Введи минимальное число: ', 'Введи максимальное число: ']
answers = [int(input(x)) for x in quations_list]
min_val, max_val = [n for n in answers]
new_list = [x for x in my_list if min_val < x < max_val]


print(new_list)

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows: int = 6, num_columns: int = 6) -> print:
    matrix = [[0] * num_columns for _ in range(num_rows)]
    for row in range(num_rows):
        matrix[row][0] = row + 1
    for col in range(num_columns):
        matrix[0][col] = col + 1

    for row in range(1, num_rows):
        for col in range(1, num_columns):
            matrix[row][col] = operation(matrix[row][0], matrix[0][col])

    for line in matrix:
        print(*(f'{i:<4}' for i in line), sep='')


print_operation_table(lambda x, y: x*y)

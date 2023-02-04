num = int(input("Число для проверки:\n"))


def sum_all(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_all(n // 10)


def is_lucky(number):
    if len(str(number)) != 6:
        return print("Invalid")
    a = sum_all(int(str(number)[3::]))
    b = sum_all(int(str(number)[:3:]))
    if a == b:
        return print("Число счастливое!")
    return print('Число не счастливое!')


is_lucky(num)

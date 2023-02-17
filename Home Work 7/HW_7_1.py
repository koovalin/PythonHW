# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам


# V1
def is_rithm_v1(__self__: list, letters: str = 'аяуюоеёэиы') -> str:
    vowels_counter = [sum([word.count(letter) for letter in letters if letter in word]) for word in __self__]
    return "Парам пам-пам" if sum(vowels_counter)/len(vowels_counter) == vowels_counter[0] else "Пам парам"


# V2
def is_rithm_v2(__self__: list, letters: str = 'аяуюоеёэиы') -> str:
    vowels_counter = []
    for word in __self__:
        vowels_counter.append(sum(word.count(letter) for letter in letters if letter in word))
    if sum(vowels_counter)/len(vowels_counter) == vowels_counter[0]:
        return "Парам пам-пам"
    else:
        return "Пам парам"


print(is_rithm_v1(input("Введите стих: ").split()))
print(is_rithm_v2(input("Введите стих: ").split()))

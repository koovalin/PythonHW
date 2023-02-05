# word = "ноутбук"
word = str(input("Введите слово для подсчета его стоимости: "))

points = {'1' : "AEIOULNSTRАВЕИНОРСТ",
          '2' : "DGДКЛМПУ",
          '3' : "BCMPБГЁЬЯ",
          '4' : "FHVWYЙЫ",
          '5' : "KЖЗХЦЧ",
          '8' : "JXШЭЮ",
          '10': "QZФЩЪ"}

cost = 0
for letter in word.upper():
    for key in points:
        if letter in points[key]:
            cost += int(key)
print(f"Стоимость слова = {cost}")

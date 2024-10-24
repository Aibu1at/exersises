"""
Формат ввода
Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода
Выводится один символ в нижнем регистре — наиболее часто встречающийся.
"""

d = {}
while (string := input()) != "ФИНИШ":
    for char in string.lower():
        if char in d:
            d[char] += 1
        elif char != " ":
            d[char] = 1
print(d)
print(max(d, key=d.get))
"""
Давайте сделаем программу, которая сокращает длинный заголовок до требуемой длины и завершает его многоточием ..., если это требуется.

Формат ввода
Вводится натуральное число L — необходимая длина заголовка.
Вводится натуральное число N — количество строк в заголовке новости.
В каждой из последующих N строк записано по одной строке заголовка.
"""


lenght = int(input())
n = int(input())
fin = ""
num_of_line_feeds = 0
for _ in range(n):
    string = input()
    if len(fin) + num_of_line_feeds <= lenght - 3:
        fin += string + "\n"
        num_of_line_feeds += 1
if len(fin) + num_of_line_feeds > lenght - 3:
    fin.rstrip("\n")
    fin = fin[:lenght - 4 + num_of_line_feeds] + "..."
print(fin)
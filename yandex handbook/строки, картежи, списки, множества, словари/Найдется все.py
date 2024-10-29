"""
Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
Порядок заголовков должен сохраниться.
"""

n = int(input())
strings = []
for _ in range(n):
    strings.append(input())
request = input()
for string in strings:
    if string.lower().count(request.lower()):
        print(string)
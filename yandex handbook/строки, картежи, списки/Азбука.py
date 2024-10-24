"""
YES — если все слова начинаются с нужной буквы.
NO — если хотя бы одно слово начинается не с нужной буквы.
"""

n = int(input())
start_with_ABC = True
for i in range(n):
    word = input()
    if word[0] not in "абв":
        start_with_ABC = False
print("YES" if start_with_ABC else "NO")
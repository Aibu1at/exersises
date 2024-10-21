"""Напишите программу, которая определяет количество палиндромов в переданном списке."""

n = int(input())
count = 0
for _ in range(n):
    inp =  input()
    is_pal = True
    for i, _ in enumerate(inp):
        if inp[i] != inp[len(inp) - i - 1]:
            is_pal = False
            break
    count += is_pal
print(count)
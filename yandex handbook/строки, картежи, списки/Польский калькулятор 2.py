"""
бинарные:
+ (сложение),
- (вычитание),
* (умножение),
/ (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);

унарные:
~ (унарный минус — меняет знак),
! (факториал),
# (клонирование — вернуть в стек значение дважды);

тернарные:
@ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).
"""


inp = input().split()
stack = []
for c in inp:
    match c:
        case '+':
            stack[-2] += stack[-1]
            stack.pop()
        case '-':
            stack[-2] -= stack[-1]
            stack.pop()
        case '*':
            stack[-2] *= stack[-1]
            stack.pop()
        case "/":
            stack[-2] //= stack[-1]
            stack.pop()

        case "~":
            stack[-1] = - stack[-1]
        case "!":
            fact = 1
            for i in range(1, stack[-1] + 1):
                fact *= i
            stack[-1] = fact
        case "#":
            stack.append(stack[-1])

        case "@":
            stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
        case _:
            stack.append(int(c))
print(stack[0])

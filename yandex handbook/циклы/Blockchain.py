'''Следует вывести номер первого блока, у которого неправильный хэш (не меньше 100 или не совпадает 
с вычисленным по указанной в условии формуле), или -1, если все хэши в блокчейне правильные.
Нумерация блоков идёт с нуля, так что они имеют номера от 0 до N-1.'''

def hash_check(m: int, r: int, h_prev: int, h: int) -> bool:
    return (h == (37 * (m + r + h_prev)) % 256) and (h < 100)


n = int(input())
number_of_wrong = -1
hash_prev = 0

for i in range(n):
    block = int(input())
    hash = block % 256
    r = (block // 256) % 256
    m = block // 256**2
    if not hash_check(m, r, hash_prev, hash):
        number_of_wrong = i
        break
    hash_prev = hash

print(number_of_wrong)

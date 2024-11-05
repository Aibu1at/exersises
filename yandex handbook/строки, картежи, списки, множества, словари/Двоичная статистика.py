"""
Напишите программу, которая для переданных чисел вычисляет:
количество разрядов;
количество единиц;
количество нулей.
"""

def dec_to_bin(dec: int) -> str:
    result = ""
    while dec != 0:
        result = str(dec % 2) + result
        dec //= 2
    return result


nums = [int(x) for x in input().split()]
fin = []
for num in nums:
    bin_num = dec_to_bin(num)
    fin.append({"digits": len(bin_num), "units": bin_num.count("1"), "zeros": bin_num.count("0")})
print(fin)
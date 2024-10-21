n = int(input())
count = 0
for i in range(n):
    contain_rabbit = False
    while (word := input()) != "ВСЁ":
        if word == "зайка":
            contain_rabbit = True
    count += contain_rabbit
print(count)
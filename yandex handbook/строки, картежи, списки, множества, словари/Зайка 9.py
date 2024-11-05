d = {}
while inp := input().split():
    for word in inp:
        d[word] = d.get(word, 0) + 1

print(*(f"{word} {count}" for word, count in d.items()), sep="\n")
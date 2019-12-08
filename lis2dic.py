l = [["banana", "oranges", "grapes"],["banana", "grapes"],["grapes", "oranges", "banana"]]
d = {}
for i in l:
    if i[0] not in d:
        d[i[0]] = 1
    else:
        d[i[0]] += 1
    for w in i[1:]:
        if w not in d:
            d[w] = 0


print(d)


def example(box):
    diagonal = ''
    for listed in range(len(box)):
        print()
        for letters in range(listed + 1):
            diagonal += box[listed - letters][letters]
            print(box[listed - letters][letters], end=", ")
            print(f"[{listed - letters}][{letters}]", end=" ")
    return diagonal


print(example([['a', 'b', 'c', 'p', 'q'],
               ['d', 'e', 'f', 'j', 'r'],
               ['g', 'h', 'i', 'k', 's'],
               ['l', 'm', 'n', 'o', 't'],
               ['5', '4', '3', '2', '1'],
               ]))
x = [['a', 'b', 'c', ],
     ['e', 'f', 'g'],
     ['h', 'i', 'j']]

print([b for a in x[::-1] for b in a[::-1]])

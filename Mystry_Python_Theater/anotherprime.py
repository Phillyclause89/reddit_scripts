import numpy as np


def isprime(x):
    root = np.sqrt(x)
    print("root ==>", root)
    print("Loop i values ==>", [i for i in range(2, int(root), 1)])
    for i in range(2, int(root), 1):
        print("i ==>", i)
        print("x % i ==>", x % i, "(x % i==0) ==> ", (x % i == 0))
        print("int(root) ==>", int(root), "(i < int(root)) ==> ", (i < int(root)))
        print("x % i == 0 and i < int(root) ==>", (x % i == 0 and i < int(root)))
        if x % i == 0 and i < int(root):
            return False
            break
        else:
            i += 1
            print("i+=1 ==>", i)
    else:
        return True


for x in [x for x in range(0, 20)]:
    print("x==>", x)
    print("function returns:", isprime(x))
    print("-----------------------------")

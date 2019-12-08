def is_prime(x):
    if x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    elif x == 0 or x == 1:
        return False
    elif x == 2:
        return True


print(is_prime(9))

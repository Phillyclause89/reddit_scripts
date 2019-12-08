def nth_right_split_prime(n):
    p = 23
    split_primes = [2, 3, 5, 7]
    while len(split_primes) < n:
        prime = True
        for num in range(2, p // 2):
            if p % num == 0:
                prime = False
                break
        if prime:
            split_prime = True
            for c in str(p):
                if int(c) not in split_primes[0:4]:
                    split_prime = False
                    break
            if split_prime:
                split_primes.append(p)
        p += 2
    return split_primes[n - 1]


print(nth_right_split_prime(1000))

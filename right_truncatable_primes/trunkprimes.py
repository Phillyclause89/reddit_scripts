def nth_split_prime(n, debug=False):
    p = 23
    split_primes = [2, 3, 5, 7]
    while len(split_primes) < n:
        split = True
        for c in str(p):
            if int(c) not in split_primes[0:4]:
                split = False
                break
        if split:
            split_prime = True
            for num in range(2, p // 2):
                if p % num == 0:
                    split_prime = False
                    break
            if split_prime:
                split_primes.append(p)
                print(f"Split Prime #{len(split_primes)} is {split_primes[-1]}") if debug else 0
        p += 2
    return split_primes[n - 1]


print(nth_split_prime(1000000, True))

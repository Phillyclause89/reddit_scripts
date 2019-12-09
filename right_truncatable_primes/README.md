# r/learnpython Adventure Summary
  Note, after adding my 2 cents to this post, I have since wrote a more optimal split primes func:
```python
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
```

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/right_truncatable_primes/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/right_truncatable_primes/requirements.txt?style=plastic) | requirements.txt for this adventure.
trunkprimes.py| ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/right_truncatable_primes/trunkprimes.py?style=plastic) | code for this adventure.
  
## Source Link:
  * [ r/learnpython/.../right_truncatable_primes ]( https://www.reddit.com/r/learnpython/comments/e4niv0/right_truncatable_primes/ )
  
## Post Title:
  > Right truncatable primes
  
## Post Body:
  > Hi guys im new at python and im trying to code something my school gave me a challenge to try and code a program that outputs the nth right truncatable prime.
  > We define a right-truncatable prime as a prime number such that, if the rightmost digit is successively removed, then all the resulting numbers are prime. For example, 7393 is a right-truncatabie e number, since
  > 7393, 739, 73 and 7 are all prime.
  > Given a positive integer n, i want to write a program which outputs the n-th right-truncatable prime number, starting from 2. For example, the first four right-truncatable prime numbers are 2, 3, 5, and 7. However, since 1 is not prime, the prime numbers following these, viz. 11, 13, 17, and 19, are not right-truncatable prime numbers.
  > I have tried to code this and look at the output but it is not outputting the corecct numbers. Here is my code:
  > ```python
  > right_truncatable_primes = []
  > ans = 0
  > for x in range(3, 100):
  >     for i in range(len(str(x)), 0, -1):
  >         num = int(str(x)[0:i])
  >         for ix in range(2, num):
  >             if num % ix == 0 and num not in {2, 3, 5, 7}:
  >                 ans = 0
  >                 break
  >         else:
  >             ans += 1
  >     if int(str(x)[0]) != 1:
  >         if ans == len(str(x)):
  >             right_truncatable_primes.append(x)
  >   ```

### My Comment(s):
  > Here is a function that will return the nth split prime (a prime where each individual digit is also prime.) Can you modify it to return the nth right truncatable prime?
  > ```python
  > def nth_right_split_prime(n):
  >     p = 23
  >     split_primes = [2, 3, 5, 7]
  >     while len(split_primes) < n:
  >         prime = True
  >         for num in range(2, p//2):
  >             if p % num == 0:
  >                 prime = False
  >                 break
  >         if prime:
  >             split_prime = True
  >             for c in str(p):
  >                 if int(c) not in split_primes[0:4]:
  >                     split_prime = False
  >                     break
  >             if split_prime:
  >                 split_primes.append(p)
  >         p += 2
  >     return split_primes[n - 1]
  >     
  >     
  > for i in range(1,10):
  >     print(nth_right_split_prime(i))
  > ```
 

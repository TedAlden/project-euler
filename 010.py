"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the
primes below two million.
"""

import math


def is_prime(n):
    """Returns whether a given integer is prime"""
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


def prime_numbers_upto(n):
    """Yields all prime numbers between 2 and n"""
    for num in range(2, n+1):
        if is_prime(num):
            yield num


if __name__ == "__main__":
    primes = [prime for prime in prime_numbers_upto(2000000)]

    print(sum(primes))

# solution = 142913828922

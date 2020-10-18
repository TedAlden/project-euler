"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
"""

import math


def is_prime(n):
    """Returns whether a given integer is prime"""
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


if __name__ == "__main__":
    number_of_primes = 0
    number = 0

    while number_of_primes <= 10001:
        number += 1
        if is_prime(number):
            number_of_primes += 1

    print(number)

# solution = 104743

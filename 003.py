"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor
of the number 600851475143 ?
"""

import math


def prime_numbers_upto(n):
    """Yields all prime numbers between 2 and n"""
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            yield num


if __name__ == "__main__":
    NUM = 600851475143
    prime_factors = []

    for i in prime_numbers_upto(int(math.sqrt(NUM)) + 1):
        if NUM % i == 0:
            prime_factors.append(i)

    print(max(prime_factors))

# solution = 6857

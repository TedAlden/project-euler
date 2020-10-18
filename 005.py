"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder. What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

# Using the information, we can assume that it will be a multiple of 2520.

import functools


def factorial(n):
    return functools.reduce(lambda a, b: a * b, range(1, n + 1))


if __name__ == "__main__":
    number = 0

    while number < factorial(20):
        number += 2520
        if all(number % i == 0 for i in list(range(2, 20))):
            break

    print(number)

# solution = 232792560

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
"""


def multiple_of(a, b):
    """Returns whether a is a multiple of b"""
    if a % b == 0:
        return True
    return False


if __name__ == "__main__":
    total = 0

    for i in range(1, 1000):
        if multiple_of(i, 3) or multiple_of(i, 5):
            total += i

    print(total)

# solution = 233168

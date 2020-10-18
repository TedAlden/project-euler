"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be: # 1, 2, 3, 5, 8,
13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.
"""


def fibonacci(n):
    """Returns all fibonacci numbers upto c, starting with a and b"""
    a, b = 0, 1
    while a + b < n:
        yield a + b
        a, b = b, a + b


if __name__ == "__main__":

    total = 0

    for i in fibonacci(4000000):
        if i % 2 == 0:
            total += i

    print(total)

# solution = 4613732

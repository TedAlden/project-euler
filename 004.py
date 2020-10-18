"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""


def reverse(x):
    """Reverses a string."""
    return str[::-1]


def is_palindrome(n):
    """Returns whether a number is a palindrome"""
    num = list(str(n))
    h1 = num[:int(len(num)/2)]  # first half of palindrome
    if len(num) % 2 == 0:
        h2 = num[int(len(num)/2):]  # second half of palindrome
    else:
        h2 = num[int(len(num)/2) + 1:]
    return h1 == list(reversed(h2))


if __name__ == "__main__":
    palindromes = []

    for i in range(100, 1000):  # should be backwards from 1000 to 100...
        for j in range(100, 1000):
            if is_palindrome(i * j):
                palindromes.append(i * j)

    print(max(palindromes))

# solution = 906609

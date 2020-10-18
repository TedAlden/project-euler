"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural numbers and the
square of the sum.
"""

# first one hundred natural numbers:
first_100 = range(101)

# sum of the squares of the first one hundred:
sum_of_squares = sum(map(lambda x: x ** 2, first_100))

# square of the sum of the first one hudred numbers:
square_of_sums = sum(first_100) ** 2

print(abs(sum_of_squares - square_of_sums))

# solution = 25164150

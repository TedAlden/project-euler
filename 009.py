"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2. E.g. 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists exactly one
Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

num = 1000
solutions = set()  # use a set to avoid duplicates


for a in range(num/2):
    for b in range(num/2):
        c = num - (a + b)
        if c == 0:
            continue
        if (a ** 2) + (b ** 2) == c ** 2:
            solutions.add(a*b*c)

print(solutions)

# solution = 31875000

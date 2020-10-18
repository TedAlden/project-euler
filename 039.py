"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120: {20,48,52}, {24,45,51},
{30,40,50}. For which value of p <= 1000, is the number of solutions maximised?
"""

#        /|
# c	    / |	b
#      /  |
#     /___|
#       a


def f(p_max):
    solutions = {}

    for p in range(1, p_max):
        solutions[str(p)] = 0
        for a in range(1, int(p/2)):
            for b in range(1, int(p/2)):
                c = p - (a + b)
                if (a ** 2) + (b ** 2) == c ** 2 and type(c) == int:
                    solutions[str(p)] += 1

    return solutions


sol = f(1000)

# Sort the dictionary by value i.e the amount of solutions each value of p has
for key, value in sorted(sol.iteritems(), key=lambda k, v: (v, k)):
    print(key, value)

# solution = 840

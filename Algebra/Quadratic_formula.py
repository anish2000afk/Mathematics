# Program for Quadratic Formula
import math

"New code"


def solve_quadratic(a, b, c):
    disc = b**2 - 4 * a * c

    if disc < 0:
        return "no real roots"
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    return root1, root2


"""My old code"""
# # Take input separated by spaces
# values = input("Enter 3 values separated by spaces: ").split()
#
# # Convert to integers
# a, b, c = map(float, values)
# disc = (b * b) - (4 * a * c)
# print(disc)
# equation_1 = (-b + math.sqrt(disc)) / (2 * a)
# equation_2 = (-b - math.sqrt(disc)) / (2 * a)
# print(equation_1, equation_2)

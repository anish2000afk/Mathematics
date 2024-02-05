# Program for Quadratic Formula
import math

# Take input separated by spaces
values = input("Enter 3 values separated by spaces: ").split()

# Convert to integers
a, b, c = map(int, values)
disc = (b * b) - (4 * a * c)
equation_1 = (-b + math.sqrt(disc)) / 2 * a
equation_2 = (-b - math.sqrt(disc)) / 2 * a
print(equation_1, equation_2)

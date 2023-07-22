# This program is relevant to Pg. 32 of Ron Larson Algebra book.
x = int(input())
for x in range(1, 8):
    volume = x * (4 * (pow(x, 3))) - (72 * (pow(x, 2))) + (320 * x)
    print(volume)

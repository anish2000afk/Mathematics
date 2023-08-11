# Relevant to question 115 of pg.48
x = int(input())
for i in range(0, x):
    print(i)
    beam6 = ((0.06 * (i * i)) - (2.42 * i) + (38.71)) * (
        (0.06 * (i * i)) - (2.42 * i) + (38.71)
    )
    beam8 = ((0.08 * (i * i)) - (3.30 * i) + (51.93)) * (
        (0.08 * (i * i)) - (3.30 * i) + (51.93)
    )
    print(beam6)
    print(beam8, "\n")
    print("Difference", (beam8 - beam6))

# Create a list of difference of differences. To-do

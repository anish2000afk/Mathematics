# Take input separated by spaces
values = input(
    "Enter intial velocity, intial height and time separated by spaces: "
).split()

# Convert to integers
v0, s0, t = map(float, values)
height = (-16 * (t * t)) + (v0 * t) + s0
print("Height of object is : ", height)

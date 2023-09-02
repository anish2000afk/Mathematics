for i in range(7):
    try:
        eq1 = ((pow(i, 2)) - (2 * i) - (3)) / (i - 3)
    except ZeroDivisionError:
        i = 0
        continue
    eq2 = i + 1
    print("i-value = ", i)
    print("Equation 1 ", eq1)
    print("Equation 2 ", eq2)

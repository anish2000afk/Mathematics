for i in range(7):
    try:
        eq1 = 1 / (i + 2)
        eq2 = (i - 3) / (pow(i, 2) - i - 6)
    except ZeroDivisionError:
        print("Zero Exception Error ")
        continue
    print("i-value = ", i)
    print("Equation 1 ", eq1)
    print("Equation 2 ", eq2)

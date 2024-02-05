def pre_val(V, i, n):
    Pnin = ((1 + i) ** n) - 1
    Pnid = i * (1 + i) ** n
    equation = V / (Pnin / Pnid)
    print(equation)


def pre_val2(A, i, n):
    Pnin = ((1 + i) ** n) - 1
    Pnid = i * (1 + i) ** n
    equation = A * (Pnin / Pnid)
    print(equation)


pre_val(10000, 0.14, 4)
pre_val2(5000, 0.04, 12)

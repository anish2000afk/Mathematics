# For finding correlation
def single_cor(n, sumx, sumy, sumxy, sumxsq, sumysq):
    import math

    eq_num = (n * sumxy) - (sumx * sumy)
    eq_den1 = math.sqrt((n * sumxsq) - (sumx * sumx))
    eq_den2 = math.sqrt((n * sumysq) - (sumy * sumy))
    final_eq = eq_num / (eq_den1 * eq_den2)
    print(final_eq)


single_cor(5, 0, -2, -57, 10, 59)

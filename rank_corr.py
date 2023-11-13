def rank_correlation(n, dsq):
    eq_num = 6 * dsq
    eq_den = n * ((n**2) - 1)
    final_eq = 1 - (eq_num / eq_den)
    print(final_eq)


def rank_correlation_joint(n, dsq, sumt):
    eq_num = 6 * (dsq + sumt)
    eq_den = n * ((n**2) - 1)
    final_eq = 1 - (eq_num / eq_den)
    print(final_eq)


rank_correlation_joint(7, 8, 1)

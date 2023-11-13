# For finding regression values for y on x.
def single_cor_y_on_x(n, sumx, sumy, sumxy, sumxsq, sumysq):
    # For finding b_hat.
    eq_num = (n * sumxy) - (sumx * sumy)
    eq_den1 = (n * sumxsq) - (sumx * sumx)
    b_hat = eq_num / eq_den1
    # Finding a_hat.
    print("Input mean values of x and y ")
    mean_x = float(input())
    mean_y = float(input())
    print(type(mean_x))
    print(mean_x, mean_y)
    a_hat = float(mean_y - (b_hat * mean_x))
    print("b_hat value = ", b_hat)
    print("a_hat value = ", a_hat)
    # Finding y on x equation.
    x_val = float(input("Input value of x for finding out y \n"))
    y_val = a_hat + (b_hat * x_val)
    print("Value of y = ", y_val)


def single_cor_x_on_y(n, sumx, sumy, sumxy, sumxsq, sumysq):
    # For finding b_hat.
    eq_num = (n * sumxy) - (sumx * sumy)
    eq_den1 = (n * sumysq) - (sumy * sumy)
    b_hat = eq_num / eq_den1
    # Finding a_hat.
    print("Input mean values of x and y ")
    mean_x = float(input())
    mean_y = float(input())
    print(type(mean_x))
    print(mean_x, mean_y)
    a_hat = float(mean_x - (b_hat * mean_y))
    print("b_hat value = ", b_hat)
    print("a_hat value = ", a_hat)
    # Finding y on x equation.
    y_val = float(input("Input value of y for finding out x \n"))
    x_val = a_hat + (b_hat * y_val)
    print("Value of x = ", x_val)

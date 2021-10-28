import math


# Var_1
def my_func(x, y):
    if x < 0:
        z = "n1 must be positive."
    elif y > 0:
        z = "n2 must be negative."
    else:
        z = x ** y
    return z


# Var_2
def my_func_2(x, y):
    it = 1
    z = x
    while it < abs(y):
        z = z * x
        it += 1
    return 1 / z


arg_1 = float(input("enter positive n1: "))
arg_2 = int(input("enter negative integer n2: "))
print(my_func(arg_1, arg_2))
print(my_func_2(arg_1, arg_2))





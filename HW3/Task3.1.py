def my_funk(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        z = "Zero division is not allowed."
    return z


arg_1 = int(input("enter integer n1: "))
arg_2 = int(input("enter integer n2: "))

print(my_funk(arg_1, arg_2))

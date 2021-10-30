def my_func(x, y, z):
    if x < y and z:
        return y + z
    elif y < z and x:
        return x + z
    elif z < y and x:
        return y + x
    else:
        return "Wrong values. Try again "


print(my_func(1, 55, 3))

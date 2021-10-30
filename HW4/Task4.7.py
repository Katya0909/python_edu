from math import factorial


def fact_2(n):
    generator = [i for i in range(1, n + 1)]
    for i in generator:
        yield factorial(i)


for el in fact_2(5):
    print(el)

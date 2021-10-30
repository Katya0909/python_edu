# Вариант 1

a = int(input("Введите число от 1 до 9 включительно: "))
b = 10 * a + a
c = 100 * a + b
d = a + b + c
print(d)

# Вариант 2

x = int(input("Введите число от 1 до 9 включительно: "))
print(x)
print(x * 10 + x)
print(x * 100 + x * 10 + x)
y = x + (x * 10 + x) + (x * 100 + x * 10 + x)
print(y)


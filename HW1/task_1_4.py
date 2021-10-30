number = int(input("Введите целое положительное число: "))

if number <= 0:
    print("Введите положительное число")
else:
    max_number = 0
    while number > 0:
        digit = number % 10
        if max_number < digit:
            max_number = digit
        number = int(number / 10)
    print("Наибольшая цифра в числе :", max_number)



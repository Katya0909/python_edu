income = int(input("Введите размер выручки за период 01.2020-01.2021: "))
expenses = int(input("Введите размер расходов за аналогичный период: "))
profit = income - expenses

if income > expenses:
    print("Ваша фирма прибыльна")
    profitability = (profit / income) * 100
    print("Рентабельность фирмы по товарообороту: " + str(profitability) + " %")
    employees = int(input("Введите численность сотрудников: "))
    emplprofitability = profit / employees
    print("Прибыль в расчете на одного сотрудника: " + str(emplprofitability))
if income < expenses:
    print("Ваша фирма убыточна")
if income == expenses:
    print("Точка безубыточности")

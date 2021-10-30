def my_func(lst):
    summa = 0
    for i in lst:
        if i.isdigit():
            summa = summa + int(i)
    return summa


break_cycle = False
sm = 0
while True:
    int_str = input("enter special symbol '#$%' when you want to stop :")
    list_to_calculate = []
    for el in int_str.split(" "):
        if el != "#$%":
            list_to_calculate.append(el)
        else:
            break_cycle = True
    sm = sm + my_func(list_to_calculate)
    print(f"Current sum: {sm}")
    if break_cycle:
        break

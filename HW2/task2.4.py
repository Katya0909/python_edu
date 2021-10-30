lst = input("enter several words separated by a space: ")
lst_a = lst.split(' ')
for ind, el in enumerate(lst_a, 1):
    if len(el) > 9:
        print(ind, el[0:10])
    else:
        print(ind, el)

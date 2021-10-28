my_lst = [7, 5, 3, 3, 2]
numb = int(input("enter integer: "))

break_loop = False

if numb <= my_lst[len(my_lst)-1]:
    my_lst.insert(len(my_lst), numb)
    break_loop = True
for ind, val in enumerate(my_lst.copy()):
    if numb > val:
        break_loop = True
        my_lst.insert(ind, numb)
    if break_loop:
        break

print(my_lst)

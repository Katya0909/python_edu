lst = input("enter several integers or words separated by a space: ")
data_lst = lst.split(' ')
i = 0
while i < len(data_lst)-1:
    data_lst[i], data_lst[i+1] = data_lst[i + 1], data_lst[i]
    i += 2

print(data_lst)

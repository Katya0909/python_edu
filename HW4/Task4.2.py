my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for index, el in enumerate(my_list) if el > my_list[index - 1]]
print(my_list)
print(new_list[1::])

final_dict = {}
with open('task5.6.txt', 'r') as new_file:
    f_lines = new_file.readlines()
    for line in f_lines:
        split_line = line.split(': ')
        d_name = split_line[0]
        d_hour = split_line[1]
        list_d_hour = d_hour.split(' ')
        sum_hour = 0
        for el in list_d_hour:
            split_number = el.split('(')
            if el != "-":
                el_hours = el.split("(")
                sum_hour = sum_hour + int(el_hours[0])
        final_dict[d_name] = sum_hour
print(final_dict)

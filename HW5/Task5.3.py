with open('task5.3.txt', 'r') as f:
    lines = f.readlines()
    salary_sum = 0
    for line in lines:
        line_list = line.split(' : ')
        if int(line_list[1]) < 20000:
            print("Salary less then 20 000 has", line_list[0])
        count_lines = int(len(lines))
        salary_sum = salary_sum + int(line_list[1])
        average_income = salary_sum / count_lines
    print("Average income is:", average_income)

result_list = []
firm_dict_profit = {}
firm_dict_average = {}
with open('task5.7.txt', 'r') as new_file:
    f_lines = new_file.readlines()
    firm_count = 0
    profit_sum = 0
    for line in f_lines:
        split_line = line.split(' ')
        firm_name = split_line[0]
        firm_income = split_line[2]
        firm_expenses = split_line[3]
        firm_profit = int(firm_income) - int(firm_expenses)
        firm_dict_profit[firm_name] = firm_profit
        if firm_profit >= 0:
            firm_count += 1
            profit_sum = profit_sum + firm_profit
    average_profit = profit_sum / firm_count
    firm_dict_average["average_profit"] = average_profit
result_list.append(firm_dict_profit)
result_list.append(firm_dict_average)

print(result_list)

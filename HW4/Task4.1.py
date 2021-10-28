from sys import argv
script_name, output_h, range_h, bonus = argv


def salary_func(a, b, c):
    salary = (int(a) * int(b)) + int(c)
    return salary


salary_result = salary_func(output_h, range_h, bonus)
print(salary_result)

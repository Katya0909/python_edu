import random

generate_list = [str(random.randint(1, 100)) for i in range(8)]
final_str = " ".join(generate_list)

with open('task5.5.txt', 'w') as f_out:
    f_out.write(final_str)

with open('task5.5.txt', 'r') as f_inp:
    data = f_inp.read()
    print(data)
    new_data = data.split(' ')
    summa = 0
    for el in new_data:
        summa = summa + int(el)
print(summa)

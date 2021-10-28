from itertools import count
from itertools import cycle

my_list = []
for el in count(3):
    if el > 10:
        break
    else:
        my_list.append(el)

print(my_list)

a = 0
for element in cycle(my_list):
    if a > 20:
        break
    print(element)
    a += 1


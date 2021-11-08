class MyError(Exception):
    def __init__(self):
        self.my_err = "Wrong data type"


result_list = []
break_loop = False
while True:
    inp_string = input("enter integers divided by space, to stop enter word 'stop':")
    for el in inp_string.split(" "):
        if el == 'stop':
            break_loop = True
        else:
            try:
                if el.isdigit():
                    result_list.append(el)
                else:
                    raise MyError
            except MyError as e:
                print(e.my_err)
    if break_loop:
        break
print(result_list)

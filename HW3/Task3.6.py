def int_func(x):
    words_list = x.split(" ")
    result_str = ""
    for el in words_list:
        result_str += " " + el.capitalize()
    return result_str.lstrip()


txt = input("enter a word with a small letter: ")
print(int_func(txt))

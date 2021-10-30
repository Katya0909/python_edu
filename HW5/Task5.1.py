f_1 = open("my_file.txt", 'w')
while True:
    data = input("write some words about you, when you stop tap enter: ")
    if data:
        f_1.write(data + "\n")
    else:
        break
f_1.close()

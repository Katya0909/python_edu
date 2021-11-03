with open("text5.2.txt", 'r') as f:
    lines = f.readlines()
    count_lines = len(lines)
    print("Lines", count_lines)
    line_number = 1
    for line in lines:
        print(str(line_number) + " : " + str(len(line.split(' '))))
        line_number += 1

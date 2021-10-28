translation_dict = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}


with open('task5.4.txt', 'r')as f:
    file_content = f.readlines()
    output_file = open("output_task5.4.txt", "w")
    for line in file_content:
        # print(line)
        split_line = line.split(" - ")
        print(translation_dict[split_line[0]], " - ", split_line[1])
        output_file.write(f"{translation_dict[split_line[0]]} - {split_line[1]}")
    output_file.close()

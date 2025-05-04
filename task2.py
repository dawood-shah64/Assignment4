with open('output.txt', 'w') as file:
    data_1 = input("enter text to write to the file: ")
    file.write(data_1 +'\n')
    print('Data successfully written to output.txt.' + '\n')
with open('output.txt', 'a') as file:
    data_2 = input("enter addtional text to appned: ")
    file.write(data_2 + '\n')
    print('Data successfully appended.'+ '\n')
with open('output.txt', 'r') as file:
    print("Final content of output.txt: ")
    print(file.read())


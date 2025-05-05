file_name = input('Enter file name: ')
try:
    with open(file_name, "r") as file:
        print('reading file content:')
        print("line 1: ", file.readline())
        print("line 2: ", file.readline())
except FileNotFoundError:
    print("The file", file_name, "was not found.")
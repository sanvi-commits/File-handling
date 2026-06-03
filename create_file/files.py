def create_file():
    file_name = input("Enter the name of the file to create: ")
    file = open(file_name, 'w')
    file_content = input("Enter some text to write to the file: ")
    file.write(file_content)
    file.close()

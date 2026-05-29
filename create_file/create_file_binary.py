import pickle
def create_binary():
    file_name = input("Enter the name of the binary file to create: ")
    data = input("Enter some data to write to the binary file: ")
    file = open(f"{file_name}", "wb")
    pickle.dump(data, file)
    file.close()
    print("Binary file created successfully.")
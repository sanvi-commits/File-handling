file=open("file.txt", "a+")
file_content=input("Enter the date you want to append to the file: ")
file.write(file_content + "\n")
file.close()
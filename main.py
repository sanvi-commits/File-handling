try:
    file = open("file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"The file was not found: {e}")
    file = open("file.txt", "w")
    file.write("This is a new file created because the original file was not found.")
    file.close()
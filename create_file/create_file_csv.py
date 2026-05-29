import csv
def create_csv():
    file_name = input("Enter the name of the CSV file to create: ")
    file = open(f"{file_name}", "w", newline="")
    writer = csv.writer(file)
    # Add your CSV data here
    file.close()
    print("CSV file created successfully.")
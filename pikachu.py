import csv
fh=open("employee.csv","w",newline="")
ewriter=csv.writer(fh)
empdata=[
    ['empno','name','desigination','salary'],
    ['101','john','manager','50000'],
    ['102','michael','developer','40000'],
    ['103','susan','designer','45000'],
]
ewriter.writerows(empdata)
print("file successfully created")
fh.close()                                                                                   
import csv

with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print(header)
    
    for row in reader:
        print(row)

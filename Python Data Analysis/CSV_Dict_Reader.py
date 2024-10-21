import csv

with open("Python Data Analysis\hightemp.csv",'r') as csv_file:
    data_file=csv.DictReader(csv_file)

    for row in data_file:
        print(row)
        
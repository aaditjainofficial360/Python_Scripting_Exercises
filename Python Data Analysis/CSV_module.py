import csv 

# Table List
Table=[]

with open(r'Python Data Analysis\hightemp.csv','r') as csv_file:
    data_file=csv.reader(csv_file)

    for row in data_file:
        Table.append(row)
print(Table)
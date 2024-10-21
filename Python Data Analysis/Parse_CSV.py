# Table List
table=[]
# Reading a CSV file containing high temperatures recorded for major cities of the world in different months of the year
with open(r'C:\Users\AJain204\Documents\GitHub\Python_Scripting_Exercises\Python Data Analysis\hightemp.csv','r') as csv_file:
    data_file_list=csv_file.readlines()
    for row in data_file_list:
        # print(row,end='')
        table.append(row[:-1])
print(table[1:])

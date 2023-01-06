import csv
with open("D:/Code/test_CSV_file/SampleCSVFile_1.csv") as f:

    csv_file = csv.reader(f,delimiter = ',')
    for row in csv_file:
        print(row[0],"-",row[1])
import csv
with open("D:/Code/test_CSV_file/SampleCSVFile_1.csv") as f:
    csv_file = csv.reader(f,delimiter = ',')

    # csv_file is an iterable object that we can iterate on using a for loop.
    for row in csv_file:
        print(row)  # Print entire row
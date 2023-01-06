import csv

# Use open function to read the CSV file and create
# a file object f:

with open("D:/Code/test_CSV_file/SampleCSVFile_1.csv") as f:
    # Use the reader class under the csv module to
    # read the file using comma as the delimiter

    csv_file = csv.reader(f,delimiter = ',')

    row = f.readline() # Read the firstline of the .csv
    print(row)

    row = f.readline() # Read the firstline of the .csv
    print(row)
import csv
row_1 = ["fruit_1","Mango","2kg"]
row_2 = ["fruit_2","Apple","1kg"]
row_3 = ["fruit_3","Pappaya","5kg"]

with open('fruit_list.csv','a') as csv_file:
     writer = csv.writer(csv_file, delimiter = ',')
     writer.writerow(row_1)
     writer.writerow(row_2)
     writer.writerow(row_3)

f = open('fruit_list.csv','r')
print(f.read())
f.close()
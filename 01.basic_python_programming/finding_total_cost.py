length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
price = float(input("Enter the price: "))

total_footage = length * width
total_cost = total_footage * price

print("Length: ",length)
print("Width: ",width)
print("Price: ",price)
print("Total Footage: ",total_footage)
print("Total Cost: ",total_cost)
# Creating a function to find numbers divisible by a factor.

def find_div(transactions, factor):
    for num in transactions:
        if (num % factor == 0):
            print(num)

transactions = [1,6,9,12,15,16,17,18,22,21,24,25,27,30,4,3,18,20]

print("factor of 3: \n")
find_div(transactions,3)
print("factor of 2: ")
find_div(transactions,2)
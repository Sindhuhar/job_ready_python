#In this example, we create a script to ask the user for a year, month, and day.

import datetime

year = input("Enter the year from 2001 to 2022: ")
while True:
    if int(year) >= 2001 and int(year) <= 2022:
        break
    else:
        print("Please Enter a year from 2001 to 2022: ")

month = input("Enter a month from 1 to 12: ")
while True:
    if int(month) >= 1 and int(month) <=12:
        break
    else:
        print("Please Enter a month from 1 to 12")

date = input("Enter a date from 1 to 31: ")
while True:
    if int(date) >= 1 and int(date) <= 31:
        break
    else:
        print("Please Enter a date from 1 t 31")

user_date = datetime.date(int(year),int(month),int(date))
print(user_date)
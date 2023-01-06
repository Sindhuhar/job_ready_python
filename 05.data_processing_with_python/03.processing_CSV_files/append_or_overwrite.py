import os,csv

while True:
    if os.path.exists("user_input.csv"):
        user_prompt = input("What data would you like to append[type quit to exit]? ")

        if user_prompt.lower() == 'quit' :
            break
        else:
            with open('user_input.csv','a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow([user_prompt])
    else:
        f = open('user_input.csv','w')
        print("The file user input does not exist. It has been created.")

f = open('user_input.csv','r')
print(f.read())
f.close()



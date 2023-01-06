#Create a program that takes an input list of strings, identifies all the strings with two or more characters, and stores the results in another list

a = ["a", "bc","rye","hello","c"," "]


output = []

for character in a:
    if (len(character)) >= 2 :
        print(character)
        output.append(character)


print( [ i for i in a if len(i) >= 2 ])

print( output )
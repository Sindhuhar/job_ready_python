#creating tuples
names = ("Sindhu","Abhi","Arya","Leela","jay","Vishwas","Sindhu")
search_term = "Sindhu"

if search_term in names:
    print(search_term + " appears atleast once in the tuple")
    
for name in names:
    if name == search_term:
        print("We found " + search_term)
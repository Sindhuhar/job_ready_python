import json
data = []

data.append({"Name":"Sindhu","DOB":"27/01/2001"})
data.append({"Name":"Prajwal","DOB":"20/03/2003"})

with open('person.json','w') as outfile:
    json.dump(data,outfile)

f = open('person.json','r')
print(f.read())
f.close()


import json

json_dict = {
    "first_name": "Rohini",
    "last_name": "Poojari",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

# Convert a dictionary into a JSON formatted string object.

json_data = json.dumps(json_dict)
print(json_data)
print(type(json_data))

# Convert a JSON encoded object into a python dictionary.
json_dict = json.loads(json_data)
print(json_dict)
print(type(json_dict))
import json
json_dict = {
    "first_name": "Rohini",
    "last_name": "Poojari",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

## convert a dictionary into a string object that we can display.
json_data = json.dumps(json_dict)

print(json_dict)               # dict
print(type(json_dict))

print(json_data)               # string
print(type(json_data))
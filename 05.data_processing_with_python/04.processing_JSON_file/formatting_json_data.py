import json

json_dict = {
    "first_name": "Rohini",
    "last_name": "Poojari",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

json_data = json.dumps(json_dict, indent=4)

print(json_data)
print(type(json_data))
import json

from pprint import pprint

with open("D:/Code/test_CSV_and_JSON_file/sample2.json", 'r') as jsonfile:
    data = json.load(jsonfile)  # load the json content and serialize it.
print(type(data))  # dict
pprint(data)  # print the entire file content.
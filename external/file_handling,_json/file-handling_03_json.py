import json
from os import name

a = {
    "name": "Tomas",
    "year_birth": 1987,
    "favorite_color": "red",
    "country": "Brazil",
    "marks": [10, 12, 11, 15],
    "pass": True
}

# This snippet writes dict as json to sample-file_02.json:
'''with open("sample-file_02.json", "w") as fh:
    fh.write(json.dumps(a, indent=4))
'''

# This snippet reads the content of sample-file_02.json:
with open("sample-file_02.json", "r") as fh:
    #print(fh.read())
    json_str = fh.read()
    json_value = json.loads(json_str)
    #print(json.dumps(json_value, indent=4))
    print(json_value["name"], end =" ")
    print(json_value["year_birth"], end =" ") 
    print(json_value["favorite_color"])
    print(json_value["name"], end =", ") 
    print(json_value["year_birth"], end =", ") 
    print(json_value["favorite_color"])

# manipulating json.dumps(var):
'''
print(json.dumps(a))
print()
print(json.dumps(a, indent=2))
print()
print(json.dumps(a, indent=3))
print()
print(json.dumps(a, indent=4, sort_keys=True))
print()
print(json.dumps(["1", "2"]))
print(json.dumps(("1", "2")))
print(json.dumps(100))
print(json.dumps(12.36))
print(json.dumps(False))
print(json.dumps(True))
print(json.dumps(None))
'''
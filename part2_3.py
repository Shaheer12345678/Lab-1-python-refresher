import json

# Iterate through the json dictionary recursively and set all instances of size to 42
def iterate_keys(dictionary):
    if type(dictionary) != dict:
        return
    keys = dictionary.keys()
    for key in keys:
        if key == 'size':
            dictionary[key] = 42

        
        if type(dictionary[key]) == dict:
            iterate_keys(dictionary[key])


with open("large-file.json", "r") as in_file:
    content = json.load(in_file)

for entry in content:
    iterate_keys(entry)

with open("output.2.3.json", "w") as out_file:
    content.reverse()
    json.dump(content, out_file, indent=2)
    

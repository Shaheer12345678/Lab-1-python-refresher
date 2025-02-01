import json
import timeit

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

def iterate_json_list(content):
    for entry in content:
        iterate_keys(entry)

with open("large-file.json", "r") as in_file:
    content = json.load(in_file)

iterations = 10
total_time = timeit.timeit(lambda: iterate_json_list(content), number=iterations)
average_time = total_time/iterations

print(f'Average elapsed time: {average_time} seconds')

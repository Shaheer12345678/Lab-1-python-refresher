import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

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

def iterate_json_list(content, record_target):
    records_processed = 0
    for entry in content:
        iterate_keys(entry)
        records_processed += 1
        if records_processed == record_target:
            return

def avg_processing_time(content, record_target, iterations):
    total_time = timeit.timeit(lambda: iterate_json_list(content, record_target), number=iterations)
    return total_time/iterations

with open("large-file.json", "r") as in_file:
    content = json.load(in_file)

average_times = []
list_lengths = [1000, 2000, 5000, 10000]
for length in list_lengths:
    average_times.append(avg_processing_time(content, length, 100))

slope, intercept = np.polyfit(list_lengths, average_times, 1)
plt.scatter(list_lengths, average_times)
line_values = [slope * x + intercept for x in list_lengths]
plt.plot(list_lengths, line_values, 'r')
plt.savefig("output.3.2.png")

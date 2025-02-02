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

def processing_time(content, record_target, iterations):
    total_time = timeit.timeit(lambda: iterate_json_list(content, record_target), number=iterations)
    return total_time/iterations

with open("large-file.json", "r") as in_file:
    content = json.load(in_file)

times = []
for i in range(1000):
    times.append(processing_time(content, 1000, 1))

plt.hist(times, bins=np.arange(min(times), max(times) + 0.00001, 0.00001))
plt.xlabel("Processing time (Seconds)")
plt.ylabel("Frequency")
plt.title("Processing time of first 1000 records across 1000 iterations")
plt.savefig("output.3.3.png")

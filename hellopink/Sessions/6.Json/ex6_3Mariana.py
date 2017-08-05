#3. What is the minimum and maximum population growth years.
#Make a function out of that.
#Hint, use inbuilt min, max functions.

import json

def function(data):
    dictionary = {}
    for i in range(1, len(data)):
        pop_grow = int(data[i - 1]["value"]) - int(data[i]["value"])
        years = data[i]["date"] + "-" + data[i - 1]["date"]
        print(years, pop_grow)
        dictionary[pop_grow] = years
    return dictionary

with open('data/sweden.json') as data_file:
    data = json.load(data_file)

dictionary = function(data)
print(dictionary)
min_pop_grow = min(dictionary)
print(min_pop_grow)
print(dictionary[min_pop_grow])

max_pop_grow = max(dictionary)
print(max_pop_grow)
print(dictionary[max_pop_grow])

"""
dictionary = {}

for i in range(1,len(data)):
    pop_grow = int(data[i-1]["value"])-int(data[i]["value"])
    years = data[i]["date"] + "-" + data[i-1]["date"]
    print(years, pop_grow)
    dictionary[pop_grow] = years

print(dictionary)
min_pop_grow = min(dictionary)
print(min_pop_grow)
print(dictionary[min_pop_grow])

max_pop_grow = max(dictionary)
print(max_pop_grow)
print(dictionary[max_pop_grow])

"""
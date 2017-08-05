#What is the average minimum and maximum population growth years.
# Make a function out of that. Hint, use inbuilt min, max functions.
import json
import numpy
from pprint import pprint
with open('data/sweden.json')as data_file:
    sweden = json.load(data_file)

average_list = []
for i in range(0,len(sweden)-1):
    difference = int(sweden[i]['value']) - int(sweden[i+1]['value'])/2
    average_list.append(difference)
print(average_list)
print(numpy.min(average_list))
print(numpy.max(average_list))


mini=100000000
for value in average_list:
    if value < mini:
        mini = value
print(mini)

maxi = 100
for value in average_list:
    if value > maxi:
        maxi = value
print(maxi)


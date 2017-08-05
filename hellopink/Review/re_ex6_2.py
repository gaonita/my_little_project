#What is the average population growth between the years.
# E.g. between 2015 and 2016 the population growth is 103936.
# Hint: To calculate the average of 1 and 2 you would need to run:  numpy.mean([1,2])
# output: 1.5. Make a function out of that.

import json
import numpy
from pprint import pprint
with open('data/sweden.json')as data_file:
    sweden = json.load(data_file)

sum = 0
average_list = []
for i in range(0,len(sweden)-1):
    difference = int(sweden[i]['value']) - int(sweden[i + 1]['value'])
    sum = sum + difference
    average_list.append(difference)
print(average_list)
print(numpy.mean(average_list))
print(sum / len(average_list))
#for all in pop_list:
    #x = 0
    #x = x+1
    #average = numpy.mean(pop_list[x],pop_list[x-1])
    #average_list.append(average)

# pprint(sweden)

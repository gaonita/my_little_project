#1. Find the year with lowest population in Sweden. Hint: use loops and min.
import json
from pprint import pprint
with open('data/sweden.json') as data_file:
    data = json.load(data_file)
    lowest_population = 100000000
    for dict in data:
        if int(dict["value"]) < lowest_population:
            lowest_population = int(dict["value"])
            lowest_year = dict["date"]
    print(lowest_population, lowest_year)



#2. What is the average population growth between the years.
#E.g. between 2015 and 2016 the population growth is 103936.
#Hint: To calculate the average of 1 and 2 you would need to run:  numpy.mean([1,2])
#output: 1.5. Make a function out of that.

#import numpy.mean([1,2])
import json
from pprint import pprint
with open('data/sweden.json') as data_file:
    data = json.load(data_file)
    for dict in data:
        def population_average(date1,date2):
            date1 = int(dict["value"])
            date2 = int(dict["value"])
            average = date1 -- date2
            return average
    my_average = population_average(2014,2015)
    print(my_average)


#3. What is the average minimum and maximum population growth years.
#Make a function out of that.
#Hint, use inbuilt min, max functions.

import json
from pprint import pprint

with open('data/sweden.json') as data_file:
    sweden = json.load(data_file)
#Find the year with lowest population in Sweden.
# i = 0
# pop_list = []
# for population in sweden:
#     i =i+1
#     population = sweden[i-1]['value']
#     pop_list.append(population)
#
# i= 0
# lowest=10000000
# for minus in pop_list:
#     i = i+1
#     a= int(pop_list[i])
#     b= int(pop_list[i-1])
#     if a <= b:
#         lowest = a
#     else:
#         lowest = b
# print(lowest)

lowest=100000000
for i in sweden:
    lowest = min(lowest, int(i['value']))
print(lowest)

for i in sweden:
    if int(i['value']) == lowest:
        print (i['date'])


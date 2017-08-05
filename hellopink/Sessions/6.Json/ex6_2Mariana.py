#import numpy
#print(numpy.mean([1,2]))

import json
from pprint import pprint
with open('data/sweden.json') as data_file:
    data = json.load(data_file)

list = []

for i in range(1,len(data)):
    print(data[i]["date"])
    print(data[i-1]["date"])
    kittens = int(data[i-1]["value"])-int(data[i]["value"])
    list.append(kittens)
    print(kittens)




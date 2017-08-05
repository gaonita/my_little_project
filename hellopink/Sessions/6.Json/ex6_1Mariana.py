import json
from pprint import pprint
with open('data/sweden.json') as data_file:
    data = json.load(data_file)

low_value=1000000000

for population in data:
    value = int(population["value"])
    if value < low_value:
        low_value = value

print(low_value)

for population in data:
    if int(population["value"]) == low_value:
        print(population["date"])


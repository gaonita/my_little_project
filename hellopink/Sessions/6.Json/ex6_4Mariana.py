#4. Given the sweden country data convert it into a list with dictionaries in this form:
# [ { 'population': 9903122, 'year': 2016}, .... ]. Make a function out of that.

import json
from pprint import pprint
with open('data/sweden.json') as data_file:
    data = json.load(data_file)

my_list = []
for blob in data:
    content = ({"year":blob["date"],"population":blob["value"]})
    print(content)
    my_list.append(content)
print(my_list)
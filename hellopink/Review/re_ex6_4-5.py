#Given the sweden country data convert it into a list with dictionaries
# in this form:[ { 'population': 9903122, 'year': 2016}, .... ].
#  Make a function out of that.
import json
from pprint import pprint
with open('data/sweden.json')as data_file:
    sweden = json.load(data_file)


# pop_dic = {}
# for i in range(0,len(sweden)):
#     pop_dic['population'] = sweden[i]['value']
#     pop_dic['year'] = sweden[i]['date']
#     print(pop_dic)
#

#Create a list where you have the year pairs and the growth from one year to another.
    # Example [ { 'pair': '2015-2016', 'growth': 103936}, .... ].

pair_dic = {}
for i in range(0,len(sweden)-1):
    pair_dic['pair'] = sweden[i]['date']+'-'+sweden[i+1]['date']
    pair_dic['growth'] = int(sweden[i]['value']) - int(sweden[i+1]['value'])
    print(pair_dic)
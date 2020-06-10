import sys
import json

def fetch_key(dict1, key1):
    key_list = key1.split('/')
#    print(key_list)
    dict = json.loads(dict1)
    fetch_dict = dict
    for i in key_list:
        fetch_dict = fetch_dict.get(i)
    return fetch_dict
#key_list = sys.argv[2].split('/')
#print(key_list)
#print(fetch_key({"a":{"b":{"c":"d"}}},['a', 'b', 'c']))
print(fetch_key(sys.argv[1], sys.argv[2]))

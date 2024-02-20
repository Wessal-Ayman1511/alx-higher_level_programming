#!/usr/bin/python3
"""file moduel """


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    data_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    data_list = []

for i in range(1, len(sys.argv)):
    data_list.append(sys.argv[i])
save_to_json_file(data_list, "add_item.json")

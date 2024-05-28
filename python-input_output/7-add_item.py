#!/usr/bin/python3
"""import os module
   import sys module
"""
import os
import sys

"""import of load from json function """
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""import of save to json function """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, "add_item.json")

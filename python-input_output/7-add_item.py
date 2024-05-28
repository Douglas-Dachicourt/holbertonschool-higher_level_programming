#!/usr/bin/python3
"""import json module
   import sys module
"""
import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, "add_item.json")

print(items)

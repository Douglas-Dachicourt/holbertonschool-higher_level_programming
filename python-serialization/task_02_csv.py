#!/usr/bin/python3
"""import csv and json modules"""
import csv
import json
import os


def convert_csv_to_json(csv_file):
    """
    Function : convert_csv_to_json
    This function is converting a csv file into a json file

    Parameter:

    - csv_file : the csv file to convert

    Returns:
    => True if conversion is done.
    => False if file is not found

    """
    data = []
    try:
        if os.path.exists(csv_file):
            with open(csv_file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for rows in reader:
                    data.append(rows)
            return True
    except FileNotFoundError:
        return False

    with open("data.json", "w", encoding="utf-8") as f:
        try:
            json.dump(data, f, indent=0)
        except FileNotFoundError:
            return False

#!/usr/bin/python3
"""create"""
import json


def save_to_json_file(my_obj, filename):
    """json object"""

    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
    json_file.close()

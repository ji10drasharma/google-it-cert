#!/usr/bin/env python3

import json

try:
    with open('people.json', 'r') as people_json:
        people = json.load(people_json)
        print(people)
except FileNotFoundError:
    print("File not found.")

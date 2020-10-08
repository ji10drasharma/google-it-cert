#!/usr/bin/env python3

import json
import yaml


people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]


def to_json(var):
    try:
        with open('people.json', 'w') as people_json:
            json.dump(people, people_json, indent=2)
    except NameError:
        print("No object defined or initiliazed.")


def to_yaml(var):
    try:
        with open('people.yaml', 'w') as people_yaml:
            yaml.safe_dump(people, people_yaml)
    except NameError:
        print("No object defined or initialiazed")


to_json(people)

# Stores json object ratther writing to a file
people_json = json.dumps(people)
print(people_json)

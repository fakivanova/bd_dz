import random 
import json

BASE_FILENAME = 'supplies/diseases_short.json'
with open(BASE_FILENAME) as file:
	specialists = sorted({specialist for specialists in json.load(file).values() for specialist in specialists})

def specialist():
    return random.choice(specialists)

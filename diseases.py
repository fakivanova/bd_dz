import random 
import json

BASE_FILENAME = 'supplies/diseases_short.json'
with open(BASE_FILENAME) as file:
	diseases = sorted(json.load(file).keys())

def diseas():
    return random.choice(diseases)

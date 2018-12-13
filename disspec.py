import random 
import json

BASE_FILENAME = 'supplies/diseases_short.json'
with open(BASE_FILENAME) as file:
	diseases_specialties = json.load(file)

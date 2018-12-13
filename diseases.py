import random 
import json
import disspec

diseases = sorted(disspec.diseases_specialties.keys())

def diseas():
    return random.choice(diseases)

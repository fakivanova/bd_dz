import random 
import json
import disspec

specialties = sorted({
    speciality 
    for specialties in disspec.diseases_specialties.values()
    for speciality in specialties
})

def specialist():
    return random.choice(specialties)

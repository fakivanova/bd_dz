import random

BASE_FILENAME = 'supplies/medicalequipment_list'
equipment_list = sorted({line.strip() for line in open(BASE_FILENAME)})      

def equipment():
    return random.choice(equipment_list)

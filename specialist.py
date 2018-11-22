import random 

BASE_FILENAME = 'supplies/specialist_list'
specialists = sorted({line.strip() for line in open(BASE_FILENAME)})      

def specialist():
    return random.choice(specialists)

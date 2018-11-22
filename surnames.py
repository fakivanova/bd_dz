BASE_FILENAME = 'supplies/surname_list'
male_surnames = sorted({line.strip() for line in open(BASE_FILENAME)})      

def get_male_surnames():
    return list(male_surnames)

def get_female_surnames():
    return sorted({name + 'а' for name in male_surnames})

names = {
    'male': get_male_surnames(),
    'female': get_female_surnames()
}

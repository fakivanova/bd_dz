import json 
import itertools

BASE_FILENAME = 'supplies/firstnames.json'
NUMBER_OF_NAMES = 300

def get_names(number_of_names):
    with open(BASE_FILENAME) as jsondb:
        all_names = json.load(jsondb)

    all_names.sort(key=lambda entry: entry['PeoplesCount'], reverse=True)
    female_filter = filter(lambda entry: entry['Sex'] == 'Ж', all_names)
    female_names = [next(female_filter)['Name'] for _ in range(number_of_names)]

    male_filter = filter(lambda entry:  entry['Sex'] == 'М', all_names)
    male_names = [next(male_filter)['Name'] for _ in range(number_of_names)]

    return {
            'female': female_names,
            'male': male_names
        }
        
names = get_names(NUMBER_OF_NAMES)

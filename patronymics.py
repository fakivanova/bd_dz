BASE_FILENAME = 'supplies/patronymic_list'
male_patronymics = sorted({line.strip() for line in open(BASE_FILENAME)})      

def get_male_patronymics():
    return list(male_patronymics)

female_suffix_map = [
    ('вич', 'вна'), 
    ('ич', 'ичьевна'), 
    ('ыч', 'овна')
]
def get_female_patronymics():
    def substitute_suffix(name, suffix_map):
        for suffix, substitute in suffix_map:
            if name.endswith(suffix):
                return name[:-len(suffix)] + substitute
        raise RuntimeError('Unknow suffix in word: ' + name)
    return sorted({substitute_suffix(name, female_suffix_map) for name in male_patronymics})

names = {
    'male': get_male_patronymics(),
    'female': get_female_patronymics()
}

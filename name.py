import firstnames
import surnames
import patronymics
import random

def name(sex):
    return (random.choice(surnames.names[sex]),
            random.choice(firstnames.names[sex]),
            random.choice(patronymics.names[sex]))
    

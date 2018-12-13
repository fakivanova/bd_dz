import sqlite3
import diseases
import specialties
import disspec

def init(name):
    if name != ':memory:' and not name.endswith('.db'):
        name += '.db'
    connection = sqlite3.connect(name)
    __init_diseases_specialties(connection)
    connection.executescript('''
        PRAGMA foreign_keys = ON;

        CREATE TABLE hospitals(
            Id INTEGER PRIMARY KEY,
            Name TEXT);


        CREATE TABLE doctors(
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            HospitalId INTEGER,
            FOREIGN KEY(HospitalId) REFERENCES hospitals(Id));

    ''')

    connection.commit()
    return connection

def __init_diseases_specialties(connection):
    __init_diseases(connection)
    __init_specialties(connection)
    # add interconnection between diseases and specialties
    connection.executescript('''
        DROP TABLE IF EXISTS disspec;
        CREATE TABLE disspec(
            DiseasId INTEGER KEY,
            SpecialtyId INTEGER KEY
        )
    ''');
    for diseas, specialties in disspec.diseases_specialties.items():
        connection.executemany('INSERT INTO disspec(DiseasId, SpecialtyId) VALUES (?,?)',
                                1,
                                1)

def __init_diseases(connection):
    connection.executescript('''
        DROP TABLE IF EXISTS diseases;
        CREATE TABLE diseases(
            Id INTEGER PRIMARY KEY,
            Name TEXT)
    ''');
    connection.executemany('INSERT INTO diseases(Name) VALUES (?)', 
                           ((diseas,) for diseas in diseases.diseases))
def __init_specialties(connection):
    connection.executescript('''
        DROP TABLE IF EXISTS specialties;
        CREATE TABLE specialties(
            Id INTEGER PRIMARY KEY,
            Name TEXT)
    ''');
    connection.executemany('INSERT INTO specialties(Name) VALUES (?)', 
                           ((specialty,) for specialty in specialties.specialties))


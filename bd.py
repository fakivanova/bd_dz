import sqlite3

def init(name):
    if not name.endswith('.db'):
        name += '.db'
    sqlite.connect(name)






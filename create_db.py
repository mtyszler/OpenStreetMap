import sqlite3
from sqlite3 import OperationalError

import pandas

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            c.execute(command)
        except OperationalError, msg:
            print "Command skipped: ", msg


# Create a new empty db
db = sqlite3.connect("OpenStreeMap_Nieuwegein.sqlite")
c = db.cursor()

# Create all tables
executeScriptsFromFile("data_wrangling_schema.sql")
db.commit()

# import data
data_source = ['nodes', 'nodes_tags', 'ways', 'ways_tags', 'ways_nodes']
for part in data_source:
    print "Importing " + part
    df = pandas.read_csv(part + '.csv')
    df.to_sql(part, db, if_exists='append', index=False)



db.commit()
db.close()

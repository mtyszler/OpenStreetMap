## Description of files:

nieuwegein.osm.bz2: data downloaded via a custom extracts from mapzen
nieuwegein_sample.osm: sample file, with k = 10


create_sample.py: python scrtip to create a sample file
db_prep.py: python scrip to create csv files for the import. Based on course files and containing cleaning bits for the postcodes.
db_prep_schema.py: support file
create_db.py: python scrip to create the sqlite database, and clean the postcodes.

data_wrangling_schema.sql: schema for the creation of the database
support_file_for_post_codes_nodes.sql: sql query to clean postcodes
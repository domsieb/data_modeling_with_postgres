# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays ()
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users ()
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs ()
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists ()
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time ()
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays () VALUES ()
""")

user_table_insert = ("""
INSERT INTO users () VALUES ()
""")

song_table_insert = ("""
INSERT INTO songs () VALUES ()
""")

artist_table_insert = ("""
INSERT INTO artists () VALUES ()
""")


time_table_insert = ("""
INSERT INTO time () VALUES ()
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
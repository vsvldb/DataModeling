# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES
songplay_table_create = ("""
create table if not exists songplays(
songplay_id serial PRIMARY KEY
,start_time text
,user_id int
,level text
,song_id text
,artist_id text
,session_id text
,location text
,user_agent text);""")

user_table_create = ("""create table if not exists users(
user_id int PRIMARY KEY
,first_name text  NOT NULL
,last_name text  NOT NULL
,gender text
,level text);""")

song_table_create = ("""create table if not exists songs(
song_id text PRIMARY KEY
,title text  NOT NULL
,artist_id text  NOT NULL
,year int
,duration decimal);""")

artist_table_create = ("""create table if not exists artists(
artist_id text PRIMARY KEY
,name text  NOT NULL
,location text
,latitude float
,longitude float);""")

time_table_create = ("""create table if not exists time(
start_time timestamp PRIMARY KEY
,hour int
,day int
,week int 
,month int 
,year int
,weekday int);""")

# INSERT RECORDS
songplay_table_insert = ("""
insert into songplays
(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
)

user_table_insert = ("""
insert into users
(user_id,first_name,last_name,gender,level) 
VALUES(%s,%s,%s,%s,%s)ON CONFLICT (user_id) DO NOTHING;"""
)

song_table_insert = ("""
insert into songs
(song_id,title,artist_id,year,duration) 
VALUES(%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""
insert into artists
(artist_id,name,location,latitude,longitude)
VALUES(%s,%s,%s,%s,%s)ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""
insert into time
(start_time,hour,day,week,month,year,weekday) 
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS
song_select = (""" 
SELECT 
s.song_id
,s.artist_id 
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE 1=1
AND s.duration = %s
AND s.title = %s 
AND a.name = %s;
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


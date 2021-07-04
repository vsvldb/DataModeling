## Introduction
Sparkify is a Mobile App for Streaming music. This project aims to build a prototype of db that log all clients actions and stores it into DWH

## DWH structure

### Fact Table:
- songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
### Dimension tables:
- users (user_id,first_name,last_name, gender, level)
- artists (artist_id,name,location,latitude,longitude)
- songs (song_id,title,artist_id,year,duration)
- time (start_time,hour,day,week,month,year,weekday)


## Running of the project:
- Step 1: Create the Database and the tables Run the Following command in the terminal

python create_tables.py

- Step 2: Run the ETL pipeline to load the data from JSON to Postgres Database

python etl.py

After Step 1, you can view the ETL process in detail for extracting, transforming and loading one JSON file by using Restart and Run All Cells options in the etl.ipynb Jupyter Notebook Also, if you want to view the data in individual tables or test the Data Integrity of the songplays dataset, you can Restart and Run All Cells in the test.ipynb Jupyter Notebook

After using any of these notebooks, make sure to Restart Kernel so that the connection to the database is released.

# NOTE:

You will not be able to run test.ipynb, etl.ipynb, or etl.py until you have run create_tables.py at least once to create the sparkifydb database, which these other files connect to.

You can check out some of the Analytical queries and Data Integrity queries in the test.ipynb Jupyter Notebook

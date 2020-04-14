# DROP TABLES

drop_table = "DROP TABLE IF EXISTS "

songplay_table_drop = drop_table+"songplays"
user_table_drop = drop_table+"users"
song_table_drop = drop_table+"songs"
artist_table_drop = drop_table+"artists"
time_table_drop = drop_table+"time"

# CREATE TABLES

create_table = "CREATE TABLE IF NOT EXISTS"


###
###  I originally wanted to set song_id and artist_id to NOT NULL, however, they do have NULL values in the dataset
###

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL         PRIMARY KEY,
        start_time BIGINT NOT NULL REFERENCES time (start_time),
        user_id INT NOT NULL       REFERENCES users (user_id),
        level VARCHAR,
        song_id VARCHAR            REFERENCES songs (song_id),
        artist_id VARCHAR          REFERENCES artists (artist_id),
        session_id INT NOT NULL,
        location VARCHAR,
        user_agent VARCHAR
        
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender VARCHAR,
        level VARCHAR);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR,
        artist_id VARCHAR,
        year INT,
        duration NUMERIC);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY,
        name VARCHAR,
        location VARCHAR,
        latitude INT,
        longitude INT);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
        start_time BIGINT PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
        VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
        VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO UPDATE SET location =  EXCLUDED.location,
                  latitude =  EXCLUDED.latitude,
                  longitude = EXCLUDED.longitude;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT
        s.song_id, a.artist_id
    FROM
        songs s
    JOIN
        artists a
    ON
        s.artist_id = a.artist_id
    WHERE
        s.title = %s AND a.name = %s AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
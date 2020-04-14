# Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

I used the star schema, which is denormalized, so that we can have the benefits of 
    - Denormalized
    - Simplifies queries
    - Fast aggregations
    
The ETL pipeline first created 5 relevant tables, songplays (fact table), users, songs, artists and time (dimension tables) 

# Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Instructions
    1. Restart all openned kernals to close all connections to the database
    2. Run create_tables.py to create your database and tables.
    3. Run etl.py to populate all tables from the song/log files
    4. Run test.ipynb to confirm your records were successfully inserted into each table. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
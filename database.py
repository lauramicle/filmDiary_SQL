import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT,
    release_timestamp REAL
)
"""
CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched(
    username TEXT,
    title TEXT
)
"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?,?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title=?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (username, title) VALUES (?,?);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE username = ?;"
#SET_MOVIE_WATCHED = "UPDATE movies SET watched=1 WHERE title=?;"
connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(username, title):
    with connection:
     #   connection.execute(DELETE_MOVIE,(title,))
        connection.execute(INSERT_WATCHED_MOVIE,(username, title))

def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()
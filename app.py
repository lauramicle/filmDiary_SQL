import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!!"


print(welcome)
database.create_tables()

def print_movies(heading,movies):
    print(f"{heading} movies: ")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    input("\n Press Enter to continue...\n")

def print_watched_movies(username,movies):
    print(f"{username}'s movies: ")
    for movie in movies:
        print(f"{movie[1]}")
    input("\n Press Enter to continue...\n")

while (user_input := input(menu)) != "6":

    if user_input == "1":
        title = input("Title:")
        date = input("Release date (dd/mm/year):")
        release_datetime = datetime.datetime.strptime(date,"%d/%m/%Y")
        release_timestamp = datetime.datetime.timestamp(release_datetime)
        database.add_movie(title, release_timestamp)

    elif user_input == "2":
        upcoming = True
        movies = database.get_movies(upcoming)
        print_movies("Upcoming",movies)

    elif user_input == "3":
        upcoming = False
        movies = database.get_movies(upcoming)
        print_movies("Current", movies)

    elif user_input == "4":
        title = input("Title:")
        username = input("User name:")
        database.watch_movie(username, title)

    elif user_input == "5":
        username = input("Username:")
        movies = database.get_watched_movies(username)
        print_watched_movies(username,movies)
    else:
        print("Invalid input, please try again!")
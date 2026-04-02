from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.themoviedb.org/3/movie/"
params = {
    "api_key": api_key
}

keep_going = True



def show_menu():
    print("\n---Movie Data Available---\n1. Now Playing\n2. Popular\n3. Top Rated\n4. Upcoming")
    value = int(input("\nPlease make a selection\n"))
    if (value ==1):
        route_value = "now_playing"
    elif (value == 2):
        route_value = "popular"
    elif (value == 3):
        route_value = "top_rated"
    elif (value == 4):
        route_value = "upcoming"
    elif (value == 5):
        keep_going = False
        print("Stopping")
    else:
        print("Womp womp")
    return route_value


def build_route(endpoint):

    picked_route = url + endpoint

    return picked_route

def process_data(picked_route):
    response = requests.get(picked_route, params)
    movies = response.json()
    my_movies = []

    for movie in movies["results"]:
        movie_title = movie["title"]
        my_movies.append(movie_title)

    return my_movies

def send_data(my_movies):
    for movie in my_movies:
        print(movie)


while (keep_going == True):

    endpoint = show_menu()
    complete_url = build_route(endpoint)
    my_movies = process_data(complete_url)
    send_data(my_movies)


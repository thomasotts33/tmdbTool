from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.themoviedb.org/3/movie/"
params = {"api_key": api_key}


def show_menu():
    print("\n---Movie Data Available---\n--------------------------\n1. Now Playing\n2. Popular\n3. Top Rated\n4. Upcoming\n5. Stop Script\n--------------------------\n")
    value = input("Please make a selection\n")
    if (value =="1"):
        route_value = "now_playing"
    elif (value == "2"):
        route_value = "popular"
    elif (value == "3"):
        route_value = "top_rated"
    elif (value == "4"):
        route_value = "upcoming"
    elif (value == "5"):
        route_value = None
        print("Stopping")
    else:
        print("Invalid input... make a selection 1 - 5")
        route_value = "invalid"
    return route_value


def build_route(endpoint):
    
    picked_route = url + endpoint

    return picked_route

def process_data(picked_route):
    try:

        response = requests.get(picked_route, params)
        movies = response.json()
        my_movies = []

        for movie in movies["results"]:
            movie_title = movie["title"]
            my_movies.append(movie_title)

        return my_movies
    except:
        return None

def send_data(my_movies):
    print("\n---Results---\n--------------------------\n")
    for index, movie in enumerate(my_movies, start=1):
        print(f"{index}. {movie}")
    print("\n--------------------------\n")
    

while True:
    endpoint = show_menu()

    if (endpoint is None):
            break 
    if (endpoint == "invalid"):
            continue 

    complete_url = build_route(endpoint)
    my_movies = process_data(complete_url)

    if (my_movies == None):
        print("No data due to failed request...\n\nCheck API key and API Endpoints")
    else:

        send_data(my_movies)


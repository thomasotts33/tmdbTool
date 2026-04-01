from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.themoviedb.org/3/movie/"
params = {
    "api_key": api_key
}

keepGoing = True



def show_Menu():
    print("\n---Movie Data Available---\n1. Now Playing\n2. Popular\n3. Top Rated\n4. Upcoming")
    value = int(input("\nPlease make a selection\n"))
    if (value ==1):
        routeValue = "now_playing"
    elif (value == 2):
        routeValue = "popular"
    elif (value == 3):
        routeValue = "top_rated"
    elif (value == 4):
        routeValue = "upcoming"
    elif (value == 5):
        keepGoing = False
        print("Stopping")
    else:
        print("Womp womp")
    return routeValue


def Route(endPoint):

    picked_route = url + endPoint

    return picked_route

def process_Data(picked_route):
    response = requests.get(picked_route, params)
    movies = response.json()
    myMovies = []

    for movie in movies["results"]:
        movieTitle = movie["title"]
        myMovies.append(movieTitle)

    return myMovies

def send_Data(myMovies):
    for movie in myMovies:
        print(movie)


while (keepGoing == True):

    endPoint = show_Menu()
    complete_url = Route(endPoint)
    myMovies = process_Data(complete_url)
    send_Data(myMovies)


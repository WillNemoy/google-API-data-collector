import os
from dotenv import load_dotenv
from pprint import pprint
import json
import requests

import pandas as pd
import numpy as np

load_dotenv() #look in the ".env" file for env vars

def googleAPI_places(GOOGLE_API_KEY_parameter, search_term): #, location_parameter):

    # Python program to get a set of 
    # places according to your search 
    # query using Google Places API
    
    # https://developers.google.com/maps/documentation/places/web-service/search-text    
    response = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" 
                            + search_term 
                            + '&key=' 
                            + GOOGLE_API_KEY_parameter
                            + '&key=')
    
    data = response.json()

    return data

# https://developers.google.com/maps/documentation/places/web-service/place-data-fields#places-api-fields-support
def googleAPI_reviews(GOOGLE_API_KEY_parameter, place_id_parameter):

    response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=" 
                            + place_id_parameter 
                            + '&key=' 
                            + GOOGLE_API_KEY_parameter)
    data = response.json()

    return data
        
    

#run the function


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

my_place_id = "ChIJRfH9lXW7woARDUjiE-YILn8"

my_reviews_data = googleAPI_reviews(GOOGLE_API_KEY, my_place_id)

pprint(my_reviews_data)


"""
user_search_term = input("What type of businesses are you interested in? ")
user_location = input("What area should we focus on? ")

user_input = user_search_term + " " + user_location

my_data = googleAPI_places(GOOGLE_API_KEY, user_input)

pprint(my_data)
"""
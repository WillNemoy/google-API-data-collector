import os
from dotenv import load_dotenv
from pprint import pprint
import json
import requests

import pandas as pd
import numpy as np

from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS


def googleAPI(GOOGLE_API_KEY_parameter, search_term): #, location_parameter):

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
    all_reviews = []

    for place in places_data:
        place_review_data = 
        response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=" 
                            + place_id_parameter 
                            + '&key=' 
                            + GOOGLE_API_KEY_parameter)
        all_reviews.append(response.json())

    return data

# https://developers.google.com/maps/documentation/places/web-service/place-data-fields#places-api-fields-support

        

#run the function
load_dotenv() #look in the ".env" file for env vars


user_search_term = input("What type of businesses are you interested in? ")
user_location = input("What area should we focus on? ")

user_input = user_search_term + " " + user_location

my_data = googleAPI(GOOGLE_API_KEY, user_input)

pprint(my_data)

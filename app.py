import os
from dotenv import load_dotenv
from pprint import pprint
import json
import requests

import pandas as pd
import numpy as np

from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS

#steps:
#1) Fix the unicode error
#2) Bring in the Yelp API code. Bring this API up to speed.
#3) Paginate through all pages

def googleAPI(GOOGLE_API_KEY_parameter, search_term): #, location_parameter):

    # Python program to get a set of 
    # places according to your search 
    # query using Google Places API
    
    # https://developers.google.com/maps/documentation/places/web-service/search-text  
    # https://developers.google.com/maps/documentation/places/web-service/place-data-fields#places-api-fields-support
  
    response = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" 
                            + search_term 
                            + '&key=' 
                            + GOOGLE_API_KEY_parameter
                            + '&key=')
    
    data = response.json()

    place_data = data["results"]
    all_reviews = []

    
    for place in place_data:
        response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=" 
                            + place["place_id"] 
                            + '&key=' 
                            + GOOGLE_API_KEY_parameter)
        all_reviews.append(response.json())
    
    print(response.encoding)
    return all_reviews


        

#run the function
load_dotenv() #look in the ".env" file for env vars

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


user_search_term = input("What type of businesses are you interested in? ")
user_location = input("What area should we focus on? ")

user_input = user_search_term + " " + user_location

my_data = googleAPI(GOOGLE_API_KEY, user_input)

pprint(my_data)

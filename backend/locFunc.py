from pprint import pprint
import googlemaps # pip install googlemaps
from queue import PriorityQueue
import member
import locManager
import requests
import json
import urllib

SHELTERS = PriorityQueue
API_KEY = 'AIzaSyDuu7nGNYVBhoLQFNa1_qZ7O2CHs0ON94E'

user_addr = locManager.my_loc
map_client = googlemaps.Client(API_KEY)
wp_address = '6100 Main St, Houston, TX'
response = map_client.geocode(wp_address)
# pprint(response)

def str_to_loc(addr):
    my_rps = map_client.geocode(addr)
    lat = my_rps[0].get("geometry").get("location").get("lat")
    lng = my_rps[0].get("geometry").get("location").get("lng")
    return (lat, lng)

# Initialize shelter database
shelter_file = open("./shelters.txt", 'r')
shltr_addr = shelter_file.readline()
while(shltr_addr != ''):
    SHELTERS.append(str_to_loc(shltr_addr))
    shltr_addr = shelter_file.readline()

# addr - a string of the address
def get_location(addr):
    return str_to_loc(addr)

def get_nrst_shelter():
    return None


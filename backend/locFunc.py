from pprint import pprint
import flask
import googlemaps # pip install googlemaps
from queue import PriorityQueue
from flask import Flask
import pandas as pds
import member
import math
import locManager
import requests
import json
import urllib

SHELTERS = PriorityQueue
API_KEY = 'AIzaSyDuu7nGNYVBhoLQFNa1_qZ7O2CHs0ON94E'

app = Flask(__name__)

# @app.route('../Hurricane\ SOS/Login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if flask.request.method == 'POST':
#         return (flask.request.form['username'])
#     # # the code below is executed if the request method
#     # # was GET or the credentials were invalid
#     # return render_template('login.html', error=error)

u_loc = None

def str_for_pin(addr):
    newaddr = addr.replace(" ","+")
    return newaddr

def str_to_loc(addr):
    my_rps = map_client.geocode(addr)
    lat = my_rps[0].get("geometry").get("location").get("lat")
    lng = my_rps[0].get("geometry").get("location").get("lng")
    return (lat, lng)

## Helper
def get_distance(addr1, addr2):
    return math.dist(addr1, addr2)

def get_nrst_k_shelter(k):
    # Initialize shelter database
    shelter_file = open("./shelters.txt", 'r')
    shltr_addr = shelter_file.readline()
    nrst_k = []
    while(shltr_addr != ''):
        shltr_data = str_to_loc(shltr_addr)
        shltr_pin_addr = str_for_pin(shltr_addr)
        SHELTERS.append(get_distance(str_to_loc(u_loc), shltr_data), shltr_data, shltr_pin_addr)
        shltr_addr = shelter_file.readline()
    for i in range(k):
        nrst_k.append(SHELTERS.queue[i][1])
    return nrst_k


if __name__ == '__main__':
    # user_addr = locManager.my_loc
    map_client = googlemaps.Client(API_KEY)
    wp_address = '6100 Main St'
    response = map_client.geocode(wp_address)
    pprint(str_to_loc(response))

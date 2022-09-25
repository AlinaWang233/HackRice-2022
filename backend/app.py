from pprint import pprint
import flask
import googlemaps # pip install googlemaps
from queue import PriorityQueue
from flask import Flask, url_for, request, render_template
import pandas as pds
import locManager
import requests
import json
import urllib
import locFunc
import json

app = Flask(__name__)

my_fname = None 
my_lname = None
my_loc = None 
my_phone = None


@app.route('/')
def main():
    return render_template('home.html') 

@app.route('/home/login', methods = ['POST', 'GET'])
def login():
    global my_fname, my_lname, my_loc,my_phone
    if request.method == 'POST':

        my_fname = request.form.get('fname')
        my_lname = request.form.get('lname')
        my_loc = request.form.get('loc')
        my_phone = request.form.get('phone')

        locFunc.u_loc = my_loc
        
        # process information
        if my_phone in locManager.phone_numbers:
            pass
        else:
            locManager.first_names.append(my_fname)
            locManager.last_names.append(my_lname)
            locManager.locations.append(my_loc)
            locManager.phone_numbers.append(my_phone)

            # Calculate the nearest 10 shelters 
            # And return a list of shelter (lat, lng) tuple
            # Send as a parameter to home_update
            my_loc_data = locFunc.str_to_loc(my_loc)
            shelters = locFunc.get_nrst_k_shelter(10)
            
        return render_template('home_update.html', my_loc_data, shelters) 
    elif request.method == 'GET':
        return render_template('home.html') 
    
@app.route('/home/login/success', methods = ['POST', 'GET'])
def generate_twitter():
    return "Hello World"

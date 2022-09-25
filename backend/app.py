from pprint import pprint
import flask
import googlemaps # pip install googlemaps
from queue import PriorityQueue
from flask import Flask, url_for, request, render_template
import pandas as pds
import member
import locManager
import requests
import json
import urllib
import locFunc

app = Flask(__name__)

u_fname = None 
u_lname = None
u_loc = None 
u_phone = None


@app.route('/')
def main():
    return render_template('home.html') 

@app.route('/home/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':

        u_fname = request.form.get('fname')
        u_lname = request.form.get('lname')
        u_loc = request.form.get('loc')
        u_phone = request.form.get('phone')

        locFunc.u_loc = u_loc
        
        # process information
        if u_phone in locManager.phone_numbers:
            pass
        else:
            locManager.first_names.append(u_fname)
            locManager.last_names.append(u_lname)
            locManager.locations.append(u_loc)
            locManager.phone_numbers.append(u_phone)

            # Calculate the nearest 10 shelters 
            # And return a list of shelter (lat, lng) tuple
            # Send as a parameter to home_update
            shelters = locFunc.get_nrst_k_shelter(10)
            
        return render_template('home_update.html', shelters) 
    elif request.method == 'GET':
        return render_template('home.html') 
    
@app.route('/home/login/success', methods = ['POST', 'GET'])
def generate_twitter():
    
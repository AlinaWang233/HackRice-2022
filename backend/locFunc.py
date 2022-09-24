from pprint import pprint
import googlemaps # pip install googlemaps

SHELTERS = []
API_KEY = 'AIzaSyDuu7nGNYVBhoLQFNa1_qZ7O2CHs0ON94E'

map_client = googlemaps.Client(API_KEY)
wp_address = '6100 Main St, Houston, TX'
response = map_client.geocode(wp_address)
pprint(response)

# Initialize shelter database
shelter_file = open("./shelters.txt", 'r')
shelter_address = shelter_file.readline()
while(shelter_address != ''):
    SHELTERS.append(shelter_address)



def get_location():
    return None

def get_nrst_shelter():
    return None



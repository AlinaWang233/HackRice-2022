import googlemaps # pip install googlemaps
import locFunc
import member
'''
The manager for user's registered location
Have a queue for rescurers and a queue for survivors
'''
#user is a member
user = None
my_name = user.name
my_loc = locFunc.get_location(user.addr)



#a importing googlemaps module
import googlemaps
  
# Requires API key
gmaps = googlemaps.Client(key='AIzaSyDOVK-17iqBopzoBlkoWOzClQmRz5B7TqE')
  
start = 'renton'
dest ='issaquah'

# Requires cities name
my_dist = gmaps.distance_matrix(start,dest)['rows'][0]['elements'][0]
  
# Printing the result
print(my_dist)
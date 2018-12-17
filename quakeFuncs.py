from urllib.request import *
from json import *
from datetime import *
from operator import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
# Add Earthquake class definition here   
class Earthquake():
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = str(place)
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = int(time)
   def __str__(self):
      return ("(%.2f) %40s at %s (%8.3f, %.3f)" % (self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude))
   def __repr__(self):
      return ("%s %s %s %s %s\n" % (str(self.mag), str(self.longitude), str(self.latitude), str(self.time), self.place))
   def __eq__(self, other):
      eq_place = self.place == other.place
      eq_mag = self.mag == other.mag
      eq_longitude = self.longitude == other.longitude
      eq_latitude = self.latitude == other.latitude
      eq_time = self.time == other.time
      return eq_place and eq_mag and eq_longitude and eq_latitude and eq_time
# Required function - implement me!   
def read_quakes_from_file(filename):
   list_quakes = []
   with open(filename, 'r') as inFile:
      for i in inFile:
         i = i.split()
         mag = float(i[0])
         long_ = float(i[1])
         lat = float(i[2])
         time = int(i[3])
         place = ' '.join(i[4:]) 
         list_quakes.append(Earthquake(place, mag, long_, lat, time))
   return list_quakes
def sort_quakes(quakes, sort):
       if sort == "m":
          quakes.sort(key=attrgetter('mag'), reverse = True)
       elif sort == "t":
          quakes.sort(key=attrgetter('time'), reverse = True)
       elif sort == "l":
          quakes.sort(key=attrgetter('longitude'))
       elif sort == "a":
          quakes.sort(key=attrgetter('latitude'))
# Required function - implement me!
def filter_by_mag(quakes, low, high):
   filter_mag = []
   for q in quakes:
      if low <= q.mag <= high:
         filter_mag.append(q)       
   return filter_mag  
# Required function - implement me!
def filter_by_place(quakes, word):   
   filter_place = []
   for q in quakes:
       if word.lower() in q.place.lower():
          filter_place.append(q)
   return filter_place
# Required function for final part - implement me too!   
def quake_from_feature(feature):
   place = feature["properties"]["place"]
   mag = feature["properties"]["mag"]
   time = (feature["properties"]["time"]) / 1000
   long_ = feature["geometry"]["coordinates"][0]
   lat = feature["geometry"]["coordinates"][1]
   new = (Earthquake(place, mag, long_, lat, time))
   if new not in read_quakes_from_file("quakes.txt"): 
      return new
def display_quakes(list_quakes):
   print('Earthquakes:')
   print('------------')
   for i in list_quakes:
      print(i)
   print("\nOptions:")
   print("    (s)ort")
   print("    (f)ilter")
   print("    (n)ew quakes")
   print("    (q)uit")
   blank = ""
   return blank

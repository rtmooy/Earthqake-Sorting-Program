from quakeFuncs import *

list_quakes = read_quakes_from_file("quakes.txt")
print(display_quakes(list_quakes))
complete = True
while complete == True:
   choice = input("Choice: ")
   if choice == "f" or choice == "F":
      filtertype = input("Filter by (m)agnitude or (p)lace? ")
      if filtertype == "p" or filtertype == "P":
          string = input("Search for what string? ")
          print("")
          filter_place = filter_by_place(list_quakes, string)
          print(display_quakes(filter_place))
      elif filtertype == "m" or filtertype == "M":
          low = float(input("Lower bound: "))
          high = float(input("Upper bound: "))
          print("")
          filter_mag = filter_by_mag(list_quakes, low, high)
          print(display_quakes(filter_mag))
   elif choice == "n" or choice == "N":
      json = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
      features = json["features"]
      for feature in features:
          new = quake_from_feature(feature)
          list_quakes.append(new)
      print("\nNew quakes found!!! ")
      print("")
      print(display_quakes(list_quakes))
      with open("quakes.txt", "a") as inFile:
          for q in list_quakes:
              inFile.write(repr(q))
   elif choice == "s" or choice == "S":
      sorttype = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
      print("")
      if sorttype == "m" or sorttype == "M":
         sort = sort_quakes(list_quakes, "m")
         print(display_quakes(list_quakes))
      elif sorttype == "t" or sorttype == "T":
         sort = sort_quakes(list_quakes, "t")
         print(display_quakes(list_quakes))
      elif sorttype == "l" or sorttype == "L":
         sort = sort_quakes(list_quakes, "l")
         print(display_quakes(list_quakes))
      elif sorttype == "a" or sorttype == "A":
         sort = sort_quakes(list_quakes, "a")
         print(display_quakes(list_quakes))
   elif choice == "q" or choice == "Q":
      complete = False
      with open("quakes.txt", "w") as inFile:
          for q in list_quakes:
              inFile.write(repr(q))
      break

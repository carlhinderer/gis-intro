import turtle as t

# Constants
NAME = 0
POINTS = 1
POP = 2

# Each state has name, polygon points, and population
state = ["COLORADO", [[-109, 37],[-109, 41],[-102, 41],[-102, 37]], 5187582]

# Each city has name, polygon points, and population
cities = []
cities.append(["DENVER",[-104.98, 39.74], 634265])
cities.append(["BOULDER",[-105.27, 40.02], 98889])
cities.append(["DURANGO",[-107.88,37.28], 17069])

# Define the map size
MAP_WIDTH = 400
MAP_HEIGHT = 300

# Scale the map to the graphics canvas by
#   1. Determine the bounding box
#   2. Calculate the ratio between the actual state and the canvas we will render it on
#   3. Transform each point from map coordinates into pixel coordinates


    


if __name__ == '__main__':
    simple = SimpleGIS()
    print('Hey there')
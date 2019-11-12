"""SimpleGIS.py - A Simple GIS"""

import turtle as t

# DATA MODEL
# All layers will have a name, 1+ points, and population count
NAME = 0
POINTS = 1
POP = 2

# Create the state layer
STATE = ["COLORADO", [[-109, 37], [-109, 41], [-102, 41], [-102, 37]], 5187582]

# city = [name, [point], population]
CITIES = []

# Map Graphics Rendering
MAP_WIDTH = 800
MAP_HEIGHT = 500

# State Bounding Box
MINX = 180
MAXX = -180
MINY = 90
MAXY = -90

# Earth Distances
DIST_X = 260
DIST_Y = 180

# Scaling Ratios
X_RATIO = 3
Y_RATIO = 2

def populate_cities():
    CITIES.append(["DENVER", [-104.98, 39.74], 634265])
    CITIES.append(["BOULDER", [-105.27, 40.02], 98889])
    CITIES.append(["DURANGO", [-107.88, 37.28], 17069])

def get_bounding_box():
    global MINX, MAXX, MINY, MAXY
    for x, y in STATE[POINTS]:
        if x < MINX:
            MINX = x
        elif x > MAXX:
            MAXX = x
        if y < MINY:
            MINY = y
        elif y > MAXY:
            MAXY = y

# Get earth distance on each axis
def get_earth_distance():
    global DIST_X, DIST_Y
    DIST_X = MAXX - MINX
    DIST_Y = MAXY - MINY

# Scaling ratio each axis
# to map points from world to screen
def get_scaling_ratio():
    global X_RATIO, Y_RATIO
    X_RATIO = MAP_WIDTH / DIST_X
    Y_RATIO = MAP_HEIGHT / DIST_Y

def convert(point):
    """Convert lat/lon to screen coordinates"""
    lon = point[0]
    lat = point[1]
    x = MAP_WIDTH - ((MAXX - lon) * X_RATIO)
    y = MAP_HEIGHT - ((MAXY - lat) * Y_RATIO)

    # Python turtle graphics start in the middle of the screen
    # so we must offset the points so they are centered
    x = x - (MAP_WIDTH/2)
    y = y - (MAP_HEIGHT/2)

    return [x, y]

def setup_data_model():
    populate_cities()
    get_bounding_box()
    get_earth_distance()
    get_scaling_ratio()

# Add a title to the window
def add_title():
    wn = t.Screen()
    wn.title("Simple GIS")

# Draw the state
def draw_state():
    t.up()
    first_pixel = None

    for point in STATE[POINTS]:
        pixel = convert(point)
        if not first_pixel:
            first_pixel = pixel
        t.goto(pixel)
        t.down()

    # Go back to the first point
    t.goto(first_pixel)

    # Label the state
    t.up()
    t.goto([0, 0])
    t.write(STATE[NAME], align="center", font=("Arial", 16, "bold"))

# Draw the cities
def draw_cities():
    for city in CITIES:
        pixel = convert(city[POINTS])
        t.up()
        t.goto(pixel)
        # Place a point for the city
        t.dot(10)
        # Label the city
        t.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")
        t.up()

# Perform an attribute query
# Question: Which city has the largest population?
# Write the result but make sure it's under the map
def show_biggest_city():
    biggest_city = max(CITIES, key=lambda city: city[POP])
    t.goto(0, -1*((MAP_HEIGHT/2)+20))
    t.write("The highest-populated city is: " + biggest_city[NAME])

# Perform a spatial query
# Question: Which is the western most city?
# Write the result but make sure it's under the other question
def show_westernmost_city():
    western_city = min(CITIES, key=lambda city: city[POINTS])
    t.goto(0, -1*((MAP_HEIGHT/2)+40))
    t.write("The western-most city is: " + western_city[NAME])

# Hide our map pen
def hide_map_pen():
    t.pen(shown=False)
    t.done()

def render_map():
    add_title()
    draw_state()
    draw_cities()
    show_biggest_city()
    show_westernmost_city()
    hide_map_pen()


# Main Execution
setup_data_model()
render_map()
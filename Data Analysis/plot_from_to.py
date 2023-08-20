import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


import sqlite3

import math

def dist(lat1, long1, lat2, long2):
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Multiply arc by the radius of the earth in kilometers to get distance in km
    return arc * 6373.0

# Open database connection
db = sqlite3.connect('database.db')

# Get the ToAddresses from the telemetry table as a list
cursor = db.execute('SELECT FromAddress, ToAddress FROM Telemetry')

# Create an empty list
fromAddress = []
toAddress = []

for row in cursor:
    fromAddress.append(row[0])
    toAddress.append(row[1])

# Get the latitude and longitude of each address
cursor = db.execute('SELECT Address, Latitude, Longitude FROM Addresses')

# Create a dictionary to get the latitude and longitude from the address
address_dict = {}
for row in cursor:
    address_dict[row[0]] = (row[1], row[2])

# Plot each arrow on a map
fig = px.scatter_mapbox(lat=[i[0] for i in address_dict.values()],
                        lon=[i[1] for i in address_dict.values()],
                        zoom=9,
                        mapbox_style="stamen-terrain")

# Add all the lines at one time
# Convert all the arrows to scattermapbox traces
fig.add_traces(go.Scattermapbox(
    lat=[i[0] for i in address_dict.values()],
    lon=[i[1] for i in address_dict.values()],
    mode='lines',
    line=dict(width=1, color='red'),
    opacity=0.1
))

fig.show()

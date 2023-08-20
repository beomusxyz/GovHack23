import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


import sqlite3

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

service_center_coordinates = [
    (-26.65088996, 153.06063996),
    (-27.09259971, 152.96401811),
    (-27.09811215, 152.9701132),
    (-26.6568536, 153.09403343),
    (-26.656597255614404, 153.09404887116014),
    (-26.65862931, 153.09353741),
    (-26.658898075550404, 153.09361228255744),
    (-26.6560851, 153.09410832),
    (-26.65637578, 153.0948274),
    (-26.65643781, 153.09414208),
    (-26.65657642, 153.09410587),
    (-26.65691871, 153.09466019)
]

fig.add_trace(go.Scattermapbox(
    lat=[i[0] for i in service_center_coordinates],
    lon=[i[1] for i in service_center_coordinates],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=10,
        color='rgb(255, 0, 0)',
        opacity=0.7
    ),
    text=['Service Center 1', 'Service Center 2', 'Service Center 3', 'Service Center 4', 'Service Center 5',
            'Service Center 6', 'Service Center 7', 'Service Center 8', 'Service Center 9', 'Service Center 10',
            'Service Center 11', 'Service Center 12'],
    hoverinfo='text'
))

fig.show()
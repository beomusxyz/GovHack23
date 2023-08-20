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


# Draw arrows between each fromAddress and toAddress
arrows = []
for i in range(len(fromAddress)):
    if fromAddress[i].split(',')[0] in address_dict and toAddress[i].split(',')[0] in address_dict:
        from_lat_long = address_dict[fromAddress[i].split(',')[0]]
        to_lat_long = address_dict[toAddress[i].split(',')[0]]

        arrows.append(dict(
            x=[from_lat_long[1], to_lat_long[1]],
            y=[from_lat_long[0], to_lat_long[0]],
            mode='lines',
            line=dict(width=1, color='red'),
            opacity=0.5
        ))

# Plot each arrow on a map
fig = px.scatter_mapbox(lat=[i[0] for i in address_dict.values()],
                        lon=[i[1] for i in address_dict.values()],
                        zoom=10,
                        mapbox_style="stamen-terrain")

print(len(arrows))
for i, arrow in enumerate(arrows):
    if i > 1000:
        break
    fig.add_trace(go.Scattermapbox(
        lat=arrow['y'],
        lon=arrow['x'],
        mode='lines',
        line=dict(width=1, color='red'),
        opacity=0.5
    ))

fig.show()

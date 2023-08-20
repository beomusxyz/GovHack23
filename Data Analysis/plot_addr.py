import pandas as pd
import numpy as np
import plotly.express as px

import sqlite3

# Open database connection
db = sqlite3.connect('database.db')

# Get the ToAddresses from the telemetry table as a list
cursor = db.execute('SELECT ToAddress FROM Telemetry')

# Create an empty list
to_address = []

# Get the frequency of each address
for row in cursor:
    # Append the address to the list
    to_address.append(row[0])

# Get the latitude and longitude of each address
cursor = db.execute('SELECT Address, Latitude, Longitude FROM Addresses')

# Create a dictionary to get the latitude and longitude from the address
address_dict = {}
for row in cursor:
    address_dict[row[0]] = (row[1], row[2])

# Get the frequency of each latitude and longitude
lat_long_freq = {}
for address in to_address:
    if address.split(',')[0] in address_dict:
        lat_long = address_dict[address.split(',')[0]]
        if lat_long in lat_long_freq:
            lat_long_freq[lat_long] += 1
        else:
            lat_long_freq[lat_long] = 1

# print(lat_long_freq)

# Order the dictionary by frequency
lat_long_freq = dict(sorted(lat_long_freq.items(), key=lambda item: item[1], reverse=True))

# print(lat_long_freq)

# Plot a heatmap of the addresses with the frequency as the weight
df = pd.DataFrame(list(lat_long_freq.keys()), columns=['Latitude', 'Longitude'])
df['Frequency'] = list(lat_long_freq.values())
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Frequency', radius=10,
                        center=dict(lat=-26.924, lon=152.96), zoom=10,
                        mapbox_style="stamen-terrain")
fig.show()
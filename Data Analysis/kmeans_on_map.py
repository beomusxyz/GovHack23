import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans


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

# Find the optimal number of clusters
# Create a list of latitudes and longitudes
lat_long = []
for address in fromAddress:
    if address.split(',')[0] in address_dict:
        lat_long.append(address_dict[address.split(',')[0]])

# Convert the list to a numpy array
lat_long = np.array(lat_long)

# Calculate k-means
k = 5
kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10)
pred_y = kmeans.fit_predict(lat_long)

# Plot the clusters
fig = px.scatter_mapbox(lat=[i[0] for i in lat_long],
                        lon=[i[1] for i in lat_long],
                        zoom=9,
                        mapbox_style="stamen-terrain",
                        color=pred_y.astype(str),
                        color_discrete_map={
                            '0': 'red',
                            '1': 'blue',
                            '2': 'green',
                            '3': 'yellow',
                            '4': 'purple'
                        })

# Plot the centroids
fig.add_trace(go.Scattermapbox(
    lat=[i[0] for i in kmeans.cluster_centers_],
    lon=[i[1] for i in kmeans.cluster_centers_],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=10,
        color='rgb(0, 0, 0)',
        opacity=1
    ),
    text=['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'],
    hoverinfo='text'
))

fig.show()
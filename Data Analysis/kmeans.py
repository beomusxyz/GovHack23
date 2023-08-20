import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
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

# # Plot the latitudes and longitudes
# plt.scatter(lat_long[:, 1], lat_long[:, 0])
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Latitude and Longitude of Addresses')
# # make the axes equal so that the circles aren't ovals
# plt.axis('equal')
# plt.show()

max = 25
data = list(zip(lat_long[:, 1], lat_long[:, 0]))
inertias = []
for i in range(1, max):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# Plot the graph
# plt.plot(range(1, max), inertias)
# show all but the first
# plt.plot(range(2, max), inertias[1:])
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

# k = 6
# kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10)
# kmeans.fit(data)
# y_kmeans = kmeans.predict(data)

# # Plot the clusters
# plt.scatter(lat_long[:, 1], lat_long[:, 0], c=y_kmeans, s=15, cmap='viridis')
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=50, alpha=0.5, marker='x')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Latitude and Longitude of Addresses')
# # make the axes equal so that the circles aren't ovals
# plt.axis('equal')
# plt.show()

# Save an image with 1-10 clusters
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(data)
    y_kmeans = kmeans.predict(data)

    # Plot the clusters
    plt.scatter(lat_long[:, 1], lat_long[:, 0], c=y_kmeans, s=15, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=50, alpha=0.5, marker='x')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Latitude and Longitude of Addresses')
    # make the axes equal so that the circles aren't ovals
    plt.axis('equal')
    plt.savefig(f'images/cluster{i}.png')
    plt.clf()
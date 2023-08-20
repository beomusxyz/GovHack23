import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


import sqlite3

# Open database connection
db = sqlite3.connect('database.db')

# Get everything from the telemetry table
cursor = db.execute('SELECT * FROM Telemetry')

data = {}
# e.g.
# data = {
    # 'vehicleID': {
    #     'date1': 20, #km
    #     'date2': 30, #km
    # }
# }

for row in cursor:
    if row[1] not in data:
        data[row[1]] = {}
    
    date = row[3]
    if date not in data[row[1]]:
        data[row[1]][date] = 0

    data[row[1]][date] += row[6]

# print(data)

# Print each vehicle's average distance travelled per day
for vehicle in data:
    print(vehicle, ":", sum(data[vehicle].values())/len(data[vehicle].values()), "km")
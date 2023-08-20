import matplotlib.pyplot as plt
import sqlite3

# Open database connection
db = sqlite3.connect('database.db')

# Get the distance and idling duration from the telemetry table as a list
cursor = db.execute('SELECT Distance, IdlingDuration FROM telemetry')

# Create two empty lists
distance = []
idling_duration = []

# Iterate over the cursor and append the values to the lists
for row in cursor:
    distance.append(row[0])
    idling_duration.append(row[1])

# Close the database connection
db.close()

# Plot the distance and idling duration
plt.plot(distance, idling_duration, 'o')
plt.xlabel('Distance')
plt.ylabel('Idling Duration')
plt.show()
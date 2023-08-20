import sqlite3

# Open database connection
db = sqlite3.connect('database.db')
conn = db.cursor()

# Get all distances from telemetry table
conn.execute('SELECT Distance FROM Telemetry')

# Create an empty list
distance = []
for row in conn:
    # Append the distance to the list
    distance.append(row[0])

# Close the database connection
db.close()

print(sum(distance), "km")
print(sum(distance)/len(distance), "km")
print("$", sum(distance) * 0.85)
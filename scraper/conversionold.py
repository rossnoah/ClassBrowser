#convert the sqlite db data.db to a json file


import sqlite3
import json
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("SELECT * FROM classes")
rows = c.fetchall()
data = []
for row in rows:
    data.append(row)
conn.close()

#convert the data to a json file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


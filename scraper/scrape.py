#import soup
from bs4 import BeautifulSoup

#open the file /files/31.html

soup = BeautifulSoup(open('all.html'), 'lxml')

#find the 6th tbody element
tablebody = soup.find_all('tbody')[5]

rows=[]
data=[]
#add every tr element to a list from the tbody
for tr in tablebody.find_all('tr'):
    rows.append(tr)
    #add every td element to a list from the tr

for tr in rows:    
    temp=[]
    for td in tr.find_all('td'):
            #add the text of the td to the list

            
            temp.append(td.text)
            #check column span of td
            if(td.has_attr('colspan')):
                 #get the column span
                col_span = int(td['colspan'])
                #add the text to the list the number of times of the column span
                for i in range(1, col_span):
                     temp.append("Data not available")

        #add the list to the data list
    if(len(temp)==0):
         continue
    data.append(temp)
    #print(len(temp))





#loop through tbody elements
#id, subject, course, name, attributes

# print(data[0])
# print(data[99][1])
# print(data[3])
# print(data[len(data)-1])


useful_data = []
for index, d in enumerate(data):
    subject = d[2]
    course = d[3]
    section = d[4]
    name = d[7]
    id = d[1]
    location = d[21]
    if(location == '\xa0'):
        location = "TBA"

    values = "Values" in d[22]
    writing = "Writing" in d[22]
    social = "Social" in d[22]
    humanities = "Humanities" in d[22]
    multicultural1 = "Multicultural 1" in d[22]
    multicultural2 = "Multicultural 2" in d[22]
    language = "Second Lang" in d[22]
    naturalscience = "Natural Science" in d[22]
    quantitative = "Quantitative" in d[22]

    


    attributes = [values, writing, social, humanities, multicultural1, multicultural2, language, naturalscience, quantitative]

    useful_data.append([subject, course, section, name, id, location, values, writing, social, humanities, multicultural1, multicultural2, language, naturalscience, quantitative])

# print(useful_data[0])
# print(useful_data[len(useful_data)-1])

# for d in data:
#     print(len(d))

#print(data[len(data)-1])

#enumerate through the data
# for index, d in enumerate(data):
#     if(len(d)!=23):
#         print(d)
#         print(len(d))
#         print(data[index+1])

#save useful data to a csv file
import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["subject", "course", "section", "name", "id", "location", "values", "writing", "social", "humanities", "multicultural1", "multicultural2", "language", "naturalscience", "quantitative"])
    for d in useful_data:
        writer.writerow(d)


#save the data to a sqlite database
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE classes (subject text, course text, section text, name text, id text, location text, values_outcome text, writing text, social text, humanities text, multicultural1 text, multicultural2 text, language text, naturalscience text, quantitative text)''')
for d in useful_data:
    c.execute("REPLACE INTO classes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", d)
conn.commit()
conn.close()

#save the data to a json file
import json
with open('data.json', 'w') as outfile:
    json.dump(useful_data, outfile)
    
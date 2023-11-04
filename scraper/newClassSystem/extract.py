import json


def load_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


data = load_json("part1.json")
data2 = load_json("part2.json")

# print(len(data['data']))
# print(len(data2['data']))

# combine the two json files
data['data'].extend(data2['data'])

# print(len(data['data']))

# save this combined data to a new json file but only the data part
with open('combined.json', 'w') as outfile:
    json.dump(data['data'], outfile)


merged_data = load_json("combined.json")


# print(merged_data[0])


useful_data = []
for index, d in enumerate(merged_data):
    subject = d['subject']
    course = d['courseNumber']
    section = d['sequenceNumber']
    name = d['courseTitle']
    name = name.replace("&amp;", "&")
    id = d['courseReferenceNumber']

# [{'category': '01', 'class': 'net.hedtech.banner.student.schedule.SectionSessionDecorator', 'courseReferenceNumber': '30386', 'faculty': [], 'meetingTime': {'beginTime': '1315', 'building': 'VAN', 'buildingDescription': 'Van Wickle Hall', 'campus': '1', 'campusDescription': 'Main Campus', 'category': '01', 'class': 'net.hedtech.banner.general.overall.MeetingTimeDecorator', 'courseReferenceNumber': '30386', 'creditHourSession': 0.0, 'endDate': '05/13/2024', 'endTime': '1600', 'friday': False, 'hoursWeek': 2.75, 'meetingScheduleType': '2', 'meetingType': 'CLAS', 'meetingTypeDescription': 'Class', 'monday': False, 'room': '106', 'saturday': False, 'startDate': '01/22/2024', 'sunday': False, 'term': '202330', 'thursday': False, 'tuesday': True, 'wednesday': False}, 'term': '202330'}]

    location_data = d['meetingsFaculty']
    if (location_data == '\xa0'):
        location = "TBA"
    elif (location_data == []):
        location = "TBA"
    else:
        location = str(location_data[0]['meetingTime']['building']) + \
            " " + str(location_data[0]['meetingTime']['room'])

    values = False
    writing = False
    social = False
    humanities = False
    multicultural1 = False
    multicultural2 = False
    language = False
    naturalscience = False
    quantitative = False

    if (d['sectionAttributes'] != []):
        for attribute in d['sectionAttributes']:
            # print(attribute['code'])
            code = attribute['code']
            if (code == "V"):
                values = True
            elif (code == "WRIT"):
                writing = True
            elif (code == "SS"):
                social = True
            elif (code == "HUM"):
                humanities = True
            elif (code == "GM1"):
                multicultural1 = True
            elif (code == "GM2"):
                multicultural2 = True
            elif (code == "EPSL"):
                language = True
            elif (code == "NS"):
                naturalscience = True
            elif (code == "Q"):
                quantitative = True


#     values = "Values" in d[22]
#     writing = "Writing" in d[22]
#     social = "Social" in d[22]
#     humanities = "Humanities" in d[22]
#     multicultural1 = "Multicultural 1" in d[22]
#     multicultural2 = "Multicultural 2" in d[22]
#     language = "Second Lang" in d[22]
#     naturalscience = "Natural Science" in d[22]
#     quantitative = "Quantitative" in d[22]

#     attributes = [values, writing, social, humanities, multicultural1,
#                   multicultural2, language, naturalscience, quantitative]

    useful_data.append([subject, course, section, name, id, location, values, writing, social,
                        humanities, multicultural1, multicultural2, language, naturalscience, quantitative])

# save this combined data to a new json file but only the data part
with open('classes.json', 'w') as outfile:
    json.dump(useful_data, outfile)

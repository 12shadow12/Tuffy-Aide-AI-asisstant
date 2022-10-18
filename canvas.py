import strings
import config
import requests


BASE_URL = strings.URLS["canvas"]
courses = {}
assignments = {}

def getSchedule():
    url = BASE_URL + "?access_token=" + config.APIKEYS["canvas"]
    response = requests.get(url).json()

    for c in response:
        if "name" in c and "id" in c:
            if "Fall 2022" in c["name"]:
                courses[str(c["id"])] = c["name"]
    print(courses)
    return courses.values()

def getAssignments():
    if not courses:
        getSchedule()
    for key, value in courses.items():
        url = BASE_URL + "/" + key + "/assignments?access_token=" + config.APIKEYS["canvas"]
        response = requests.get(url).json()
        
        for assignment in response:
            if assignment["locked_for_user"] and "Roll Call" not in assignment["name"]:
                continue
            if value not in assignments.keys():
                assignments[value] = []
            assignments[value].append(assignment["name"])

    for key, values in assignments.items():
        print(key + ":")
        for k in values:
            print("\t" + k)

getAssignments()
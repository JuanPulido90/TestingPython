import json
import jsonpath
import requests


def test_add_new_student():
    global id
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('/Users/juan/Documents/Python/API Testing/addStudent.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_get_details():
    url = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(url)
    print(response.text)

# 7457408

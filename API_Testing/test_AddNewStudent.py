import requests
import json
import jsonpath


# POST Request
def test_add_student_data():
    url = "https://thetestingworldapi.com/api/StudentsDetails"
    file = open('/Users/juan/Documents/Python/API Testing/request.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(url, json_request)
    print(response.text)


# PUT request
def test_update_student_data():
    url = "https://thetestingworldapi.com/api/StudentsDetails/7457259"
    file = open('/Users/juan/Documents/Python/API Testing/request.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(url, json_request)
    print(response.text)


# DELETE request
def test_delete_student():
    url = 'https://thetestingworldapi.com/api/StudentsDetails/7457259'
    response = requests.delete(url)
    print(response.text)


# GET request
def test_get_student_data():
    url = 'https://thetestingworldapi.com/api/StudentsDetails/7457259'
    response = requests.get(url)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 7457259

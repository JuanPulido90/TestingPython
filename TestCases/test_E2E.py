import requests
import json
import jsonpath


def test_add_new_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('/Users/juan/Documents/Python/API Testing/request.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = 'https://thetestingworldapi.com/api/technicalskills'
    file = open('/Users/juan/Documents/Python/API Testing/technical.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = 'https://thetestingworldapi.com/api/addresses'
    file = open('/Users/juan/Documents/Python/API Testing/address.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(add_api_url, request_json)

    final_details = 'https://thetestingworldapi.com/api/FinalStudentDetails/7457387'
    response = requests.get(final_details)
    print(response.text)
# 7457387
# 7457389

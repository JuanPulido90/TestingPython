import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"

def test_create_new_user():
    #Read input json file
    file = open('/Users/juan/Documents/Python/API Testing/users.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    #Make POST request with Json input body
    response = requests.post(url,request_json)
    #validate response code
    assert response.status_code == 201
    # #Fetch header from response
    # print(response.headers.get('Content-Length'))
    # #Parse response to Json format
    # response_json = json.loads(response.text)
    # # Pick Id using json path
    # id = jsonpath.jsonpath(response_json, 'id')
    # print(id[0])

def test_create_other_user():
    #Read input json file
    file = open('/Users/juan/Documents/Python/API Testing/users.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url,request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

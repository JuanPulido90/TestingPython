import json
import jsonpath
import requests
import openpyxl
from DataDriven import Library


def test_add_multiple_data():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('/Users/juan/Documents/Python/API Testing/newStudent.json', 'r')
    json_request = json.loads(file.read())

    obj = Library.Common("/Users/juan/Documents/Python/API Testing/testData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    #Excel code
    for i in range (2, row+1):
        updated_json_request = obj.update_request_with_data(i,json_request,keyList)
        response = requests.post(url, updated_json_request)
        print(response)







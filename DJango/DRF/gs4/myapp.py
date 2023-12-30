import requests
import json
URL = "http://127.0.0.1:8080/studentapi/"


def get_data(id=None):
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


get_data()


def post_data():
    data = {}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()

import requests
import json

URL = "http://127.0.0.1:8000/"

# GET METHOD
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
        json_data = json.dumps(data)
        r = requests.get(url = URL,data = json_data)
        data = r.json()
        print(data)

get_data()


# POST METHOD
# def post_data():
#     data = {
#         'name':'Rahul',
#         'roll':104,
#         'city':'Mumbai'
# }
#     headers = {'content-Type':'application/json'}
#     json_data = json.dumps(data)
#     r = requests.post(url = URL ,header= headers, data  = json_data)
#     data = r.json(data)
#     print(data)

# post_data()
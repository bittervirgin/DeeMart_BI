# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import datetime

def api_call():
    url = "https://api.yelo.red/open/orders/getAll"
    parameter = {
        "api_key": "aad87082b5e5cde09257c29948bb37b0",
        "marketplace_user_id": 373138,
        "order_status": 13,
        "sortCol": 1,
        "start": 1,
        "length": 5,
        "start_date": "20201009",
        "end_date": "20201009"
    } 
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response


#print(api_call)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def jsave(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)
    return text
    #with open('data20201009.txt', 'w') as outfile:
        #json.dump(text, outfile)
    
def save_json():
    with open('data20201009.json', 'w') as outfile:
        json.dump(api_call().json(), outfile)


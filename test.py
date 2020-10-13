# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
from datetime import date
api_key = "aad87082b5e5cde09257c29948bb37b0"
fleet_ids = [662610, 729894, 730509, 794724, 792004]
def process_date():
    today = date.today()
    today = str(today)
    print(today)
    year = today[0:4]
    month = today[5:7]
    day = int(today[8:10]) - 1
    yesterday = year + month + str(day)
    return yesterday
def api_call():
    url = "https://api.yelo.red/open/orders/getAll"
    parameter = {
        "api_key": api_key,
        "user_id": 373138,
        "marketplace_user_id": 373138,
        "order_status": 13,
        "start": 0,
        "length": 1000,
        "start_date": process_date(),
        "end_date": process_date()
    } 
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response
def user_details():
    url = "https://api.yelo.red/open/customer/view"
    parameter = {
        "api_key": api_key,
        #"marketplace_user_id": 373138
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params = parameter, headers=headers)
    return response
def agent_api():
    url = "https://private-anon-405ba5e8b1-tookanapi.apiary-proxy.com/v2/get_fleets_availability"
    parameter = {
    "api_key":"51646384f34a57081c586c7b5d46254314e3cdf822d4733a541e01   ", 
    "local_date_time":process_date(),
    "limit" : 0
}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response
#print(api_call)
def order_details():
    url = "https://api.yelo.red/open/orders/getDetails"
    parameter = {
        "api_key": api_key,
        "job_id": 2877732
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response

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
    
def save_json(obj):
    if obj == "orders":
        with open('orders_%s.json' + %yesterday(), 'w') as outfile:
            json.dump(api_call().json(), outfile)
    if obj == "customer":
        with open('users_20201010.json', 'w') as outfile:
            json.dump(user_details().json(), outfile)
    if obj == "agent":
        with open('agent_20201010.json', 'w') as outfile:
            json.dump(agent_api().json(), outfile)
        #print("1")
'''    
#order_details = jsave(api_call().json())
order_details = api_call().json()
print(type(order_details))
save_json("orders")
#print(order_details)

data = order_details['data']
count = data['count']
jobs = data['all_jobs']
#jprint(jobs)
print(len(jobs))
total = 0
revenue = 0
agent = []
for i in range(len(jobs)):
    
    order = jobs[i]
    #print(order['merchant_name'])
    total += len(order['product_ids'])
    revenue += order['order_amount']

for i in range(len(jobs)):
    order = jobs[i]
    seen = set(agent)
    if order['job_pickup_phone'] not in seen:
        seen.add(order['job_pickup_phone'])
        agent.append(order['job_pickup_phone'])
print("Revenue ", revenue)
print("Total orders: ", count)
print("Total products: ",total)
basket_size = total/count
print("Ticket size: ", revenue/count)
print("Basket size:",basket_size)
#print("Agent: ", len(agent))
#print("Agent: ", agent)
order = jobs[0]
print(type(order))
agent_details = agent_api().json()
jsave("agent")
jprint(agent_details)
customer = user_details().json()
#jprint(customer)

save_json("customer")
#print(type(jobs))
#jprint(jobs[1])
'''

'''
order_detail = order_details().json()
jprint(order_detail)
'''


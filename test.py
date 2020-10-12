# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import datetime
api_key = "aad87082b5e5cde09257c29948bb37b0"
def api_call():
    url = "https://api.yelo.red/open/orders/getAll"
    parameter = {
        "api_key": api_key,
        "user_id": 373138,
        "marketplace_user_id": 373138,
        "order_status": 13,
        "start_date": "20201009",
        "end_date": "20201009"
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
    response = requests.get(url, params = parameter)
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
    
def save_json(obj):
    if obj == "orders":
        with open('orders_20201009.json', 'w') as outfile:
            json.dump(api_call().json(), outfile)
    if obj == "customer":
        with open('users_20201009.json', 'w') as outfile:
            json.dump(user_details().json(), outfile)
     
#order_details = jsave(api_call().json())
order_details = api_call().json()
print(type(order_details))
save_json("orders")
#print(order_details)

data = order_details['data']
count = data['count']
jobs = data['all_jobs']
#jprint(jobs)
total = 0
revenue = 0
for i in range(len(jobs)):
    print(i)
    order = jobs[i]
    print(order['merchant_name'])
    total += len(order['product_ids'])
    revenue += order['order_amount']
print("Revenue ", revenue)
print("Total orders: ", count)
print("Total products: ",total)
basket_size = total/count
print("Ticket size: ", revenue/count)
print("Basket size:",basket_size)
order = jobs[0]
print(type(order))   

customer = user_details().json()
#jprint(customer)

save_json("customer")
#print(type(jobs))
#jprint(jobs[1])
# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
from datetime import date
import xlwt
from xlwt import Workbook
api_key = "aad87082b5e5cde09257c29948bb37b0"

fleet_ids = [662610, 729894, 730509, 794724, 792004]
def process_date():
    today = date.today()
    #today = today.strftime("%Y%M%D")
    today = str(today)
    #print("Today: ",today)
    
    year = today[0:4]
    month = today[5:7]
    day = int(today[8:10]) - 1
    yesterday = year + month + str(day)
    
    return yesterday

def api_call(user_id, start_date, end_date):
    url = "https://api.yelo.red/open/orders/getAll"
    parameter = {
        "api_key": api_key,
        "user_id": user_id,
        "marketplace_user_id": 373138,
        "order_status": 13,
        "start": 0,
        "length": 1000,
        "start_date": str(start_date),
        "end_date": str(end_date)
    } 
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response

def user_details():
    url = "https://api.yelo.red/open/customer/view"
    parameter = {
        "api_key": "aad87082b5e5cde09257c29948bb37b0",
        "marketplace_user_id": 373138,
        "length": 1500
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params = parameter, headers=headers)
    return response

def get_all_agent():
    url = "https://api.tookanapp.com/v2/get_all_fleets"
    parameter = {
    "api_key":"51646384f34a57081c586c7b5d46254314e3cdf822d4733a541e01"

    }   
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response
#print(api_call)

def order_details(job_id):
    url = "https://api.yelo.red/open/orders/getDetails"
    parameter = {
        "api_key": api_key,
        "job_id": job_id
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
    
def save_json(obj, user_id):
    yesterday = str(process_date())
    if obj == "orders":
        
        with open('orders_{0}_{1}.json'.format(str(yesterday),str(user_id)), 'w')  as outfile:
            json.dump(api_call(user_id, yesterday, yesterday).json(), outfile)
        print("Success")
    if obj == "customer":
        with open('users_%s.json' %yesterday, 'w') as outfile:
            json.dump(user_details().json(), outfile)
    '''

    if obj == "agent":
        with open('agent_%s.json' %yesterday, 'w') as outfile:
            json.dump(agent_api().json(), outfile)
        #print("1")
    '''

def open_file(ftype, user_id):
    if ftype == "orders":
        yesterday = process_date()
        with open('orders_{0}_{1}.json'.format(str(yesterday),str(user_id)), 'r') as f:
            orders = f.read()

    return orders

#Get list of orders
def get_list_order(user_id):
    yesterday = str(process_date())
    list_orders = []
    #save_json("orders", user_id)
    all_orders = api_call(user_id, yesterday, yesterday).json()
    data = all_orders['data']
    jobs = data['all_jobs']
    for i in range(len(jobs)):
        #print(i)
        order = jobs[i]
        list_orders.append(order['job_id'])
    return list_orders


#get total quantity 
def get_quantity(user_id):
    print("Quantity")
    quantity = 0
    list_orders = get_list_order(user_id)
    for i in range(len(list_orders)):
        order = order_details(list_orders[i]).json()
        data = order['data']
        #print(type(data))
        #jprint(data)
        data1 = data[0]
        data = data1['orderDetails']
        for i in range(len(data)):
            #print(i)
            order_detail = data[i]
            product = order_detail['product']
            quantity += product['quantity']
    return quantity

def get_promo_list():
    url = "https://api.yelo.red/open/promo/get"
    params = {
        "api_key": api_key,
        "start": 0,
        "length": 100
    }

    header = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(params), headers=header)
    return response

#jprint(user_details().json())
def order_call():
    url = "https://api.yelo.red/open/orders/getAll"
    parameter = {
        "api_key": api_key,
        "user_id": 660774,
        "marketplace_user_id": 373138,
        "order_status": 13,
        "start": 0,
        "length": 1000,
        "start_date": str(process_date()),
        "end_date": str(process_date())
    } 
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(parameter), headers=headers)
    return response

#jprint(user_details().json())
def first_order_counting():

    users = user_details().json()
    data = users['data']
    #jprint(data)\
    j = 0
    #wb = Workbook()
    #sheet1 = wb.add_sheet('Sheet 1')
    user_list = []
    print(type(user_list))
    for i in range(len(data)):
        details = data[i]
        datetime = details['creation_datetime']
        #sheet1.write(i, 2, details['creation_datetime'])
        dt = str(datetime).split('T')
        ymd = dt[0].split('-')
        temp = {}
        if (int(ymd[1]) >= 10):
            if ( int(ymd[2]) >= 10 ):
                j += 1
                temp['name'] = details['name']
                temp['id'] = details['vendor_id']
                user_list.append(temp)
            #sheet1.write(i, 0, details['name'])
            #sheet1.write(i, 1, details['phone_no'])
    #print(user_list)
    start_date = "20201010"
    end_date = str(process_date())
    orders_list = api_call(660774, start_date, end_date).json()
    data = orders_list['data']
    #count = data['count']
    jobs = data['all_jobs']
    amount = 0
    user_id_list = list(set([user['id'] for user in user_list]))
    customer_id = list(set([job['customer_id'] for job in jobs]))
    from collections import Counter
    a = dict(Counter(user_id_list + customer_id))
    a = {k: v for k, v in sorted(a.items(), key=lambda item: item[1], reverse=True)}
    print(a)
    amount = len([x for x in a if a[x] == 2])
    print(amount)
    #wb.save('regis user.xls')
first_order_counting()


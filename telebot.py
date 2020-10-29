import requests
import test
from datetime import datetime
import time
import json
import os.path
merchant_list = [660774, 373138]
group_id = ["-473360139", "-334458180"]
personal_id = "1199485011"
def api_call(text, chat_id):
    url = "https://api.telegram.org/bot"
    token = "1253557076:AAGiiX_5xSfDz6PqPit8MuzuTU0A8MhczKk"
    chat_id = personal_id #chat_id of person or group you want to send messsages

    endpoint = url + token + "/sendMessage?chat_id=" + chat_id + "&text=" + text
    response = requests.get(endpoint)

    return response

def generate_report():
    print("report")
    #get yesterday date
    yesterday = test.process_date()
    '''
    for i in range(len(yesterday)):
        print("i: ",i, yesterday[i])
    '''
    yesterday = test.process_date()
    year = yesterday[0:4]
    month = yesterday[4:6]
    day = yesterday[6:8]
    
    yesterday = day + " - " + month + " - " + year
    

    #check if json file is available
    start_time = time.time()
    if (os.path.isfile('orders_{0}.json'.format(str(test.process_date()))) == False):
        test.save_json("orders")
        orders = json.loads(test.open_file("orders"))
    else: orders = json.loads(test.open_file("orders"))
    #orders = json.loads(test.open_file("orders"))
    #Processing report
    data = orders['data']
    count = data['count']
    count_test = 0
    jobs = data['all_jobs']
    #total = test.get_quantity(merchant_id)
    revenue = 0
    '''
    if merchant_id == 660774:
        merchant_name = "Phú Mỹ Hưng"
    else: merchant_name = "Era Town"
    '''
    total_quantity = test.get_quantity()
    count = count - count_test
    order_amount = sum([order.get('order_amount', 0) for order in jobs])
    revenue = "{:,.0f}".format(order_amount)
    basket_size = total_quantity/count
    ticket_size = int(order_amount)/count
    ticket_size = "{:,.2f}".format(ticket_size)
    #Customer development
    new_user, sign_up = test.first_order_counting()
    print(sign_up)
    DAU = test.daily_active_user()
    #create message content
    text =  "\t DAILY UPDATE " + str(yesterday) + "\n" + "SALES METRICS\n" + "Revenue: " + str(revenue) + "\nOrders: " + str(count) + "\nTicket size: " + str(ticket_size) + "\nBasket size: " + str(round(basket_size, 2)) + "\nCUSTOMER DEVELOPMENT" + "\nDaily Active User: "+ str(DAU)  +"\nNew user: " + str(new_user) +"\nConversion rate: "+ str(round(new_user/sign_up, 2))
    end_time = time.time()

    print("Generate report time:", end_time-start_time)
    return text


if  __name__ == "__main__":
    yesterday = test.process_date()
    year = yesterday[0:4]
    month = yesterday[4:6]
    day = yesterday[6:8]
    
    yesterday = day + " - " + month + " - " + year
    print(yesterday)
    text = "#DAILY UPDATE " + str(yesterday) + "\n"
    #api_call(text)
    for id in group_id:   
        api_call(generate_report(), id)
    

    




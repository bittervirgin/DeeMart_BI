import requests
import test
from datetime import datetime
import json
import os.path
merchant_list = [660774, 373138]
def api_call(text):
    url = "https://api.telegram.org/bot"
    token = "1253557076:AAGiiX_5xSfDz6PqPit8MuzuTU0A8MhczKk"
    chat_id = "1199485011" #chat_id of person or group you want to send messsages

    endpoint = url + token + "/sendMessage?chat_id=" + chat_id + "&text=" + text
    response = requests.get(endpoint)

    return response

def generate_report(merchant_id):
    print("report")
    yesterday = test.process_date()
    '''
    for i in range(len(yesterday)):
        print("i: ",i, yesterday[i])
    '''
    #check if json is available
    if (os.path.isfile('orders_%s.json' %yesterday) == False):
        test.save_json("orders", merchant_id)
    else: test.open_file("orders")
    
    year = yesterday[0:4]
    month = yesterday[4:6]
    day = yesterday[6:8]
    
    yesterday = day + " - " + month + " - " + year
    print(yesterday)
    
    orders = json.loads(test.open_file("orders"))
    data = orders['data']
    count = data['count']
    
    jobs = data['all_jobs']
    total = test.get_quantity(merchant_id)
    revenue = 0
    if user_id == 660774:
        merchant_name = "Phú Mỹ Hưng"
    else: merchant_id = "Era Town"
    for i in range(len(jobs)):
        print(i)
        order = jobs[i]
        
        revenue += order['order_amount']
    basket_size = total/count
    ticket_size = revenue/count
    
    text = "DAILY REPORT" + str(yesterday) + "\n" + "SALES METRICS (" + merchant_name + ")  \n"   + "Revenue: " + str(revenue) + "\n Orders: " + str(count) + "\n Ticket size: " + str(round(ticket_size, 2)) + "\n Basket size:" + str(round(basket_size, 2))
    return text


if  __name__ == "__main__":
    for i in range(len(merchant_list)):
        user_id = merchant_list[i]
        api_call(generate_report(user_id))
    

    




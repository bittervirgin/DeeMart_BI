import requests
import test
from datetime import datetime
import json

def api_call(text):
    url = "https://api.telegram.org/bot"
    token = "1253557076:AAGiiX_5xSfDz6PqPit8MuzuTU0A8MhczKk"
    chat_id = "1199485011"

    endpoint = url + token + "/sendMessage?chat_id=" + chat_id + "&text=" + text
    response = requests.get(endpoint)

    return response

def generate_report():
    yesterday = test.process_date()
    yesterday = yesterday.strftime("%d-/%m-/%Y")
    print(yesterday)
    orders = json.loads(test.open_file("orders"))
    #print("Orders type: ",type(orders))
    data = orders['data']
    #print("Data type: ",type(data))
    #print(data['count'])
    count = data['count']
    #test.jprint(data)
    
    jobs = data['all_jobs']
    total = 0
    revenue = 0

    for i in range(len(jobs)):
        print(i)
        order = jobs[i]
        product_details = order['product_details']
        for j in range(len(product_details)):
            product = product_details[j]
            print(product)
            total += int(product[len(product) - 4])
        #total += len(order['product_ids'])
        revenue += order['order_amount']
    basket_size = total/count
    ticket_size = revenue/count
    
    text = "DAILY REPORT" + str(yesterday) + "\n" + "SALES METRICS (ERA TOWN) \n" + "Revenue: " + str(revenue) + "\n Orders: " + str(count) + "\n Ticket size: " + str(round(ticket_size, 2)) + "\n Basket size:" + str(round(basket_size, 2))
    return text

if __name__ == "__main__":
    """
    now = str(datetime.now().time())
    hour = now[0:2]
    minute = now[3:5]
    if hour == "11":
        if minute > "01":
            api_call(generate_report())
            """
    api_call(generate_report())
    

    




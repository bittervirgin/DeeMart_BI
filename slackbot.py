import requests
from datetime import datetime, time
import json
#import test
from slacker import Slacker
def bot_oauth():
    pass
def slack_api():
    url = "https://slack.com/api/chat.postMessage"
    parameter = {
        "token": "xoxb-1238984517398-1425483195283-Pr8RzlN533G0dtPfZ5rkrGml",
        "channel": "C0177M0TK18",
        "text": "Hello world"
    }
    header = {'Content-Type': 'application/json'}
    response = requests.post(url, data=parameter, headers=header)
    return response

print(slack_api().json())
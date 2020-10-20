from flask import Flask,render_template, jsonify,g
import requests
import json
import logging

DEBUG=True

import http.client as http_client

http_client.HTTPSConnection.debuglevel =0

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"
    payload = " \r\n{\r\n\"searchOptions\": {\r\n\"matchScore\": \"true\",\r\n\"maxRecords\": \"5\",\r\n\"matchIndicators\": \"true\"\r\n},\r\n\"header\": {\r\n\"startIndex\": \"0\",\r\n\"requestMessageId\": \"Request_001\",\r\n\"messageDateTime\": \"2020-10-19T10:39:49.903\"\r\n},\r\n\"searchAttrList\": {\r\n\"distanceUnit\": \"M\",\r\n\"distance\": \"2\",\r\n\"merchantCountryCode\": \"840\",\r\n\"latitude\": \"37.363922\",\r\n\"longitude\": \"-121.929163\",\r\n\"merchantName\": \"Starbucks\"\r\n},\r\n\"responseAttrList\": [\r\n\"GNLOCATOR\"\r\n]\r\n}"
    headers = {
        'Content-Type': "application/json"
    }
    user_id = 'F1860V207Z9KKGL6XD5S21cZZa25epJyWY3GhHWCsvva2uJHE'
    password = 'jj2GXDNG'
    cert = 'C:/Users/Dell/Downloads/cert.pem'
    key = 'C:/Users/Dell/Downloads/key_a4dbf961-80de-48e5-ae02-2f5c187b67ab.pem'
    timeout = 10

    try:
        response = requests.request("POST",url,cert = (cert,key),headers=headers,auth=(user_id,password),data = payload,timeout=timeout)
    except Exception as e:
        print(e)
    if DEBUG : return response.content
if __name__ == '__main__':
    app.run(debug=True)
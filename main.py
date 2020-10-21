from flask import Flask, jsonify, request, render_template
import requests
#import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.load_cert_chain('C:/Users/Dell/Downloads/cert.pem',
 #                       'C:/Users/Dell/Downloads/key_a4dbf961-80de-48e5-ae02-2f5c187b67ab.pem')
import http.client as http_client

import datetime
import pytz
import random
import re

app = Flask(__name__)

#need to figure out the response we will give for each of these API and modify them

def transformPayload(payload):
    payload = editLocalTime(payload)
#    payload = json.loads(payload)
    return payload

def editLocalTime(payload):
    timezone = pytz.timezone("America/Los_Angeles")
    timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
    pattern = re.compile('"messageDateTime":".{23}"', re.IGNORECASE)
    replacement = '"messageDateTime":"'+timestamp+'.903"'
    payload = re.sub(pattern, replacement, payload)
    return payload

@app.route("/")
def index3():
    return render_template('index.html')

@app.route("/login",methods = ['POST'])
def index():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if(username == 'admin' and password == 'password'):
            return render_template('after_login.html')
        else:
            return render_template('index.html')

@app.route("/profile",methods = ['GET','POST'])
def profile():
    return render_template('merchant_profiles.html')

@app.route("/viewList",methods = ['POST'])
def view1():
    if(request.method == 'POST'):
        countrycode = request.form['countrycode']
        postalcode = request.form['pincode']
        categorycode = request.form['categorycode']
        url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"
                
        payload = '{"searchOptions":{"matchScore": "true","maxRecords": "5","matchIndicators": "true"},"header": {"startIndex": "1","requestMessageId": "Request_001","messageDateTime": "2020-10-20T10:30:10.903"},"searchAttrList": {"distanceUnit": "KM","distance": "20","merchantCountryCode": "'+countrycode+'","merchantPostalCode": "'+postalcode+'","merchantCategoryCode":["'+categorycode+'"]},"responseAttrList": ["GNLOCATOR"]}'
        
        res = transformPayload(payload)
        
#        payload = "{\r\n\"searchOptions\": {\r\n\"matchScore\": \"false\",\r\n\"maxRecords\": \"5\",\r\n\"matchIndicators\": \"true\"\r\n},\r\n\"header\": {\r\n\"startIndex\": \"0\",\r\n\"requestMessageId\": \"Request_001\",\r\n\"messageDateTime\": \"2020-10-19T10:39:49.903\"\r\n},\r\n\"searchAttrList\": {\r\n\"distanceUnit\": \"M\",\r\n\"distance\": \"20\",\r\n\"merchantCountryCode\": \"840\",\r\n\"merchantPostalCode\":\"95110-1216\",\r\n\"merchantCategoryCode\": [\"5814\"]\r\n},\r\n\"responseAttrList\": [\r\n\"GNLOCATOR\"\r\n]\r\n}"
#        
        headers = {
            'Content-Type': "application/json"
        }
        user_id = 'F1860V207Z9KKGL6XD5S21cZZa25epJyWY3GhHWCsvva2uJHE'
        password = 'jj2GXDNG'
        cert = 'C:/Users/Dell/Downloads/cert.pem'
        key = 'C:/Users/Dell/Downloads/key_a4dbf961-80de-48e5-ae02-2f5c187b67ab.pem'
        timeout = 10

        response = requests.request("POST",url,cert = (cert,key),headers=headers,auth=(user_id,password),data = res,timeout=timeout)
        print(response.text.encode('utf8'))
        return render_template('merchant_list.html')

    else:
        return jsonify({"error":"invalid input"})

@app.route("/transactionScore",methods= ['GET','POST'])
def index2():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent':some_json})
    else:
        return jsonify({"error":"invalid input"})


if __name__ == '__main__':
    app.run(debug=True)

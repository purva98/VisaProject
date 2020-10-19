from flask import Flask, jsonify, request
import requests
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('C:/Users/Dell/Downloads/cert.pem',
                        'C:/Users/Dell/Downloads/key_a4dbf961-80de-48e5-ae02-2f5c187b67ab.pem')


app = Flask(__name__)

#need to figure out the response we will give for each of these API and modify them

@app.route("/")
def index():
    return "Login Page";

@app.route("/merchantLocator",methods= ['GET','POST'])
def index1():
    if(request.method == 'GET'):

        url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"

        payload = " \r\n{\r\n\"searchOptions\": {\r\n\"matchScore\": \"true\",\r\n\"maxRecords\": \"5\",\r\n\"matchIndicators\": \"true\"\r\n},\r\n\"header\": {\r\n\"startIndex\": \"0\",\r\n\"requestMessageId\": \"Request_001\",\r\n\"messageDateTime\": \"2020-10-19T10:39:49.903\"\r\n},\r\n\"searchAttrList\": {\r\n\"distanceUnit\": \"M\",\r\n\"distance\": \"2\",\r\n\"merchantCountryCode\": \"840\",\r\n\"latitude\": \"37.363922\",\r\n\"longitude\": \"-121.929163\",\r\n\"merchantName\": \"Starbucks\"\r\n},\r\n\"responseAttrList\": [\r\n\"GNLOCATOR\"\r\n]\r\n}"
        headers = {
            'Authorization': 'Basic RjE4NjBWMjA3WjlLS0dMNlhENVMyMWNaWmEyNWVwSnlXWTNHaEhXQ3N2dmEydUpIRTpqajJHWERORw==',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))
        return response.text

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
   # context  = ('C:/Users/Dell/Downloads/key_a4dbf961-80de-48e5-ae02-2f5c187b67ab.pem','C:/Users/Dell/Downloads/cert.pem')
    app.run(debug=True,ssl_context=context)



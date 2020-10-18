from flask import Flask, jsonify,request
app = Flask(__name__)

#need to figure out the response we will give for each of these API and modify them

@app.route("/merchantFinder",methods= ['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent':some_json})
    else:
        return jsonify({"error":"invalid input"})

@app.route("/transactionScore",methods= ['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent':some_json})
    else:
        return jsonify({"error":"invalid input"})


if __name__ == '__main__':
    app.run(debug=True)



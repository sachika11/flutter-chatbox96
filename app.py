from re import I
from flask import Flask, app,jsonify,request
import time

app = Flask(__name__)
@app.route("/bot",method=["POST"])

#response
def response():
    query =dict(request.form)['query']
    result = query +" "+time.ctime()
    return jsonify({"response":result})

if __name__ =="main":
    app.run(host="0.0.0.0")

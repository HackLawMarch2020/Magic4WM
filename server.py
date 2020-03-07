from flask import Flask, escape, request
import sqlite3
import json

def connectToDb(dbname):
    connection = sqlite3.connect(dbname)
    return connection

def dbSetup():
    pass

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello mate</h1>"

@app.route('/apitest', methods=['POST'])
def api():
    data = {
        "hello": 1,
        "hellno": 2
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/<string:texts>', methods=['GET'])
def wild(texts):
    return('Hey, that\'s pretty good: ' +  texts)

def run():
    app.run(port=80)

if __name__ == '__main__':
    run()
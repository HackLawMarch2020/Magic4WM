from flask import Flask, escape, request
import sqlite3
import json
import smtplib

def connectToDb():
    connection = sqlite3.connect("magicwm")
    return connection

def dbSetup():
    conn = connectToDb()
    cursor = conn.cursor()
    with open("tables.sql", "r") as fp:
        line = fp.readline()
        while line:
            print(line)
            cursor.execute(line)
            line = fp.readline()
    #cursor.execute(filecontent)
    conn.commit()
    conn.close()
    #exec.sql(filecontent)

def createDBmatter(matterobj):
    query = "INSERT INTO matters (matterName, requestingClientId, priorityId, timeNeeded, timeLogged, isBillable, deadline) VALUES (?, ?, ?, ?, ?, ?, ?)"
    data_tuple = (matterobj["name"], matterobj["requestingClientId"], matterobj["priorityId"], matterobj["timeNeeded"], matterobj["timeLogged"], matterobj["isBillable"], matterobj["deadline"])
    conn = connectToDb()
    cursor = conn.cursor()
    cursor.execute(query, data_tuple)
    conn.commit()
    conn.close()

def getDBmatter():
    query = "SELECT * FROM matters"
    conn = connectToDb()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    returnedArr = []
    for row in rows:
        returnedArr.append(row)
    return returnedArr

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello mate/homie</h1>"

@app.route('/dbmatters', methods=['GET'])
def matters():
    return str(getDBmatter())

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

@app.route('/posttest', methods=['POST'])
def testing():
    data = request.json
    print(data)
    res = app.response_class(
        response = str(data),
        status = 200,
        mimetype='text/html'
    )
    return res

@app.route('/api/createMatter', methods=['POST'])
def matterCreate():
    data = request.json
    matterobject = {
        "name": data["name"],
        "requestingClientId": int(data["clientid"]),
        "priorityId": int(data["priority"]),
        "timeNeeded": int(data["timeneeded"]),
        "timeLogged": int(data["timelogged"]),
        "isBillable": int(data["billable"]),
        "deadline": int(data["deadline"])
    }
    print(matterobject)
    createDBmatter(matterobject)
    res = app.response_class(
        response = str("Matter created."),
        status = 200,
        mimetype='text/html'
    )
    return res

@app.route('/<string:texts>', methods=['GET'])
def wild(texts):
    return('Hey, that\'s pretty good: ' +  texts)

def run():
    #dbSetup()
    metobj = {
    "name": "somename",
    "requestingClientId": 4,
    "priorityId": 1,
    "timeNeeded": 30,
    "timeLogged": 25,
    "isBillable": 0,
    "deadline": 1583663675
    }
    #createDBmatter(metobj)
    #print(getDBmatter())
    app.run(port=80)

if __name__ == '__main__':

    run()
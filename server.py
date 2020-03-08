from flask import Flask, escape, request
import sqlite3
import json
import smtplib
import time

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

def createDBuser(userobj):
    query = "INSERT INTO users (username, passwordHash, timeCreated) VALUES (?, ?, ?)"
    data_tuple = (userobj["username"], userobj["password"], int(round(time.time() * 1000)))
    conn = connectToDb()
    cursor = conn.cursor()
    cursor.execute(query, data_tuple)
    conn.commit()
    conn.close()

def getDBusers():
    query = "SELECT * FROM users"
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

def createDBTask(taskobject):
    query = "INSERT INTO tasks (matterId, taskName, taskAssigneeId, taskStatusId, timeLogged, timeNeeded, priorityId, specialisationNeededId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data_tuple = (taskobject["matterid"], taskobject["name"], taskobject["assigneeid"], taskobject["statusid"], taskobject["timelogged"], taskobject["timeneeded"], taskobject["priority"], taskobject["specialisation"])
    conn = connectToDb()
    cursor = conn.cursor()
    cursor.execute(query, data_tuple)
    conn.commit()
    conn.close()

def getDBTasks():
    query = "SELECT * FROM tasks"
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

@app.route('/dbusers', methods=['GET'])
def users():
    return str(getDBusers())

@app.route('/dbtasks', methods=['GET'])
def tasks():
    return str(getDBTasks())

@app.route('/api/getMatters', methods=['POST'])
def postUsers():
    dataArr = []
    matters = getDBmatter()
    for matter in matters:
        dataArr.append(
            {
                "name": matter[1],
                "requestingClientId": matter[2],
                "priorityId": matter[3],
                "timeNeeded": matter[4],
                "timeLogged": matter[5],
                "isBillable": matter[6],
                "deadline": matter[7]
            }
        )
    response = app.response_class(
        response=json.dumps(dataArr),
        status=200,
        mimetype='application/json'
    )
    return response

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
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/api/createUser', methods=['POST'])
def userCreate():
    data = request.json
    userobject = {
        "username": data["username"],
        "password": data["password"]
    }
    createDBuser(userobject)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/api/createTask', methods=['POST'])
def taskCreate():
    data = request.json
    taskobject = {
        "matterid": data["matterid"],
        "name": data["name"],
        "assigneeid": data["assignee"],
        "statusid": data["status"],
        "timelogged": data["timelogged"],
        "timeneeded": data["timeneeded"],
        "priority": data["priority"],
        "specialisation": data["specialisation"]
    }
    createDBTask(taskobject)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/<string:texts>', methods=['GET'])
def wild(texts):
    return('Hey, that\'s pretty good: ' +  texts)

def run():
    #dbSetup()
    #createDBmatter(metobj)
    #print(getDBmatter())
    app.run(port=80)

if __name__ == '__main__':

    run()
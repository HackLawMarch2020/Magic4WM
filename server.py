from flask import Flask, escape, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello mate</h1>"

@app.route('/apitest', methods=['POST'])
def api():
    return "NO."

@app.route('/<string:text>', methods=['GET'])
def wild(text):
    return('Hey, that\'s pretty good: ' +  text)

def run():
    app.run()

if __name__ == '__main__':
    run()
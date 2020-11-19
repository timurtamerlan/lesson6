from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello github'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/brichev')
def brichev():
    return 'Hello from CI with GitHub Actions by Brichev'
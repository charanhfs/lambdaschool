from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'March, 3rd 1995'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello %s' % name

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    int1 = int(num1)
    int2 = int(num2)
    return str(int1+int2)

@app.route("/multiply/<num1>/<num2>")
def multiply(num1, num2):
    int1 = int(num1)
    int2 = int(num2)
    return str(int1*int2)

@app.route("/subtract/<num1>/<num2>")
def subtract(num1, num2):
    int1 = int(num1)
    int2 = int(num2)
    return str(int1-int2)

@app.route("/favoritefoods")
def favoritefoods():
    mylist = ["indian food", "fries", "italian food"]
    return jsonify(mylist)

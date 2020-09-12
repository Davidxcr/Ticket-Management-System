from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    name = 'Femi'
    return render_template('hello.html', name=name)

@app.route('/login')
def login():
    return render_template('login.html')
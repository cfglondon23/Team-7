from flask import render_template, request, redirect, session
from app import app
from fb import user


@app.route('/', methods=['POST', 'GET'])
def index():
    return "Team 7"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        successful, token = user.sign_in(email, password)

        if not successful:
            return render_template('login.html', negative=True, message="Email and/or password incorrect")
        session['id'] = token
        return render_template('login.html', negative=False, message="Successfully logged in")
    else:
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        successful = user.register(email, password)

        if not successful:
            return render_template('register.html', negative=True, message="Try again later")
        return render_template('register.html', negative=False, message="Successfully registered")
    else:
        return render_template('register.html')

@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    return render_template('leaderboard.html')

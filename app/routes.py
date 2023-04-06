from flask import render_template, request, redirect, session
from app import app


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('main.html')

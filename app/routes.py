from flask import render_template, request, redirect, session
from app import app


@app.route('/', methods=['POST', 'GET'])
def index():
    return "Team 7"

#!/usr/bin/env python3.7.9
# Above line is to set the interpreter

# Imports
from flask import Flask, request, url_for, render_template
import os


# App Setup
app = Flask(__name__)
app.static_folder = 'static'
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

# Main Page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
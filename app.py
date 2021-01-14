#!/usr/bin/env python3.7.9
# Above line is to set the interpreter

# Imports
from flask import Flask, request, url_for, render_template


# App Setup
app = Flask(__name__)
app.static_folder = 'static'


# Main Page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
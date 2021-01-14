#!/usr/bin/env python3.7.9
# Above line is to set the interpreter

# Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request, url_for, render_template, redirect, session, make_response, jsonify, flash
import random, string, os, httplib2, json, requests, httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import session as login_session


app = Flask(__name__)
app.static_folder = 'static'

# Main Page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
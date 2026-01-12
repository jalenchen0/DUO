# Imports
from flask import Flask, render_template, request, flash, url_for, redirect, session
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import db
import json
from urllib.request import Request, urlopen
import pprint
import os
import api
import re
# Initialize databases

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html")
@app.route("/login", methods=['GET', 'POST'])
@app.route("/logout", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html")
@app.route("/create", methods=['GET', 'POST'])
@app.route("/profile", methods=['GET', 'POST'])


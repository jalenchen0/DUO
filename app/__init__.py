# Imports
from flask import Flask, render_template, request, flash, url_for, redirect, session
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
#import db
import json
from urllib.request import Request, urlopen
import pprint
import os
import re
# Initialize databases

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def default():
    return render_template("homepage.html")
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html");
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template("logout.html");
@app.route("/home", methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html")
@app.route("/create", methods=['GET', 'POST'])
def create():
    return render_template("create.html");
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template("profile.html");
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html");

if __name__ == "__main__":
    app.debug = True
    app.run()

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


@app.context_processor
def user_context(): # persistent info made avalible for all html templates
    return {
        "logged_in": ('username' in session),
        "current_user": session.get('username')

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if 'username' in session:
        return render_template("homepage.html")
    return render_template("login.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        user = request.form['username'].strip()
        pswd = request.form['password'].strip()
        if(not user or not pswd):
            flash("WARNING: Username and Password cannot be empty!")
            return redirect(url_for('login'))
        db_user = db.get(user)
        if (db_user is None or not db.check_password(db_user)):
            redirect(url_for('login'))
        redirect(url_for('/'))
    return render_template("login.html");

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template("logout.html");
@app.route("/create", methods=['GET', 'POST'])
def create():
    return render_template("create.html");
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template("profile.html");
@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        user = request.form['username'].strip()
        pswd = request.form['password'].strip()
        if(not user or not pswd):
            flash("WARNING: Username and Password cannot be empty!")
            return redirect(url_for('register'))
        db.add_user(user,pswd)
        return redirect(url_for('login'))
    return render_template("register.html");

if __name__ == "__main__":
    app.debug = True
    app.run()

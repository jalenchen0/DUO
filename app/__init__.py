
  #Duo's To Do List
  #Roster: Ricky Lin, Jalen Chen
 # SoftDev


# Imports
from flask import Flask, render_template, request, flash, url_for, redirect, session
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import db
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
}
@app.route("/", methods=['GET', 'POST'])
def homepage():
    if 'username' not in session:
        flash("You must be logged in to view your tasks.")
        return redirect(url_for('login'))

    tasks = db.get_tasks_for_user(session['username'])
    return render_template("homepage.html", tasks=tasks)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        user = request.form['username'].strip()
        pswd = request.form['password'].strip()
        if(not user or not pswd):
            flash("WARNING: Username and Password cannot be empty!")
            return redirect(url_for('login'))
        db_user = db.get_user(user)
        if (db_user is None or not db.check_password(db_user, pswd)):
            flash("Username or password is not correct!")
            return redirect(url_for('login'))
        flash(f"Login Successful! Welcome back, {user}.")
        session['username'] = user
        return redirect(url_for('homepage'))
    return render_template("login.html")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('homepage'))

@app.route("/create", methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        flash("You must be logged in to create a task.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form.get('title').strip()
        description = request.form.get('description').strip()
        due = request.form.get('due').strip()

        if not title:
            flash("Title cannot be empty!")
            return redirect(url_for('create'))

        db.add_task(session['username'], title, description, due)
        flash("Task created successfully!")
        return redirect(url_for('homepage'))

    return render_template("create.html")
@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        user = request.form['username'].strip()
        pswd = request.form['password'].strip()
        if(not user or not pswd):
            flash("WARNING: One of the fields cannot be empty!")
            return redirect(url_for('register'))
        if db.add_user(user, pswd):
            flash(f"Registration Successful! Welcome, {user}. Please log in.")
            return redirect(url_for('login'))
        else:
            flash("Username already exists. Please choose another.")
            return redirect(url_for('register'))
        return redirect(url_for('login'))
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

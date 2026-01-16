
  #Duo's To Do List
  #Roster: Ricky Lin, Jalen Chen
 # SoftDev
import sqlite3
import os
from datetime import datetime
import json

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS accounts (username TEXT PRIMARY KEY, password TEXT);")

def add_user(username, password):
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM accounts WHERE username = ?", [username])
    cursorfetch = c.fetchone()[0]
    if cursorfetch == 1:
        db.commit()
        return False
    c.execute("INSERT INTO accounts VALUES(?, ?)", (username, password))
    c.close()
    db.commit()
    return True

def get_user(username):
    c = db.cursor()
    c.execute("SELECT * FROM accounts WHERE username = ?", [username])
    cursorfetch = c.fetchone()
    return cursorfetch

def check_password(db_user, password):
    return password == db_user[1]

def create(title, description, due):
    c = db.cursor()
    date = datetime.date
    c.execute(f"INSERT INTO {username} VALUES({title}, {description}, {date}, {due})")
    c.close()
    db.commit()

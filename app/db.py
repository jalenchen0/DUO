import sqlite3
from datetime import datetime

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        username TEXT PRIMARY KEY,
        password TEXT
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        title TEXT,
        description TEXT,
        due TEXT
    )
""")

db.commit()
c.close()

def add_user(username, password):
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM accounts WHERE username = ?", (username,))
    exists = c.fetchone()[0]
    if exists:
        c.close()
        return False
    c.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))
    db.commit()
    c.close()
    return True

def get_user(username):
    c = db.cursor()
    c.execute("SELECT * FROM accounts WHERE username = ?", (username,))
    user = c.fetchone()
    c.close()
    return user

def check_password(db_user, password):
    return db_user and db_user[1] == password

def add_task(username, title, description, due):
    c = db.cursor()
    c.execute(
        "INSERT INTO tasks (username, title, description, due) VALUES (?, ?, ?, ?)",
        (username, title, description, due)
    )
    db.commit()
    c.close()

def get_tasks_for_user(username):
    c = db.cursor()
    c.execute("SELECT id, title, description, due FROM tasks WHERE username = ?", (username,))
    tasks = c.fetchall()
    c.close()
    return tasks

def delete_task(task_id, username):
    c = db.cursor()
    c.execute("DELETE FROM tasks WHERE id = ? AND username = ?", (task_id, username))
    db.commit()
    deleted = c.rowcount > 0
    c.close()
    return deleted

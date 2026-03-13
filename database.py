import sqlite3

DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS keys(id INTEGER PRIMARY KEY, user_name TEXT, key TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, user_name TEXT, message TEXT)''')
    conn.commit()
    conn.close()
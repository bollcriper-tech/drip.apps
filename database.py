import sqlite3

DB_NAME = "database.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gmail TEXT UNIQUE,
        name TEXT,
        password TEXT,
        role TEXT DEFAULT 'user',
        balance INTEGER DEFAULT 0,
        date_registered TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user TEXT,
        to_user TEXT,
        message TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item TEXT,
        amount INTEGER,
        date TEXT DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'pending'
    )
    """)

    conn.commit()
    conn.close()

def add_user(gmail, name, password):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (gmail, name, password) VALUES (?, ?, ?)", (gmail, name, password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_user_by_gmail(gmail):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE gmail = ?", (gmail,))
    user = c.fetchone()
    conn.close()
    return user
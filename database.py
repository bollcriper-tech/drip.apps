import sqlite3

DB_NAME = "database.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # таблица пользователей
    cursor.execute("""
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

    # таблица сообщений
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user TEXT,
        to_user TEXT,
        message TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # таблица покупок
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item TEXT,
        amount INTEGER,
        status TEXT DEFAULT 'pending',
        date TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(gmail, name, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (gmail, name, password) VALUES (?, ?, ?)",
            (gmail, name, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()


def get_user_by_gmail(gmail):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE gmail = ?", (gmail,))
    user = cursor.fetchone()

    conn.close()
    return user


def update_balance(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE id = ?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def add_purchase(user_id, item, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO purchases (user_id, item, amount, status) VALUES (?, ?, ?, ?)",
        (user_id, item, amount, "paid")
    )

    conn.commit()
    conn.close()


def add_message(from_user, to_user, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (from_user, to_user, message) VALUES (?, ?, ?)",
        (from_user, to_user, message)
    )

    conn.commit()
    conn.close()


def get_messages(user1, user2):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT from_user, to_user, message, timestamp
    FROM messages
    WHERE (from_user=? AND to_user=?)
       OR (from_user=? AND to_user=?)
    ORDER BY timestamp
    """, (user1, user2, user2, user1))

    messages = cursor.fetchall()
    conn.close()

    return messages
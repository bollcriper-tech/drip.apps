import sqlite3

DB_NAME = "database.db"

def add_message(from_user, to_user, message):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO messages (from_user, to_user, message) VALUES (?, ?, ?)",
              (from_user, to_user, message))
    conn.commit()
    conn.close()

def get_messages(user1, user2):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT from_user, to_user, message, timestamp FROM messages
        WHERE (from_user=? AND to_user=?) OR (from_user=? AND to_user=?)
        ORDER BY timestamp
    """, (user1, user2, user2, user1))
    messages = c.fetchall()
    conn.close()
    return messages
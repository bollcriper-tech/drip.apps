import flet as ft
import sqlite3

DB = "database.db"

def ChatPage(page, user):

    messages_col = ft.Column()

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, user_name TEXT, message TEXT)")
    conn.commit()
    msgs = cur.execute("SELECT user_name, message FROM messages").fetchall()
    conn.close()

    for m in msgs:
        messages_col.controls.append(ft.Text(f"{m[0]}: {m[1]}"))

    input_field = ft.TextField(label="Введите сообщение")

    def send_message(e):
        msg = input_field.value.strip()
        if not msg:
            return
        messages_col.controls.append(ft.Text(f"{user['name'] or 'Вы'}: {msg}"))
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("INSERT INTO messages(user_name,message) VALUES(?,?)",(user['name'] or "Вы",msg))
        conn.commit()
        conn.close()
        input_field.value = ""
        page.update()

    send_button = ft.ElevatedButton("Отправить", on_click=send_message)

    return ft.Column([ft.Text("Чат с админом", size=25), messages_col, input_field, send_button])
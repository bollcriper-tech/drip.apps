import flet as ft
import sqlite3

DB = "database.db"

def ProfilePage(page, user):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    name_text = ft.Text(f"Имя: {user['name']}")
    email_text = ft.Text(f"Email: {user['email']}")

    keys_text = ft.Column([ft.Text(f"Ключ: {k}") for k in user.get("keys", [])])

    return ft.Column([
        ft.Text("Профиль", size=25),
        name_text,
        email_text,
        ft.Text("Купленные ключи:"),
        keys_text
    ])
import flet as ft
import sqlite3

def open_profile(page: ft.Page, container: ft.Column, gmail):
    container.controls.clear()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT name, role, balance FROM users WHERE gmail = ?", (gmail,))
    user = c.fetchone()
    conn.close()
    if not user:
        container.controls.append(ft.Text("User not found"))
        page.update()
        return

    name, role, balance = user
    container.controls.append(ft.Text(f"Name: {name}"))
    container.controls.append(ft.Text(f"Role: {role}"))
    container.controls.append(ft.Text(f"Balance: {balance}"))
    page.update()
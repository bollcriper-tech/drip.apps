import flet as ft
import sqlite3

def open_admin(page: ft.Page, container: ft.Column):
    container.controls.clear()
    container.controls.append(ft.Text("Admin Panel", size=24, weight="bold"))

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT id, name, role, balance FROM users")
    users = c.fetchall()
    conn.close()

    def update_balance(user_id, delta):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (delta, user_id))
        conn.commit()
        conn.close()
        open_admin(page, container)
        page.snack_bar = ft.SnackBar(ft.Text(f"Balance updated for user {user_id}"))
        page.snack_bar.open = True
        page.update()

    for u in users:
        user_id, name, role, balance = u
        user_row = ft.Row([
            ft.Text(f"{name} - {role} - Balance: {balance}"),
            ft.ElevatedButton("+100", on_click=lambda e, uid=user_id: update_balance(uid, 100)),
            ft.ElevatedButton("-100", on_click=lambda e, uid=user_id: update_balance(uid, -100)),
        ])
        container.controls.append(user_row)

    page.update()
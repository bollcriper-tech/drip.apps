import flet as ft
import sqlite3
from database import DB

def GoogleAuth(page, user, callback):
    email_input = ft.TextField(label="Введите ваш Gmail")
    name_input = ft.TextField(label="Введите Имя и Фамилия (Пример: Иван.И)")

    def login(ev):
        email = email_input.value.strip()
        name = name_input.value.strip()
        if not email or not name:
            page.snack_bar = ft.SnackBar(ft.Text("Введите email и имя!"))
            page.snack_bar.open = True
            page.update()
            return

        # сохраняем в базу данных
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(?,?)", (name,email))
        conn.commit()
        conn.close()

        # обновляем пользователя в приложении
        user["name"] = name
        user["email"] = email

        page.snack_bar = ft.SnackBar(ft.Text(f"Вы вошли как {name}"))
        page.snack_bar.open = True
        page.update()

        # вызываем колбэк для возврата на главный экран
        callback()

    dialog = ft.AlertDialog(
        title=ft.Text("Вход через Google (демо)"),
        content=ft.Column([email_input, name_input]),
        actions=[ft.ElevatedButton("Войти", on_click=login)]
    )

    page.dialog = dialog
    dialog.open = True
    page.update()
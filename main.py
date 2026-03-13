import flet as ft
import os
import traceback

# Локальные файлы внутри папки приложения (самый надежный способ)
LOG_FILE = "drip_debug_log.txt"
USERS_FILE = "drip_users.txt"

def write_to_file(path, text):
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except:
        pass

def main(page: ft.Page):
    page.title = "DRIP SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    write_to_file(LOG_FILE, "--- APP STARTED ---")

    user_input = ft.TextField(label="Username", border_color="#00FF00", width=300)
    pass_input = ft.TextField(label="Password", password=True, border_color="#00FF00", width=300)

    # Регистрация
    def do_register(e):
        u, p = user_input.value, pass_input.value
        if u and p:
            write_to_file(USERS_FILE, f"{u}:{p}")
            write_to_file(LOG_FILE, f"User {u} registered.")
            page.snack_bar = ft.SnackBar(ft.Text("Регистрация успешна!"), bgcolor="green")
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Заполните поля!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # Вход
    def do_login(e):
        u, p = user_input.value, pass_input.value
        write_to_file(LOG_FILE, f"Login attempt: {u}")
        try:
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, "r") as f:
                    data = f.read()
                if f"{u}:{p}" in data:
                    page.clean()
                    page.add(
                        ft.Text(f"ДОБРО ПОЖАЛОВАТЬ, {u}!", size=30, color="#00FF00", weight="bold"),
                        ft.Text("СИСТЕМА АКТИВИРОВАНА", color="#555555"),
                        ft.ElevatedButton("ВЫЙТИ", on_click=lambda _: main(page))
                    )
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("Неверный логин или пароль!"), bgcolor="red")
                    page.snack_bar.open = True
            else:
                page.snack_bar = ft.SnackBar(ft.Text("База пуста! Зарегистрируйтесь."), bgcolor="orange")
                page.snack_bar.open = True
        except Exception:
            write_to_file(LOG_FILE, traceback.format_exc())
        page.update()

    # Главный экран
    page.clean()
    page.add(
        ft.Text("DRIP CLIENT", size=35, weight="bold", color="#00FF00"),
        ft.Container(height=20),
        user_input,
        pass_input,
        ft.Container(height=10),
        ft.Row([
            ft.ElevatedButton("LOG IN", on_click=do_login, bgcolor="#00FF00", color="black"),
            ft.OutlinedButton("REGISTER", on_click=do_register, border_color="#00FF00")
        ], alignment="center")
    )
    page.update()

try:
    ft.app(target=main)
except Exception:
    write_to_file(LOG_FILE, traceback.format_exc())
import flet as ft
import os
import traceback

# Пути к файлам в памяти телефона
USERS_FILE = "/storage/emulated/0/drip_users.txt"
LOG_FILE = "/storage/emulated/0/drip_debug_log.txt"

def write_log(text):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except: pass

def main(page: ft.Page):
    page.title = "DRIP CLIENT"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_msg(text, color="white"):
        page.snack_bar = ft.SnackBar(ft.Text(text), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    # --- ЛОГИКА РЕГИСТРАЦИИ ---
    def register_user(e):
        u = user_input.value
        p = pass_input.value
        if u and p:
            try:
                with open(USERS_FILE, "a") as f:
                    f.write(f"{u}:{p}\n")
                write_log(f"New user registered: {u}")
                show_msg("Регистрация успешна! Теперь войдите.", "green")
            except Exception as ex:
                write_log(f"Reg error: {traceback.format_exc()}")
                show_msg("Ошибка доступа к памяти!", "red")
        else:
            show_msg("Заполните все поля!")

    # --- ЛОГИКА ВХОДА ---
    def login_user(e):
        u = user_input.value
        p = pass_input.value
        write_log(f"Login attempt: {u}")
        try:
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, "r") as f:
                    users = f.readlines()
                if f"{u}:{p}\n" in users:
                    write_log("Login success!")
                    page.clean()
                    page.add(ft.Text(f"WELCOME, {u}!", size=30, color="#00FF00"))
                    page.update()
                else:
                    show_msg("Неверный логин или пароль", "red")
            else:
                show_msg("Пользователей еще нет. Зарегистрируйтесь!")
        except Exception as ex:
            write_log(f"Login error: {traceback.format_exc()}")

    # --- ИНТЕРФЕЙС ---
    user_input = ft.TextField(label="Username", border_color="#00FF00", width=300)
    pass_input = ft.TextField(label="Password", password=True, border_color="#00FF00", width=300)

    page.add(
        ft.Text("DRIP SYSTEM", size=30, weight="bold", color="#00FF00"),
        ft.Container(height=20),
        user_input,
        pass_input,
        ft.Container(height=10),
        ft.Row([
            ft.ElevatedButton("LOG IN", on_click=login_user, bgcolor="#00FF00", color="black"),
            ft.OutlinedButton("REGISTER", on_click=register_user, border_color="#00FF00"),
        ], alignment="center"),
        ft.Text(f"Logs: {LOG_FILE}", size=10, color="grey")
    )
    
    write_log("UI Loaded")
    page.update()

# Запуск
try:
    ft.app(target=main)
except Exception:
    write_log(f"App Crash: {traceback.format_exc()}")

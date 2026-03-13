import flet as ft
import os
import traceback

# Пути к файлам в памяти телефона (стандартный путь Android)
LOG_FILE = "/storage/emulated/0/drip_debug_log.txt"
USERS_FILE = "/storage/emulated/0/drip_users.txt"

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

    write_to_file(LOG_FILE, "--- APP INITIALIZED ---")

    # Поля ввода
    user_input = ft.TextField(label="Username", border_color="#00FF00", width=300)
    pass_input = ft.TextField(label="Password", password=True, can_reveal_password=True, border_color="#00FF00", width=300)

    # Функция регистрации
    def do_register(e):
        u, p = user_input.value, pass_input.value
        if u and p:
            write_to_file(USERS_FILE, f"{u}:{p}")
            write_to_file(LOG_FILE, f"User {u} registered.")
            page.snack_bar = ft.SnackBar(ft.Text("Регистрация успешна!"), bgcolor="green")
            page.snack_bar.open = True
            page.update()
        else:
            write_to_file(LOG_FILE, "Registration failed: empty fields")

    # Функция входа
    def do_login(e):
        u, p = user_input.value, pass_input.value
        write_to_file(LOG_FILE, f"Login attempt for: {u}")
        try:
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, "r") as f:
                    data = f.read()
                if f"{u}:{p}" in data:
                    write_to_file(LOG_FILE, "Login SUCCESS")
                    page.clean()
                    page.add(ft.Text(f"ДОБРО ПОЖАЛОВАТЬ, {u}!", size=30, color="#00FF00"))
                else:
                    write_to_file(LOG_FILE, "Login FAILED: wrong credentials")
            else:
                write_to_file(LOG_FILE, "Login FAILED: users.txt not found")
        except Exception:
            write_to_file(LOG_FILE, f"CRITICAL ERROR: {traceback.format_exc()}")

    # Интерфейс
    page.add(
        ft.Text("DRIP CLIENT", size=35, weight="bold", color="#00FF00"),
        ft.Text("REGISTRATION & LOGIN SYSTEM", color="#555555"),
        ft.Container(height=20),
        user_input,
        pass_input,
        ft.Container(height=10),
        ft.Row([
            ft.ElevatedButton("LOG IN", on_click=do_login, bgcolor="#00FF00", color="black"),
            ft.OutlinedButton("REGISTER", on_click=do_register, border_color="#00FF00")
        ], alignment="center"),
        ft.Text(f"Debug file: {LOG_FILE}", size=10, color="grey")
    )
    page.update()

# Запуск с отловом самых ранних ошибок
try:
    ft.app(target=main)
except Exception:
    write_to_file(LOG_FILE, f"BOOT ERROR: {traceback.format_exc()}")

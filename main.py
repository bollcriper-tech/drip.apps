import flet as ft
import sqlite3
from utils.theme_manager import set_theme
from chat_list import open_chat_list
from shop import open_shop
from settings import open_settings
from admin import open_admin

# ---------- AUTH ----------
def open_auth(page: ft.Page, on_success):
    email = ft.TextField(label="Gmail (English only)")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    name = ft.TextField(label="Name (English only)")

    theme_mode = "dark"

    def toggle_theme(e):
        nonlocal theme_mode
        theme_mode = "light" if theme_mode == "dark" else "dark"
        set_theme(page, theme_mode)
        page.update()

    theme_btn = ft.ElevatedButton("Toggle Theme", on_click=toggle_theme)

    def login_click(e):
        if not email.value or not password.value or not name.value:
            page.snack_bar = ft.SnackBar(ft.Text("Fill all fields!"))
            page.snack_bar.open = True
            page.update()
            return

        # Сохраняем в базу
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (gmail, name, password) VALUES (?, ?, ?)",
                      (email.value, name.value, password.value))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        conn.close()

        panel.visible = False
        on_success()
        page.update()

    panel = ft.Container(
        content=ft.Column([
            ft.Text("DRIP CLIENT LOGIN", size=28, weight="bold"),
            email,
            password,
            name,
            theme_btn,
            ft.ElevatedButton("Login / Register", on_click=login_click)
        ]),
        padding=30,
        bgcolor="#111111",
        border_radius=20,
        width=350,
        alignment=ft.alignment.center,
        top=50,
        left=25,
    )

    page.add(panel)
    page.update()

# ---------- MAIN APP ----------
def main(page: ft.Page):
    page.title = "DRIP CLIENT"
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.START
    set_theme(page, "dark")

    main_content = ft.Column(expand=True)

    # ---------- BURGER MENU ----------
    drawer = ft.Drawer(
        content=ft.Column([
            ft.ListTile(ft.icons.HOME, "Home", on_click=lambda e: open_screen("home")),
            ft.ListTile(ft.icons.CHAT, "Chats", on_click=lambda e: open_screen("chat")),
            ft.ListTile(ft.icons.SHOP, "Shop", on_click=lambda e: open_screen("shop")),
            ft.ListTile(ft.icons.ADMIN_PANEL_SETTINGS, "Admin", on_click=lambda e: open_screen("admin")),
            ft.ListTile(ft.icons.SETTINGS, "Settings", on_click=lambda e: open_screen("settings")),
        ])
    )

    def open_screen(screen):
        main_content.controls.clear()
        if screen == "home":
            main_content.controls.append(ft.Text("Welcome to DRIP CLIENT!", size=20))
        elif screen == "chat":
            open_chat_list(page, main_content)
        elif screen == "shop":
            open_shop(page, main_content)
        elif screen == "admin":
            open_admin(page, main_content)
        elif screen == "settings":
            open_settings(page, main_content)
        page.update()
        page.drawer.open = False

    page.drawer = drawer

    burger_btn = ft.IconButton(ft.icons.MENU, on_click=lambda e: page.drawer.open = not page.drawer.open)

    top_bar = ft.Row([burger_btn, ft.Text("DRIP CLIENT", size=24, weight="bold")],
                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN, height=50, bgcolor="#111111", padding=10)

    def open_home():
        main_content.controls.clear()
        main_content.controls.append(ft.Text("Welcome! This is the main screen.", size=20))
        page.update()

    open_auth(page, on_success=open_home)

    page.add(
        top_bar,
        main_content
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
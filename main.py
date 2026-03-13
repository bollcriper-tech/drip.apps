import flet as ft
from database import create_tables
from chat_list import open_chat_list
from shop import open_shop
from settings import open_settings
from admin import open_admin


def main(page: ft.Page):
    # создаём таблицы базы
    create_tables()

    page.title = "DRIP CLIENT"
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#000000"

    main_content = ft.Column(expand=True)

    # ---------- BURGER MENU ----------
    def open_screen(screen):
        main_content.controls.clear()

        if screen == "home":
            main_content.controls.append(
                ft.Text("Welcome to DRIP CLIENT!", size=20, color="green")
            )

        elif screen == "chat":
            open_chat_list(page, main_content)

        elif screen == "shop":
            open_shop(page, main_content)

        elif screen == "admin":
            open_admin(page, main_content)

        elif screen == "settings":
            open_settings(page, main_content)

        page.drawer.open = False
        page.update()

    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=20),
            ft.ListTile(title=ft.Text("Home"), leading=ft.Icon(ft.icons.HOME),
                        on_click=lambda e: open_screen("home")),
            ft.ListTile(title=ft.Text("Chats"), leading=ft.Icon(ft.icons.CHAT),
                        on_click=lambda e: open_screen("chat")),
            ft.ListTile(title=ft.Text("Shop"), leading=ft.Icon(ft.icons.SHOP),
                        on_click=lambda e: open_screen("shop")),
            ft.ListTile(title=ft.Text("Admin"), leading=ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS),
                        on_click=lambda e: open_screen("admin")),
            ft.ListTile(title=ft.Text("Settings"), leading=ft.Icon(ft.icons.SETTINGS),
                        on_click=lambda e: open_screen("settings")),
        ],
    )

    page.drawer = drawer

    # ---------- BURGER BUTTON ----------
    def toggle_drawer(e):
        page.drawer.open = not page.drawer.open
        page.update()

    burger_btn = ft.IconButton(
        icon=ft.icons.MENU,
        icon_color="green",
        on_click=toggle_drawer
    )

    top_bar = ft.Container(
        content=ft.Row(
            [
                burger_btn,
                ft.Text("DRIP CLIENT", size=22, weight="bold", color="green"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor="#111111",
        padding=10
    )

    # ---------- LOGIN PANEL ----------
    email = ft.TextField(label="Gmail", color="green")
    password = ft.TextField(label="Password", password=True, color="green")
    name = ft.TextField(label="Name", color="green")

    def login_click(e):
        if not email.value or not password.value or not name.value:
            page.snack_bar = ft.SnackBar(ft.Text("Fill all fields"))
            page.snack_bar.open = True
            page.update()
            return

        login_panel.visible = False
        main_content.controls.append(
            ft.Text(f"Welcome {name.value}!", size=20, color="green")
        )
        page.update()

    login_panel = ft.Container(
        content=ft.Column(
            [
                ft.Text("LOGIN", size=28, weight="bold", color="green"),
                email,
                password,
                name,
                ft.ElevatedButton("Login / Register", on_click=login_click)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=30,
        bgcolor="#111111",
        border_radius=20,
        width=350,
        alignment=ft.alignment.center
    )

    page.add(
        top_bar,
        login_panel,
        main_content
    )


ft.app(target=main)
import flet as ft
from database import init_db
from profile import ProfilePage
from shop import ShopPage
from settings import SettingsPage
from chat import ChatPage

def main(page: ft.Page):
    init_db()
    user = {"name":"", "email":"demo@demo.com", "keys":[]}  # Демо-пользователь

    def open_shop(e):
        page.clean()
        page.add(ShopPage(page, user))

    def open_profile(e):
        page.clean()
        page.add(ProfilePage(page, user))

    def open_settings(e):
        page.clean()
        page.add(SettingsPage(page, user))

    def open_chat(e):
        page.clean()
        page.add(ChatPage(page, user))

    page.title = "DRIP CLIENT MOBILE PRO"
    page.add(
        ft.Column([
            ft.Text("DRIP CLIENT MOBILE PRO", size=30, color="green"),
            ft.ElevatedButton("Профиль", on_click=open_profile),
            ft.ElevatedButton("Магазин", on_click=open_shop),
            ft.ElevatedButton("Настройки", on_click=open_settings),
            ft.ElevatedButton("Чат с админом", on_click=open_chat),
        ])
    )

ft.app(target=main)
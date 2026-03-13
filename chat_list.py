import flet as ft
from chat_room import open_chat_room

CHATS = [
    {"name": "Admin", "last_message": "Welcome!", "avatar": "A"},
    {"name": "Support", "last_message": "How can I help?", "avatar": "S"},
    {"name": "Shop", "last_message": "Check new items", "avatar": "🛒"},
]

def open_chat_list(page: ft.Page, container: ft.Column):
    container.controls.clear()
    container.controls.append(ft.Text("Chats", size=24, weight="bold"))

    for chat in CHATS:
        chat_btn = ft.ListTile(
            leading=ft.CircleAvatar(content=ft.Text(chat["avatar"])),
            title=ft.Text(chat["name"]),
            subtitle=ft.Text(chat["last_message"]),
            on_click=lambda e, c=chat: open_chat_room(page, container, c)
        )
        container.controls.append(chat_btn)

    page.update()
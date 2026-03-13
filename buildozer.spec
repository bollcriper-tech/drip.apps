import flet as ft
import time
import os

def main(page: ft.Page):
    page.title = "DRIP CLIENT MOBILE"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_bgcolor = "#000000"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Text(
        value="DRIP CLIENT",
        size=40,
        color="#00FF00",
        weight=ft.FontWeight.BOLD,
        italic=True,
        shadow=ft.BoxShadow(blur_radius=10, color="#00FF00")
    )

    status_text = ft.Text("System: IDLE", color="#555555", size=14)
    progress_bar = ft.ProgressBar(width=300, color="#00FF00", bgcolor="#111111", visible=False)

    def start_inject(e):
        inject_btn.disabled = True
        progress_bar.visible = True
        status_text.value = "STATUS: INITIALIZING..."
        page.update()

        steps = ["LOADING ASSETS...", "BYPASSING...", "DRIP ACTIVE!"]
        for step in steps:
            time.sleep(1)
            status_text.value = f"STATUS: {step}"
            page.update()

        inject_btn.text = "CONNECTED"
        inject_btn.bgcolor = "#004400"
        page.update()

    inject_btn = ft.ElevatedButton(
        text="START SESSION",
        width=250,
        height=50,
        color="#00FF00",
        bgcolor="#111111",
        on_click=start_inject,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(2, "#00FF00")
        )
    )

    page.add(
        ft.Column(
            [
                ft.Container(height=50),
                logo,
                ft.Text("MOBILE EDITION v1.0", color="#00FF00", size=12),
                ft.Container(height=100),
                status_text,
                progress_bar,
                inject_btn,
                ft.Container(height=20),
                ft.TextButton("FF MARKET ACCESS", icon=ft.icons.SHOPPING_CART, icon_color="#00FF00"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

import flet as ft
from utils.theme_manager import set_theme

def open_settings(page: ft.Page, container: ft.Column):
    container.controls.clear()
    theme_mode = "dark"
    theme_text = ft.Text(f"Theme: {theme_mode}")

    def toggle_theme(e):
        nonlocal theme_mode
        theme_mode = "light" if theme_mode == "dark" else "dark"
        set_theme(page, theme_mode)
        theme_text.value = f"Theme: {theme_mode}"
        page.update()

    theme_btn = ft.ElevatedButton("Toggle Theme", on_click=toggle_theme)

    container.controls.append(ft.Column([
        ft.Text("Settings", size=24, weight="bold"),
        ft.Row([theme_text, theme_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    ]))
    page.update()
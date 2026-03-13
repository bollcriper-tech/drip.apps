import flet as ft

def set_theme(page: ft.Page, theme_mode="dark"):
    if theme_mode == "dark":
        page.bgcolor = "#000000"
        page.update()
    else:
        page.bgcolor = "#FFFFFF"
        page.update()

import flet as ft
import asyncio

async def main(page: ft.Page):
    page.title = "DRIP CLIENT MOBILE"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Text(
        "DRIP CLIENT",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#00FF00"
    )

    status = ft.Text("STATUS: IDLE", color="#777777")
    progress = ft.ProgressBar(width=300, visible=False)

    async def start_session(e):
        button.disabled = True
        progress.visible = True
        page.update()

        steps = ["INITIALIZING...", "LOADING MODULES...", "CONNECTING...", "SESSION STARTED"]
        for s in steps:
            status.value = f"STATUS: {s}"
            page.update()
            await asyncio.sleep(1)

        button.text = "CONNECTED"
        page.update()

    button = ft.ElevatedButton(
        "START SESSION",
        width=250,
        height=50,
        on_click=start_session,
        style=ft.ButtonStyle(color="#00FF00", bgcolor="#111111")
    )

    page.add(
        ft.Column(
            [
                logo,
                ft.Text("MOBILE EDITION v1.0", size=12, color="#00FF00"),
                ft.Container(height=50),
                status,
                progress,
                button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
    

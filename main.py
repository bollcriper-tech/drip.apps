import flet as ft
import asyncio

async def main(page: ft.Page):
    page.title = "DRIP CLIENT MOBILE"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Делаем на весь экран
    page.window_full_screen = True

    # --- ФУНКЦИЯ ПЕРЕХОДА В ГЛАВНОЕ МЕНЮ ---
    async def open_dashboard(e):
        page.clean() # Очищаем страницу логина
        
        # Логотип и статус
        logo = ft.Text("DRIP CLIENT", size=40, weight="bold", color="#00FF00")
        status = ft.Text("STATUS: AUTHORIZED", color="#00FF00", size=14)
        progress = ft.ProgressBar(width=300, visible=False, color="#00FF00")

        async def start_session(e):
            btn.disabled = True
            progress.visible = True
            page.update()
            steps = ["BYPASSING...", "INJECTING...", "ACTIVE!"]
            for s in steps:
                status.value = f"STATUS: {s}"
                page.update()
                await asyncio.sleep(1)
            btn.text = "READY"
            page.update()

        btn = ft.ElevatedButton("START INJECT", on_click=start_session, width=250, color="#00FF00")

        page.add(
            ft.Column([
                logo,
                status,
                progress,
                btn,
                ft.TextButton("LOGOUT", on_click=lambda _: main(page))
            ], horizontal_alignment="center", spacing=30)
        )
        page.update()

    # --- СТРАНИЦА ЛОГИНА ---
    login_card = ft.Container(
        content=ft.Column([
            ft.Text("AUTHORIZATION", size=25, weight="bold", color="#00FF00"),
            ft.TextField(label="Login", border_color="#00FF00", color="#00FF00"),
            ft.TextField(label="Password", password=True, can_reveal_password=True, border_color="#00FF00"),
            
            ft.ElevatedButton(
                "LOGIN", 
                width=200, 
                bgcolor="#00FF00", 
                color="black",
                on_click=open_dashboard
            ),
            
            ft.Divider(color="#333333"),
            
            # Кнопка Google (имитация)
            ft.OutlinedButton(
                content=ft.Row([
                    ft.Icon(ft.icons.GOOGLEG_LOG_IN, color="white"),
                    ft.Text("Login with Google", color="white"),
                ], alignment="center"),
                width=200,
                on_click=open_dashboard # Пока просто вход
            ),
        ], horizontal_alignment="center", spacing=20),
        padding=30,
        border=ft.border.all(1, "#00FF00"),
        border_radius=15,
        bgcolor="#111111"
    )

    page.clean()
    page.add(login_card)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
    

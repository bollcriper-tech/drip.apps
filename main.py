import flet as ft
import time

def main(page: ft.Page):
    page.title = "DRIP CLIENT"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40

    # -------------------- Загрузочный экран --------------------
    loading_text = ft.Text("SYSTEM BOOT...", size=28, color="#00FF00", weight="bold")
    page.add(loading_text)
    page.update()
    time.sleep(1.2)  # имитация загрузки
    page.controls.clear()
    page.update()

    # -------------------- Функция авторизации --------------------
    def login_click(e):
        if not user_field.value or not pass_field.value:
            if not user_field.value:
                user_field.error_text = "Введите логин"
            else:
                user_field.error_text = None
            if not pass_field.value:
                pass_field.error_text = "Введите пароль"
            else:
                pass_field.error_text = None
            page.update()
        else:
            page.controls.clear()
            welcome_text = ft.Text("WELCOME, DRIPPER!", size=30, color="#00FF00", weight="bold")
            system_text = ft.Text("SYSTEM ACTIVE", color="#555555")
            back_btn = ft.ElevatedButton(
                "BACK",
                bgcolor="#00FF00",
                color="#000000",
                on_click=lambda _: main(page)
            )

            # Анимация появления
            page.add(ft.Column([welcome_text, system_text, back_btn], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, opacity=0))
            for c in page.controls:
                c.opacity = 1
                page.update()
            page.update()

    # -------------------- Элементы авторизации --------------------
    title = ft.Text("AUTHORIZATION", size=32, color="#00FF00", weight="bold", opacity=0)
    user_field = ft.TextField(
        label="Username",
        border_color="#00FF00",
        color="#00FF00",
        focused_border_color="#FFFFFF",
        width=300,
        opacity=0
    )
    pass_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        border_color="#00FF00",
        color="#00FF00",
        focused_border_color="#FFFFFF",
        width=300,
        opacity=0
    )
    login_btn = ft.ElevatedButton(
        text="LOG IN",
        width=300,
        height=50,
        bgcolor="#00FF00",
        color="#000000",
        on_click=login_click,
        opacity=0
    )
    version_text = ft.Text("v1.2 STABLE", size=10, color="#333333", opacity=0)

    # -------------------- Добавляем элементы на страницу --------------------
    auth_column = ft.Column(
        [
            title,
            ft.Container(height=20),
            user_field,
            pass_field,
            ft.Container(height=10),
            login_btn,
            version_text
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    page.add(auth_column)
    page.update()

    # -------------------- Анимация появления --------------------
    for control in auth_column.controls:
        control.opacity = 1
        page.update()
        time.sleep(0.05)  # лёгкая анимация появления

# -------------------- Запуск приложения --------------------
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
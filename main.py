import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "DRIP CLIENT"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40

    # Функция перехода (чтобы проверить, что кнопки работают)
    def login_click(e):
        if not user_field.value or not pass_field.value:
            user_field.error_text = "Введите логин"
            pass_field.error_text = "Введите пароль"
            page.update()
        else:
            page.controls.clear()
            page.add(
                ft.Text("WELCOME, DRIPPER!", size=30, color="#00FF00", weight="bold"),
                ft.Text("SYSTEM ACTIVE", color="#555555"),
                ft.ElevatedButton("BACK", on_click=lambda _: main(page))
            )
            page.update()

    # Элементы интерфейса
    title = ft.Text("AUTHORIZATION", size=28, color="#00FF00", weight="bold")
    
    user_field = ft.TextField(
        label="Username",
        border_color="#00FF00",
        color="#00FF00",
        focused_border_color="#FFFFFF",
        width=300
    )
    
    pass_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        border_color="#00FF00",
        color="#00FF00",
        focused_border_color="#FFFFFF",
        width=300
    )

    login_btn = ft.ElevatedButton(
        text="LOG IN",
        width=300,
        height=50,
        bgcolor="#00FF00",
        color="#000000",
        on_click=login_click
    )

    # Собираем страницу
    page.add(
        ft.Column(
            [
                title,
                ft.Container(height=20),
                user_field,
                pass_field,
                ft.Container(height=10),
                login_btn,
                ft.Text("v1.2 STABLE", size=10, color="#333333")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )
    page.update()

# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)

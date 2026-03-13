import flet as ft

def SettingsPage(page, user):
    gmail_input = ft.TextField(label="Ваш Gmail", value=user.get("email",""))
    theme_switch = ft.Switch(label="Хакерская тема")

    result_text = ft.Text()

    def save(e):
        user["email"] = gmail_input.value
        result_text.value = f"Gmail сохранён: {user['email']}"
        page.update()

    return ft.Column([
        ft.Text("Настройки", size=25),
        gmail_input,
        theme_switch,
        ft.ElevatedButton("Сохранить", on_click=save),
        result_text
    ])
import flet as ft
import sqlite3, random, string

DB = "database.db"

def ShopPage(page, user):

    def buy_key(e):
        name_input = ft.TextField(label="Имя и Фамилия (Пример: Иван.И)")

        def paid(ev):
            user_name = name_input.value.strip()
            if not user_name:
                warning = ft.AlertDialog(title=ft.Text("Ошибка"),
                                         content=ft.Text("Введите Имя и Фамилию!"),
                                         actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(e))])
                page.dialog = warning
                warning.open = True
                page.update()
                return

            key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            user["keys"].append(key)

            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            cur.execute("INSERT INTO keys(user_name, key) VALUES(?,?)",(user_name,key))
            conn.commit()
            conn.close()

            dialog = ft.AlertDialog(title=ft.Text("Спасибо!"),
                                    content=ft.Text(f"Ваш ключ: {key}"),
                                    actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(e))])
            page.dialog = dialog
            dialog.open = True
            page.update()

        def close_dialog(ev):
            page.dialog.open = False
            page.update()

        dialog = ft.AlertDialog(title=ft.Text("Покупка ключа"),
                                content=ft.Column([
                                    ft.Text("Цена: 500₸"),
                                    ft.Text("Kaspi карта: 4400 1234 5678 9999"),
                                    name_input,
                                    ft.Text("После перевода нажмите кнопку 'Я оплатил'")
                                ]),
                                actions=[ft.ElevatedButton("Я оплатил", on_click=paid)]
                                )
        page.dialog = dialog
        dialog.open = True
        page.update()

    return ft.Column([
        ft.Text("Магазин ключей", size=25),
        ft.ElevatedButton("Купить ключ", on_click=buy_key)
    ])
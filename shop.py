import flet as ft
import sqlite3
from chat_room import open_chat_room

SHOP_ITEMS = [
    {"name": "VIP Key", "price": 500},
    {"name": "Premium Key", "price": 1000},
]

def open_shop(page: ft.Page, container: ft.Column):
    container.controls.clear()
    container.controls.append(ft.Text("Shop", size=24, weight="bold"))

    cart = []
    items_column = ft.Column()

    def add_to_cart(e, item):
        cart.append(item)
        page.snack_bar = ft.SnackBar(ft.Text(f"Added {item['name']} to cart"))
        page.snack_bar.open = True
        page.update()

    for item in SHOP_ITEMS:
        item_row = ft.Row([
            ft.Text(f"{item['name']} - {item['price']}"),
            ft.ElevatedButton("Add to cart", on_click=lambda e, i=item: add_to_cart(e, i))
        ])
        items_column.controls.append(item_row)

    gmail_field = ft.TextField(label="Your Gmail")
    kaspi_amount = ft.TextField(label="Amount to top-up (Kaspi)", value="0")

    def checkout(e):
        if not cart and int(kaspi_amount.value) <= 0:
            page.snack_bar = ft.SnackBar(ft.Text("Cart empty or amount is zero"))
            page.snack_bar.open = True
            page.update()
            return

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        if int(kaspi_amount.value) > 0:
            c.execute("UPDATE users SET balance = balance + ? WHERE gmail = ?", (int(kaspi_amount.value), gmail_field.value))
            conn.commit()
            page.snack_bar = ft.SnackBar(ft.Text(f"Balance topped up {kaspi_amount.value}"))
            page.snack_bar.open = True
            page.update()

        for item in cart:
            c.execute("SELECT balance, id FROM users WHERE gmail = ?", (gmail_field.value,))
            user = c.fetchone()
            if not user:
                page.snack_bar = ft.SnackBar(ft.Text("User not found!"))
                page.snack_bar.open = True
                page.update()
                continue

            balance, user_id = user
            if balance >= item["price"]:
                new_balance = balance - item["price"]
                c.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
                c.execute("INSERT INTO purchases (user_id, item, amount, status) VALUES (?, ?, ?, ?)",
                          (user_id, item["name"], item["price"], "paid"))
                conn.commit()
                page.snack_bar = ft.SnackBar(ft.Text(f"{item['name']} purchased! Balance left: {new_balance}"))
                page.snack_bar.open = True
                page.update()
                open_chat_room(page, container, {"name": "Admin", "last_message": f"You bought {item['name']}", "avatar": "A"})
            else:
                page.snack_bar = ft.SnackBar(ft.Text(f"Not enough balance for {item['name']}"))
                page.snack_bar.open = True
                page.update()

        cart.clear()
        conn.close()

    checkout_btn = ft.ElevatedButton("Checkout / Pay", on_click=checkout)

    container.controls.append(ft.Column([
        items_column,
        ft.Row([gmail_field, kaspi_amount], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        checkout_btn
    ]))
    page.update()
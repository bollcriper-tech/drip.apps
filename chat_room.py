import flet as ft

def open_chat_room(page: ft.Page, container: ft.Column, chat):
    container.controls.clear()
    container.controls.append(ft.Text(f"Chat with {chat['name']}", size=24, weight="bold"))

    messages_column = ft.Column(expand=True, scroll="always")
    messages_column.controls.append(ft.Row([ft.Text(f"{chat['name']}: {chat['last_message']}")]))

    msg_input = ft.TextField(expand=True, hint_text="Type a message")

    def send_msg(e):
        if msg_input.value.strip() == "":
            return
        messages_column.controls.append(ft.Row([ft.Spacer(), ft.Text(msg_input.value)]))
        messages_column.controls.append(ft.Row([ft.Text(f"{chat['name']}: We will check your payment 👍")]))
        msg_input.value = ""
        page.update()

    send_btn = ft.IconButton(ft.icons.SEND, on_click=send_msg)

    container.controls.append(messages_column)
    container.controls.append(ft.Row([msg_input, send_btn]))
    page.update()
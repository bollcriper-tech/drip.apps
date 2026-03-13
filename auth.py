from database import add_user, get_user_by_gmail

def register_user(gmail, name, password):
    if get_user_by_gmail(gmail):
        return False  # пользователь уже существует
    add_user(gmail, name, password)
    return True

def login_user(gmail, password):
    user = get_user_by_gmail(gmail)
    if not user:
        return None
    if user[3] == password:  # password в 4-й колонке
        return user
    return None
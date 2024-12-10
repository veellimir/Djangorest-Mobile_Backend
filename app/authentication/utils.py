import re


def validate_username(username: str) -> None:
    if not re.match(r"[a-zA-Z0-9_.-]{4,30}$", username):
        raise ValueError(
            "Имя пользователя должно содержать только буквы, цифры, "
            "точки, дефисы или подчеркивания и быть длиной от 4 до 20 символов."
        )


def validate_password():
    pass
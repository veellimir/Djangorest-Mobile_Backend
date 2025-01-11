from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


EXCEPTION_USER_NOT_FOUND = Response(
    {"detail": "Неверный логин или пароль"},
    status=status.HTTP_404_NOT_FOUND
)

EXCEPTION_USER_PASSWORD = Response(
    {"error": "Неверный текущий пароль, или новый пароль не совпадает"},
    status=status.HTTP_400_BAD_REQUEST
)

EXCEPTION_USER_EMAIL = Response(
{"error": "Пользователь с таким email не найден."},
    status=status.HTTP_404_NOT_FOUND
)

EXCEPTION_CONFLICT_USERNAME = ValidationError(
    {"username": "Пользователь с таким именем уже существует."}
)

EXCEPTION_CONFLICT_EMAIL = ValidationError(
    {"email": "Пользователь с таким email уже существует."}
)

EXCEPTION_UNAUTHORIZED = Response(
    {"detail": "Не авторизован"},
    status=status.HTTP_401_UNAUTHORIZED,
)

EXCEPTION_CONFLICT_ORGANIZATION = Response(
    {"detail": "Этот пользователь уже является участником организации."},
    status=status.HTTP_409_CONFLICT
)

EXCEPTION_ORGANIZATION_NOT_FOUND = Response(
    {"detail": "Организация не найдена"},
    status=status.HTTP_404_NOT_FOUND
)


from rest_framework.response import Response

from rest_framework import status


EXCEPTION_USER_NOT_FOUND = Response(
    {"detail": "Неверный логин или пароль"},
    status=status.HTTP_404_NOT_FOUND
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


from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


EXCEPTION_USER_NOT_FOUND = Response(
    {"detail": "Invalid username or password"},
    status=status.HTTP_404_NOT_FOUND
)

EXCEPTION_USER_PASSWORD = Response(
    {"error": "The current password is incorrect, or the new password does not match."},
    status=status.HTTP_400_BAD_REQUEST
)

EXCEPTION_USER_EMAIL = Response(
{"error": "The user with this email address was not found."},
    status=status.HTTP_404_NOT_FOUND
)

EXCEPTION_CONFLICT_USERNAME = ValidationError(
    {"username": "A user with that name already exists."}
)

EXCEPTION_CONFLICT_EMAIL = ValidationError(
    {"email": "The user with this email already exists."}
)

EXCEPTION_UNAUTHORIZED = Response(
    {"detail": "Not authorized"},
    status=status.HTTP_401_UNAUTHORIZED,
)

EXCEPTION_CONFLICT_ORGANIZATION = Response(
    {"detail": "This user is already a member of the organization."},
    status=status.HTTP_409_CONFLICT
)

EXCEPTION_ORGANIZATION_NOT_FOUND = Response(
    {"detail": "The organization was not found"},
    status=status.HTTP_404_NOT_FOUND
)


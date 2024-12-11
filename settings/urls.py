from typing import List

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Backend Mobile API",
        default_version="v1",
        description="Документация API для мобильного приложения",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny, ),
)

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("", include("app.authentication.urls")),
    path("", include("app.users.urls")),
    path("", include("app.tasks_board.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
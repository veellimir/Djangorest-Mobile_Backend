from django.contrib import admin

from .models import Organization, Tasks

admin.site.register(Organization)
admin.site.register(Tasks)
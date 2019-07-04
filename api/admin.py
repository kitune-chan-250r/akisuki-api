from django.contrib import admin
from .models import Count_data


@admin.register(Count_data)
class UserAdmin(admin.ModelAdmin):
    pass

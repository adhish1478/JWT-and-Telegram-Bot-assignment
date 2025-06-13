from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'telegram_id', 'first_name', 'last_name')
    search_fields = ('username', 'telegram_id', 'first_name')
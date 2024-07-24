from django.contrib import admin
from apps.tgbot.models import TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bot_username')
    list_display_links = ('id', 'name')

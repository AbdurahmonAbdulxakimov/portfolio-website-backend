from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from apps.tgbot.views import handle_telegram_webhook


app_name = 'tgbot'

urlpatterns = [
    path("handle_telegram_webhook/<str:bot_token>",
         csrf_exempt(handle_telegram_webhook), name="telegram_webhook")
]
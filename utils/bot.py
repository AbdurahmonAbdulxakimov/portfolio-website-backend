import requests
from django.conf import settings


def set_webhook_request(bot_token):
    webhook_url = settings.WEBHOOK_URL
    url = f"https://api.telegram.org/bot{bot_token}/setWebhook?url={webhook_url}/admin/telegram/bot/handle_telegram_webhook/{bot_token}"
    response = requests.post(url)
    return response.json()


def get_info(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.post(url)
    return response.json().get("result").get("username"), response.json().get(
        "result"
    ).get("first_name")

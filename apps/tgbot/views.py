import json
from queue import Queue

from django.http import JsonResponse
from django.utils.translation import gettext_lazy, activate
from telegram import Update, Bot
from telegram.ext import (
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters
)

from apps.tgbot.handlers import MainHandler
from apps.tgbot.texts import Texts

def _(text):
    return str(gettext_lazy(text))


class Filter(Filters):
    text_except_cmd = Filters.regex(f"^(?!/).*$")


def setup(token):
    bot = Bot(token=token)
    queue = Queue()

    dp = Dispatcher(
        bot,
        queue,
        workers=4,
        use_context=True
    )
    try:
        dp.add_error_handler(MainHandler.error)
        dp.add_handler(CommandHandler("start", MainHandler.start))
        dp.add_handler(MessageHandler(Filters.regex(Texts.resume), MainHandler.get_resume))
    except Exception as e:
        print(e)
    return dp


def handle_telegram_webhook(request, bot_token):
    bot = Bot(token=bot_token)
    update = Update.de_json(json.loads(request.body.decode("utf-8")), bot)

    dp = setup(bot_token)

    try:
        if update.message.chat.type == "private":
            dp.process_update(update)
    except Exception as e:
        print(e)
        dp.process_update(update)

    return JsonResponse({"status": "ok"})
from telegram import Update, ParseMode, File
from telegram.ext import CallbackContext

from apps.tgbot.texts import Texts
from apps.tgbot.buttons.main import Keyboard
from apps.contents.models import Resume

import html
import json
import logging
import traceback


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


class MainHandler:
    @staticmethod
    def error(update: Update, context: CallbackContext) -> None:
        def error_handler(update: object, context: CallbackContext) -> None:
            """Log the error and send a telegram message to notify the developer."""
            # Log the error before we do anything else, so we can see it even if something breaks.
            logger.error(msg="Exception while handling an update:", exc_info=context.error)

            # traceback.format_exception returns the usual python message about an exception, but as a
            # list of strings rather than a single string, so we have to join them together.
            tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
            tb_string = ''.join(tb_list)

            # Build the message with some markup and additional information about what happened.
            # You might need to add some logic to deal with messages longer than the 4096 character limit.
            update_str = update.to_dict() if isinstance(update, Update) else str(update)
            message = (
                f'An exception was raised while handling an update\n'
                f'<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}'
                '</pre>\n\n'
                f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
                f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
                f'<pre>{html.escape(tb_string)}</pre>'
            )

            # Finally, send the message
            context.bot.send_message(chat_id=5462212691, text=message, parse_mode=ParseMode.HTML)

    @staticmethod
    def start(update: Update, context: CallbackContext) -> None:
        update.message.reply_text(Texts.welcome, reply_markup=Keyboard.main())

    @staticmethod
    def get_resume(update: Update, context: CallbackContext) -> None:
        resume = Resume.objects.last().file
        try:
            with open(resume.path, "rb") as resume_file:
                update.message.reply_document(resume_file, reply_markup=Keyboard.main())
        except Exception as e:
            print(e)
            update.message.reply_text(Texts.error, reply_markup=Keyboard.main())
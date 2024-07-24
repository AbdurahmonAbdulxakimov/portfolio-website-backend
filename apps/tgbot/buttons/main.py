from telegram import ReplyKeyboardMarkup, KeyboardButton
from apps.tgbot.texts.main import Texts


class Keyboard:
    @staticmethod
    def main():
        buttons = [
            [
                KeyboardButton(Texts.resume),
            ],
        ]
        return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
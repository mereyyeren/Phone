
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qabdushev"),
            KeyboardButton(text="Sagintaev"),
        ],
        [
            KeyboardButton(text="Jaishibekov"),
            KeyboardButton(text="Amanjol"),
        ],
        [
            KeyboardButton(text="Aidana"),
            KeyboardButton(text="Erkin"),
            KeyboardButton(text="Almagul"),
        ],
    ],
    resize_keyboard=True
)
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def create_number_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру с кнопками 5, 10, 15."""
    button_5 = KeyboardButton(text="5")
    button_10 = KeyboardButton(text="10")
    button_15 = KeyboardButton(text="15")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_5, button_10, button_15]],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return keyboard




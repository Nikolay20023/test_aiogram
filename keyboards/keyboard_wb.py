from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_wild():
    kb = [
        [KeyboardButton(text="Остановить уведомления"),
         KeyboardButton(text="Получить информацию из бд")],
        [KeyboardButton(text="Получить информацию по товару")],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите функцию"
    )

    return keyboard

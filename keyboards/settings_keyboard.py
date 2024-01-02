from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


def settings():
    main = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Изменить группу 📔"),
                KeyboardButton(text="Отключить рассылку 📮"),
                KeyboardButton(text="Обновить расписание 📅"),
                KeyboardButton(text="Назад ◀"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите пункт...",
        selective=True
    )

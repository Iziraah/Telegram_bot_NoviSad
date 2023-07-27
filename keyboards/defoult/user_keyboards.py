from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Заявка на рекламу'),
            KeyboardButton(text='Правила чата'),
        ],
        [
            KeyboardButton(text='Разместить свое объявление'),
            KeyboardButton(text='Условия рекламы'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Клавиатура где-то здесь"
)


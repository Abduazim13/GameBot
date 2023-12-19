from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

subscribe = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⏬ Subscribe", url='https://t.me/carsinvideo'),
            InlineKeyboardButton(text="✅ Check", callback_data='check')
        ]
    ]
)

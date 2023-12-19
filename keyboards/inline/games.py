from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

only_android = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Play market", callback_data='play_market')
        ]
    ]
)

only_windows = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft')
        ]
    ]
)

only_mac = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mac Store", callback_data='mac_store')
        ]
    ]
)

only_app = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="App store", callback_data='app_store')

        ]
    ]
)

two_android_windows = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Play market", callback_data='play_market'),
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft')
        ]
    ]
)

two_android_app = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Play market", callback_data='play_market'),
            InlineKeyboardButton(text="App Store", callback_data='app_store')
        ]
    ]
)

two_app_mac = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mac Store", callback_data='mac_store'),
            InlineKeyboardButton(text="App Store", callback_data='app_store')
        ]
    ]
)

two_win_mac = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mac Store", callback_data='mac_store'),
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft')
        ]
    ]
)

three_win_app_android = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft'),
            InlineKeyboardButton(text="App Store", callback_data='app_store')
        ], [
            InlineKeyboardButton(text="Play Market", callback_data='play_market')
        ]
    ]
)

three_win_mac_android = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft'),
            InlineKeyboardButton(text="Mac Store", callback_data='mac_store')
        ], [
            InlineKeyboardButton(text="Play Market", callback_data='play_market')
        ]
    ]
)

alL_Company = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Microsoft", callback_data='microsoft'),
            InlineKeyboardButton(text="Mac Store", callback_data='mac_store')
        ], [
            InlineKeyboardButton(text="Play Market", callback_data='play_market'),
            InlineKeyboardButton(text="App Store", callback_data='app_store')
        ]
    ]
)

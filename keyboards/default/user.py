from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Send phone number", request_contact=True)
        ]
    ], resize_keyboard=True
)

games_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="WoT Blitz"),
            KeyboardButton(text="Roblox")
        ],
        [
            KeyboardButton(text="Free Fire"),
            KeyboardButton(text="Among us")
        ],
        [
            KeyboardButton(text="Pubg"),
            KeyboardButton(text="Bow master")
        ],
        [
            KeyboardButton(text="Counter-Strike 1.6"),
            KeyboardButton(text="Forza horizon: Demoversion")
        ],
        [
            KeyboardButton(text="Car parking"),
            KeyboardButton(text="Subway Surf")
        ],
        [
            KeyboardButton(text="Minecraft"),
            KeyboardButton(text="TLauncher")
        ],
        [
            KeyboardButton(text="Fortnite"),
            KeyboardButton(text="Minecraft: Java & Bedrock Edition")
        ],
        [
            KeyboardButton(text="Discord"),
            KeyboardButton(text="Hill Climb")
        ]
    ], resize_keyboard=True
)

game_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎮 To Games Menu")
        ]
    ], resize_keyboard=True
)


async def user_tests_keyboards_def(tests):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for test in tests:
        button = KeyboardButton(text=test['title'])
        markup.insert(button)
    markup.insert(KeyboardButton(text="Menyuga qaytish"))
    return markup

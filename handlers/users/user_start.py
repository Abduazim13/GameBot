from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from states.user import *
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline.subscribe import subscribe
from utils.checker import checker
from sql.select import get_user
from keyboards.default.user import *
from sql.insert import insert_user
from data.config import channel


@dp.message_handler(CommandStart())
async def start_handler(message: types.Message):
    if get_user(message.chat.id):
        text = "🇺🇸 Hello in Our Bot\n🇷🇺 Привет на нашет боте\n🇺🇿 Bizning botimizga xush kelibsiz"
        await message.answer(text=text, reply_markup=games_menu)
    else:
        text = "🇺🇸 Hello world.\nWrite your Full Name\n\n🇷🇺 Привет.\nНапишите полное имя\n\n🇺🇿 Salom.\nIsmingizni kiriting"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.full_name.set()


@dp.callback_query_handler(text='check')
async def check_again_handler(call: types.CallbackQuery):
    checker_user = await checker(user_id=call.message.chat.id, channel_id=channel[0])
    if checker_user:
        await call.message.delete()
        await call.answer('You are successfully subscribed ✅')
        if get_user(call.message.chat.id):
            text = "🇺🇸 Hello in Our Bot\n🇷🇺 Привет на нашет боте\n🇺🇿 Bizning botimizga xush kelibsiz\n\nSubscribe To my Channel:\nhttps://t.me/carsinvideo"
            await call.message.answer(text=text, reply_markup=games_menu)
        else:
            text = "🇺🇸 Hello world.\nWrite your Full Name\n\n🇷🇺 Привет.\nНапишите полное имя\n\n🇺🇿 Salom.\nIsmingizni kiriting"
            await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())
            await RegisterState.full_name.set()
    else:
        text = f"Subscribe to the channel to use the bot.\nПодпишитесь на канал, чтобы использовать бота.\nBotdan foydalanish uchun kanalga a'zo bo'ling."
        await call.message.answer(text=text, reply_markup=subscribe)


@dp.message_handler(state=RegisterState.full_name)
async def full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Now send your phone number\nТеперь отправьте номер телефона\nEndi telefon raqamingizni yuboring"
    await message.answer(text=text, reply_markup=phone_number)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(chat_id=message.chat.id, created_at=message.date, phone_number=message.contact.phone_number)
    data = await state.get_data()
    add_user_ = insert_user(data=data)
    if add_user_:
        text = "You have successfully registered\nВы успешно зарегистрировались\nSiz muvaffaqiyatli registratsiyadan o'tdingiz"
    else:
        text = "Bot has problems\nУ бота есть проблемы\nBotda muommo bor"
    await message.answer(text=text, reply_markup=games_menu)

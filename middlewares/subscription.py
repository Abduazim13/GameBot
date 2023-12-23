from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.checker import checker
from data.config import channel
from aiogram import types
from keyboards.inline.subscribe import subscribe
from aiogram.dispatcher.handler import CancelHandler


class CheckSub(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        user_id = 0
        if update.message:
            if update.message.text == "/start":
                return
            user_id = update.message.chat.id
        elif update.callback_query:
            user_id = update.callback_query.message.chat.id
            if update.callback_query.data == "check":
                checkers = await checker(user_id=user_id, channel_id=channel[0])

                if not checkers:
                    await update.callback_query.message.delete()
                    text = "Subscribe to the channel to use the bot.\nПодпишитесь на канал, чтобы использовать бота.\nBotdan foydalanish uchun kanalga a'zo bo'ling."
                    await update.callback_query.message.answer(text=text, reply_markup=subscribe)
                    raise CancelHandler()

        checkers = await checker(user_id=user_id, channel_id=channel[0])

        if not checkers:
            await update.message.delete()
            text = "Subscribe to the channel to use the bot.\nПодпишитесь на канал, чтобы использовать бота.\nBotdan foydalanish uchun kanalga a'zo bo'ling."
            await update.message.answer(text=text, reply_markup=subscribe)
            raise CancelHandler()

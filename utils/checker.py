from aiogram import Bot
from data.config import channel


async def checker(user_id):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel[0])
    return member.is_chat_member()



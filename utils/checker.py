from aiogram import Bot


async def checker(user_id, channel_id):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id)
    return member.is_chat_member()



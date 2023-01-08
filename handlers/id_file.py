from aiogram import types, Dispatcher
from creat_bot import bot


async def cmd_user_id(message: types.Message):
    await bot.send_message(message.chat.id, f"The id of this user: {message.reply_to_message.from_user.id}")


async def cmd_group_id(message: types.Message):
    await bot.send_message(message.chat.id, f"The id of this group: {message.chat.id}")


def register_handlers_id_file(dp: Dispatcher):
    dp.register_message_handler(cmd_user_id, commands='user_id')
    dp.register_message_handler(cmd_group_id, commands='group_id')
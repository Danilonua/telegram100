from aiogram import types, Dispatcher
from creat_bot import bot

warns = {}


# @dp.message_handler(commands='warn')
async def cmd_warn(message: types.Message):
    """
    Warn user
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:

        user_id = message.reply_to_message.from_user.id
        if user_id not in warns:
            warns[user_id] = 0
        warns[user_id] += 1
        if warns[user_id] >= 3:
            await bot.kick_chat_member(message.chat.id, user_id)
            warns[user_id] = 0
        await message.reply(f"User has been warned. They now have {warns[user_id]} warns.")
    else:
        await message.reply(f"This command can be used only by administration")


# @dp.message_handler(commands='view_warns')
async def view_warns(message: types.Message):
    """
    View warns of user
    """
    user_id = message.reply_to_message.from_user.id
    if user_id not in warns:
        warns[user_id] = 0
    await message.reply(f"This user has {warns[user_id]} warns.")


def register_handlers_warn_file(dp: Dispatcher):
    dp.register_message_handler(cmd_warn, commands='warn')
    dp.register_message_handler(view_warns, commands='view_warns')
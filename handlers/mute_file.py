from aiogram import types, Dispatcher
import datetime
from creat_bot import bot

mutes = {}


async def cmd_mute_forever(message: types.Message):
    """
    Mute user
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        user_id = message.reply_to_message.from_user.id
        await bot.restrict_chat_member(message.chat.id, user_id, until_date=None)
        await bot.restrict_chat_member(message.chat.id, user_id, until_date=float("inf"))
        await message.reply("User has been muted forever!")
    else:
        await message.reply(f"This command can be used only by administration")


# @dp.message_handler(commands='mute')
async def cmd_mute(message: types.Message):
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        try:
            user_id = message.reply_to_message.from_user.id
        except AttributeError:
            await message.reply("This command should be reply to message!")
            return
        try:
            mute_duration = int(message.text[6:])
        except ValueError:
            if message.text == "/mute":
                await cmd_mute_forever(message)
                return
            else:
                await message.reply("please type int number!")
                return
        if mute_duration <= 0:
            await message.reply("Please type number that bigger then 0")
            return
        until_date = datetime.datetime.now() + datetime.timedelta(hours=mute_duration)
        until_timestamp = int(until_date.timestamp())
        await bot.restrict_chat_member(message.chat.id, user_id, until_date=until_timestamp)
        mutes[user_id] = True
        await message.reply(f"User has been banned for {mute_duration} hours.")
    else:
        await message.reply(f"This command can be used only by administration")


# @dp.message_handler(commands='unmute')
async def cmd_unmute(message: types.Message):
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        try:
            user_id = message.reply_to_message.from_user.id
        except AttributeError:
            await message.reply("This command should be reply to message!")
            return

        await bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
        await message.reply("User has been unmuted.")
    else:
        await message.reply(f"This command can be used only by administration")


def register_handlers_mute_file(dp: Dispatcher):
    dp.register_message_handler(cmd_mute, commands='mute')
    dp.register_message_handler(cmd_unmute, commands='unmute')
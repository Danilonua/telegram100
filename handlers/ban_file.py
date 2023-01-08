from aiogram import types, Dispatcher
import datetime
from creat_bot import bot


async def cmd_ban(message: types.Message):
    """
    Ban user
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        user_id = message.reply_to_message.from_user.id

        await bot.kick_chat_member(message.chat.id, user_id)
        await message.reply("User has been banned.")
    else:
        await message.reply(f"This command can be used only by administration")


# @dp.message_handler(commands='unban')
async def cmd_unban(message: types.Message):
    """
    Unban user
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        user_id = message.reply_to_message.from_user.id
        await bot.unban_chat_member(message.chat.id, user_id)
        await message.reply("User has been unbanned.")
    else:
        await message.reply(f"This command can be used only by administration")


# @dp.message_handler(commands='ban')
async def ban(message: types.Message):
    """
    Ban user for specified amount of time
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        # Get user ID of user to ban
        try:
            user_id = message.reply_to_message.from_user.id
        except AttributeError:
            await message.reply("This command should be reply to message!")
            return

        # Get time to ban user for
        try:
            ban_duration = int(message.text[5:])
        except ValueError:
            if message.text == "/ban":
                await cmd_ban(message)
                return
            else:
                await message.reply("please type int number!")
                return
        if ban_duration <= 0:
            await message.reply("Please type number that bigger then 0")
            return

        # Convert ban duration to integer
        ban_duration = int(ban_duration)

        # Calculate ban end time
        until_date = datetime.datetime.now() + datetime.timedelta(days=ban_duration)
        until_timestamp = int(until_date.timestamp())

        # Ban user
        await bot.kick_chat_member(message.chat.id, user_id, until_date=until_timestamp)
        await message.reply(f"User has been banned for {ban_duration} days.")
    else:
        await message.reply(f"This command can be used only by administration")


def register_handlers_mute_file(dp: Dispatcher):
    dp.register_message_handler(cmd_unban, commands='unban')
    dp.register_message_handler(ban, commands='ban')
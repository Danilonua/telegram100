from aiogram import types, Dispatcher
from creat_bot import bot


# @dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Start the bot
    """

    await message.reply("I'm a moderator bot! Use the /help command to see what I can do.")


# @dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    """
    Show help message
    """
    await message.reply("Here are the commands you can use:\n\n/start - starts the bot\n/help - shows this help"
                        " message\n/delete_message - deletes the current message\n/warn - warns the user\n/ban -"
                        " bans the user\n/unban - unban the user\n/view_warns - view the warns of the user\n/mute -"
                        " mute the user for 2 minutes\n/unmute - unmute the user")


# @dp.message_handler(commands='delete_message')
async def cmd_delete_message(message: types.Message):
    """
    Delete current message
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply(f"This command can be used only by administration")


def register_handlers_other_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')
    dp.register_message_handler(cmd_delete_message, commands='delete_message')
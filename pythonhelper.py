from aiogram import types
from aiogram.utils import executor
from creat_bot import dp, bot
from handlers import mute_file
from handlers import ban_file
from handlers import warn_file
from handlers import filter_file


mute_file.register_handlers_mute_file(dp)
ban_file.register_handlers_ban_file(dp)
warn_file.register_handlers_warn_file(dp)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Start the bot
    """

    await message.reply("I'm a moderator bot! Use the /help command to see what I can do.")


@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    """
    Show help message
    """
    await message.reply("Here are the commands you can use:\n\n/start - starts the bot\n/help - shows this help"
                        " message\n/delete_message - deletes the current message\n/warn - warns the user\n/ban -"
                        " bans the user\n/unban - unban the user\n/view_warns - view the warns of the user\n/mute -"
                        " mute the user for 2 minutes\n/unmute - unmute the user")


@dp.message_handler(commands='delete_message')
async def cmd_delete_message(message: types.Message):
    """
    Delete current message
    """
    if message.from_user.id == 1988813101 or message.from_user.id == 1563335601:
        await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply(f"This command can be used only by administration")


filter_file.register_handlers_filter_file(dp)


if __name__ == '__main__':
    print('It has started!')
    executor.start_polling(dp)
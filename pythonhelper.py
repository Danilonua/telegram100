from aiogram import types
from aiogram.utils import executor
import datetime
from creat_bot import dp, bot
from handlers import mute_file

# Dictionary to store warns for each user
warns = {}

# Dictionary to store mute status for each user
bad_words = {'fuck', 'stupid'}
ban_duration = 0


mute_file.register_handlers_mute_file(dp)


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


@dp.message_handler(commands='warn')
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
        await message.reply(f"User has been warned. They now have {warns[user_id]} warns.")
    else:
        await message.reply(f"This command can be used only by administration")


@dp.message_handler(commands='view_warns')
async def view_warns(message: types.Message):
    """
    View warns of user
    """
    user_id = message.reply_to_message.from_user.id
    if user_id not in warns:
        warns[user_id] = 0
    await message.reply(f"This user has {warns[user_id]} warns.")


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


@dp.message_handler(commands='unban')
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


@dp.message_handler(commands='ban')
async def ban(message: types.Message):
    global ban_duration
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


@dp.message_handler()
async def cmd_filter_message(msg: types.Message):
    text = msg.text.lower()
    for word in bad_words:
        if word in text:
            await msg.delete()

if __name__ == '__main__':
    print('It has started!')
    executor.start_polling(dp)
from aiogram import types, Dispatcher
from creat_bot import bot


async def cmd_say(message: types.Message):
    text = message.text[5:]
    await bot.send_message(message.chat.id, text)


async def send_handshake(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) пожал руку [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) пожал руку всем', parse_mode="Markdown")


async def send_kill(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await bot.kick_chat_member(message.chat.id, friend_id)
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) убил [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) хотел убить всех, но ему ето не удалось! ',
                             parse_mode="Markdown")


async def send_invite_for_tea(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) пригласил на чай [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) пригласил всех на чай', parse_mode="Markdown")


async def send_kiss(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) поцеловал [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) поцеловал всех', parse_mode="Markdown")


async def send_sorry(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) извинился перед [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) извинился перед всеми', parse_mode="Markdown")


async def send_insult(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) оскорбил [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) оскорбил всех', parse_mode="Markdown")


async def send_help(message: types.Message):
    try:
        your_id = message.from_id
        your_name = message.from_user.username
        friend_name = message.reply_to_message.from_user.username
        friend_id = message.reply_to_message.from_user.id
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) попросил помощь у [{friend_name}](tg:'
                             f'//user?id={str(friend_id)})', parse_mode="Markdown")
    except AttributeError:
        your_id = message.from_id
        your_name = message.from_user.username
        await message.answer(f'[{your_name}](tg://user?id={str(your_id)}) попросил помощь у всех', parse_mode="Markdown")


def register_handlers_id_file(dp: Dispatcher):
    dp.register_message_handler(cmd_say, commands='say')
    dp.register_message_handler(send_handshake, commands='handshake')
    dp.register_message_handler(send_kill, commands='kill')
    dp.register_message_handler(send_invite_for_tea, commands='tea')
    dp.register_message_handler(send_kiss, commands='kiss')
    dp.register_message_handler(send_sorry, commands='sorry')
    dp.register_message_handler(send_insult, commands='insult')
    dp.register_message_handler(send_help, commands='help')
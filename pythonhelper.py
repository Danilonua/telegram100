from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5806684198:AAHPUv9k_AcMXXfdmFZyPcFEDNSCDtRckUM")
dp = Dispatcher(bot)
db = Database("database.db")

bad_words = ["бля", "сука", "блять", "дебил", "блядь", "пизда", "хуй", "член", "долбоеб"]


@dp.message_handler(commands=["mute"], commands_prefix="/")
async def mute(msg: types.Message):
    if str(msg.from_user.id) == "1988813101":
        if not msg.reply_to_message:
            await msg.reply("Ета команда должна быть ответом на сообщение!")
            return
        mute_sec = int(msg.text[:6])
        db.add_mute(msg.reply_to_message.from_user.id, mute_sec)
        await msg.bot.delete_message(msg.chat.id, msg.message_id)
        await msg.reply_to_message.reply(f"Пользователь был забанен на {mute_sec} секунд!")


@dp.message_handler(commands=["ban"], commands_prefix="!/")
async def cmd_ban(msg: types.Message):
    if not msg.reply_to_message:
        await msg.reply("Ета команда должна быть ответом на сообщение!")
        return
    await msg.bot.delete_message(msg.chat.id, msg.message_id)
    await msg.bot.kick_chat_member(chat_id=msg.chat.id, user_id=msg.reply_to_message.from_user.id)


@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(msg: types.Message):
    await msg.delete()
    await msg.bot.send_message(chat_id=msg.chat.id, text="У нас новый пользователь, поприветствуем его!")


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler()
async def filter_message(msg: types.Message):
    if not db.mute(msg.from_user.id):
        text = msg.text.lower()
        for word in bad_words:
            if word in text:
                await msg.delete()
    else:
        await msg.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
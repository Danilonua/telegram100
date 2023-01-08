from aiogram import types, Dispatcher

bad_words = {'fuck', 'stupid'}


# @dp.message_handler()
async def cmd_filter_message(msg: types.Message):
    text = msg.text.lower()
    for word in bad_words:
        if word in text:
            await msg.delete()


def register_handlers_filter_file(dp: Dispatcher):
    dp.register_message_handler(cmd_filter_message)
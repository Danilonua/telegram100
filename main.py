import telebot
from telebot import types
import logging

bot = telebot.TeleBot("5202477338:AAFFgxbKRs1Oh23TU7OxnbkWaLaxMpaUrJI")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("start")
logger.info("I am working now")
x = 0


@bot.message_handler(commands=["start"])
def start(message):
    if x == 0:
        buttons1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Так, я хочу почати прямо зараз")
        btn2 = types.KeyboardButton("Так, я хочу, але пізніше")
        btn3 = types.KeyboardButton("Воно мені не потрібне")
        buttons1.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f"Привіт, {message.from_user.full_name}. Я можу Вам допомогти почати"
                                          f" вивчати базовий Python.")
        bot.send_message(message.chat.id, "Python - це мова програмування за допомогою якої, можна програмувати різні"
                                          " програми. Ця мова дуже легка та зрозуміла. Якщо Ви хочете спробувати"
                                          " свої сили, то можете почати навчання прямо зараз безкоштовно!",
                         reply_markup=buttons1)
        bot.send_message(message.chat.id, "Якщо Ви хочете поспілкуватися з автором цього бота, то пишіть, будь ласка,"
                                          " на електронну адресу: horenkomihailo2022@gmail.com")
    else:
        bot.delete_message(message.chat.id, message.id)


@bot.message_handler(content_types=["text"])
def answer(message):
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    buttons2 = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn4 = telebot.types.InlineKeyboardButton(text='Я передумав', callback_data="button4")
    btn5 = telebot.types.InlineKeyboardButton(text='Відстань від мене!', callback_data="button5")
    buttons2.add(btn4, btn5)
    if x == 1:
        bot.delete_message(message.chat.id, message.id)
    else:
        if message.text == "Так, я хочу почати прямо зараз":
            bot.send_message(message.chat.id, "Гарний вибір. Вам потрібно приєднатися до каналу у telegram. Ось"
                                              " посилання⬇️", reply_markup=remove_keyboard)
        if message.text == "Так, я хочу, але пізніше":
            bot.send_message(message.chat.id, "Добре, скоро зустрінемося! Напишіть /start, коли захочете розпочати"
                                              " перший урок.", reply_markup=remove_keyboard)
        if message.text == "Воно мені не потрібне":
            bot.send_message(message.chat.id, "Ех, жаль, а я так хотів з тобою попрограмувати... Якщо передумаєте"
                                              " натисніть на кнопку нижче", reply_markup=remove_keyboard)
            bot.send_message(message.chat.id, "Якщо передумаєте натисніть на кнопку нижче⬇ ", reply_markup=buttons2)


@bot.callback_query_handler(func=lambda c: c.data == 'button4')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ура! Я так рад за тебе! Тепер ти можеш змінити свій вибір😃, для '
                                                  'цього тобі потрібно написати /start')


@bot.callback_query_handler(func=lambda c: c.data == 'button5')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Пока, я добавляю тебе в чорний список!')
    global x
    x = 1


bot.polling(none_stop=True)

if StopIteration:
    logger = logging.getLogger("stop")
    logger.info("I am not working now")
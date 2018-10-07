import telebot
import time
from telebot.types import Message

token = "651370725:AAHmpDhzbliT9KjqOGbPrELzZ4VPrYb4RuQ"
bot = telebot.TeleBot(token)


"""
def log(message, answer):
    print("\n -------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)
"""


@bot.message_handler(commands=["start", "help", "settings"])
def command_handler(message: Message):
    bot.reply_to(message, "Сдуйся, опездол")


@bot.message_handler(content_types=["text"])
@bot.edited_message_handler(content_types=["text"])
def echo_digits(message: Message):
    text = message.text.lower()
    if "фергус" in text:
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "а")
            return
        else:
            bot.reply_to(message, "Сдуйся, дерьмодемон. Мне не о чем с тобой говорить")


@bot.message_handler(content_types=["sticker"])
def echo_digits(message: Message):
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "Не позорься")
        else:
            bot.reply_to(message, "Господи, ну ты и хуебес. Сейчас бан словишь")


@bot.message_handler(content_types=["photo"])
def echo_digits(message: Message):
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "Великолепный мэм")
        else:
            bot.reply_to(message, "Ну ты и дерьмо отправил, додик. Хуёвый Мэм, бан, дисреспект")

            
bot.polling(none_stop=True, interval=0)

import telebot
from telebot.types import Message
import sourse

bot_client = telebot.TeleBot(token=sourse.token)


@bot_client.message_handler(commands=['старт', 'start', 'привет', 'Привет'])
def echo(massage: Message):
    bot_client.send_message(chat_id=massage.chat.id, text='Я люблю тебя:)')
    # print(massage.chat.id)
    c = 1


bot_client.polling()
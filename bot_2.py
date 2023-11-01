import telebot
from telebot.types import Message
import sourse

bot_client = telebot.TeleBot(token=sourse.token)


@bot_client.message_handler(commands=['старт', 'start'])
def echo(massage: Message):
    bot_client.send_message(chat_id=massage.chat.id, text='Send')
    # print(massage.chat.id)
    c = 1


bot_client.polling()
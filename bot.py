import os
from dotenv import load_dotenv
import telebot

load_dotenv()

api_key = os.getenv("API_KEY")
bot = telebot.TeleBot(api_key)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/weather':
        bot.send_message(message.from_user.id, "Момент, домовляюсь з небесною канцелярією..")
    else:
        bot.send_message(message.from_user.id, 'Тяпни /weather')


bot.polling(none_stop=True, interval=0)

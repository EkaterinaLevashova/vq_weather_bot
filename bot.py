import os
from dotenv import load_dotenv
import telebot

from src.scrapper import Weather

load_dotenv()

api_key = os.getenv("API_KEY")
bot = telebot.TeleBot(api_key)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/weather':
        bot.send_message(message.from_user.id, "Момент, домовляюсь з небесною канцелярією..")
        weather = Weather().get_weather()
        content = (
            f"Температура: {weather['temperature']} \n"
            f"В цілому: {weather['description']} \n"
            f"Шо по вітру: {weather['wind']}"
        ) if weather else "На жаль, не вдалося отримати інформацію про погоду"
        if weather:
            bot.send_message(
                message.from_user.id,
                content
            )
        else:
            bot.send_message(message.from_user.id, "На жаль, не вдалося отримати інформацію про погоду")
    else:
        bot.send_message(message.from_user.id, 'Тяпни /weather')


bot.polling(none_stop=True, interval=0)

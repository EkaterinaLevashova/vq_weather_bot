import os
from dotenv import load_dotenv
import telebot
from telebot import types

from src.scrapper import Weather

load_dotenv()

api_key = os.getenv("API_KEY")
bot = telebot.TeleBot(api_key)


@bot.message_handler(content_types=['text'])
def start(message):

    weather = types.BotCommand(command='weather', description='Покаж погоду')
    weather_3 = types.BotCommand(command='weather_3', description='Покаж погоду на 3 дні')
    weather_7 = types.BotCommand(command='weather_7', description='Покаж погоду на тиждень')
    bot.set_my_commands([weather, weather_3, weather_7])
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonCommands('commands'))

    if message.text == '/weather':
        bot.send_message(message.from_user.id, "Момент, домовляюсь з небесною канцелярією..")
        weather = Weather().get_weather()
        content = (
            f"<b>Шо маємо на сьогодні:</b> \n"
            f"Температура: {weather['temperature']} \n"
            f"В цілому: {weather['description']} \n"
            f"Шо по вітру: {weather['wind']}"
        ) if weather else "На жаль, не вдалося отримати інформацію про погоду"
        if weather:
            bot.send_message(
                message.from_user.id,
                content,
                parse_mode='HTML'
            )
        else:
            bot.send_message(message.from_user.id, "На жаль, не вдалося отримати інформацію про погоду")
    else:
        bot.send_message(message.from_user.id, 'Тяпни /weather')


bot.polling(none_stop=True, interval=0)

import pyowm                                                                  # Импортируем модули
import telebot
import os
import time

# config_dict = get_default_config()
# config_dict['language'] = 'ru'
botToken = os.getenv('5709451393:AAEH9VpfRC8xyqVp26xkhCBEPAcsnjhsHDU')          # Telegram bot
bot = telebot.TeleBot(botToken)
owmToken = os.getenv('374db0bd2183096bd1afb5980354910c')                        # Доступ к прогнозу OWM
owm = pyowm.OWM(owmToken, language='ru')


@bot.message_handler(content_types=['text'])                                    # Модуль общения с ботом
def send_message(message):
    """Send the message to user with the weather"""

    if message.text.lower() == "/start" or message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    else:
        try:
            observation = owm.weather_at_place(message.text)
            weather = observation.get_weather()
            temp = weather.get_temperature("celsius")["temp"]
            temp = round(temp)
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), temp, "C", weather.get_detailed_status())

            answer = "В городе " + message.text.title() + " сейчас " + weather.get_detailed_status() + "." + "\n"
            answer += "Температура около: " + str(temp) + " С" + "\n\n"
            if temp < -10:
                answer += "Пипец как холодно, одевайся как танк!"
            elif temp < 10:
                answer += "Холодно, одевайся теплее."
            elif temp > 25:
                answer += "Жарень."
            else:
                answer += "На улице вроде норм!!!"
        except Exception:
            answer = "Не найден город, попробуйте ввести название снова.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), 'Error')

        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)                                               # Запускаем бота
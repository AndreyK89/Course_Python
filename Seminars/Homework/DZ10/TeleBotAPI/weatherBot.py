import telebot
import requests
import random
from telebot import types

# f = open('facts.txt', 'r', encoding='UTF-8')                       # Загружаем список интересных фактов
# facts = f.read().split('\n')
# f.close()

# f = open('thinks.txt', 'r', encoding='UTF-8')                      # Загружаем список поговорок
# thinks  = f.read().split('\n')
# f.close()

bot = telebot.TeleBot('5671094069:AAE8MGojJf9ScZm_tP8bJMpp5BbtkbwN47E')    # Создаем бота

@bot.message_handler(commands=["start"])                              # Команда start
def start(m, res=False):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)        # Добавляем две кнопки
        item1=types.KeyboardButton("Набери город: ")
        item2=types.KeyboardButton("Жми Погода.")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \n \nНабери Город. Введи город\n \nЖмите Погода, получите данные. ',  reply_markup=markup)

@bot.message_handler(content_types=["text"])                         # Получение сообщений от юзера
def handle_text(message):

    if message.text.strip() == 'Факт о Тобольске' :
            answer = random.choice(facts)                             # Если юзер прислал 1, выдаем ему случайный факт
    elif message.text.strip() == 'Поговорка Тобольской губернии':
            answer = random.choice(thinks)                            # Если юзер прислал 2, выдаем умную мысль
    bot.send_message(message.chat.id, answer)                         # Отсылаем юзеру сообщение в его чат

bot.polling(none_stop=True, interval=0)                               # Запускаем бота

# import requests
# name = input()
# response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
# a = response.json()
# print(a)
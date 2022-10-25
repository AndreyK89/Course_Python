import telebot
import random
from telebot import types

f = open('facts.txt', 'r', encoding='UTF-8')                       # Загружаем список интересных фактов
facts = f.read().split('\n')
f.close()

f = open('thinks.txt', 'r', encoding='UTF-8')                      # Загружаем список поговорок
thinks  = f.read().split('\n')
f.close()

bot = telebot.TeleBot('Ваш токен')    # Создаем бота

@bot.message_handler(commands=["start"])                              # Команда start
def start(m, res=False):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)        # Добавляем две кнопки
        item1=types.KeyboardButton("Факт о Тобольске")
        item2=types.KeyboardButton("Поговорка Тобольской губернии")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \n \nФакт для получения интересного факта о Тобольске\n \nПоговорка Тобольской губернии — для получения мудрой цитаты ',  reply_markup=markup)

@bot.message_handler(content_types=["text"])                         # Получение сообщений от юзера
def handle_text(message):

    if message.text.strip() == 'Факт о Тобольске' :
            answer = random.choice(facts)                             # Если юзер прислал 1, выдаем ему случайный факт
    elif message.text.strip() == 'Поговорка Тобольской губернии':
            answer = random.choice(thinks)                            # Если юзер прислал 2, выдаем умную мысль
    bot.send_message(message.chat.id, answer)                         # Отсылаем юзеру сообщение в его чат

bot.polling(none_stop=True, interval=0)                               # Запускаем бота

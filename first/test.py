import telebot
from telebot import types


token = '5857174935:AAH1EwIPZnH6cdtCeb2YE1Sn3gY4OZ0offc'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Расскажи о себе')
    btn2 = types.KeyboardButton('Контакты организации')
    btn3 = types.KeyboardButton('Выбор тура')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text='Привет, {user_name}, я бот, который поможет тебе подобрать идеальный тур!'.format(user_name=message.from_user.first_name), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Расскажи о себе':
        bot.send_message(message.chat.id, text='Я бот турфирмы ООО "АМРА"\nя помогу тебе с выбором лучшего в твоей жизни тура по России или за границей')
        bot.send_message(message.chat.id, text='🏝️')
    elif message.text == 'Контакты организации':
        bot.send_message(message.chat.id, text='Наш офис находится по адресу г. Ростов-на-Дону, Буденновский проспект, 21. офис 312\n'
                                          'По всем вопросам ты можешь обращаться к оператору по номеру +7 (863) 226-91-20 или +7 (863) 226-91-18')
        bot.send_message(message.chat.id, text='☎️')
    elif message.text == 'Выбор тура':
        bot.send_message(message.chat.id, text='Все еще в разработке...')
        bot.send_message(message.chat.id, text='👨‍💻')
    else:
        bot.send_message(message.chat.id, text='Прости, я не понял тебя')
        bot.send_photo(message.chat.id, photo='https://sun6-23.userapi.com/impg/GBe_CyqCYNMm_cSezDF51PxUcZuUCA7K1S4mOg/WDSzE9U5m0c.jpg?size=504x444&quality=96&sign=9128388d69635aef52333497aeeb0e9d&type=album')


if __name__ == '__main__':
    bot.infinity_polling()
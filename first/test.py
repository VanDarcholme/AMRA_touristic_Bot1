import telebot
from telebot import types
import pymysql

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='amra_bot',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('database successfully connected!!!')
except Exception as ex:
    print('error')
    print(ex)


token = '5857174935:AAH1EwIPZnH6cdtCeb2YE1Sn3gY4OZ0offc'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Расскажи о себе')
    btn2 = types.KeyboardButton('Контакты организации')
    btn3 = types.KeyboardButton('Выбор тура')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text='Привет, {user_name}, я бот, который поможет тебе подобрать идеальный тур!'
                     .format(user_name=message.from_user.first_name), reply_markup=markup)

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
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       btn_Italy = types.KeyboardButton('Италия')
       btn_Greece = types.KeyboardButton('Греция')
       btn_Tunis = types.KeyboardButton('Тунис')
       btn_Marocco = types.KeyboardButton('Марокко')
       btn_OAE = types.KeyboardButton('ОАЭ')
       btn_Turkey = types.KeyboardButton('Турция')
       btn_BlackSea = types.KeyboardButton('Черноморское побережье')
       btn_Potrugal = types.KeyboardButton('Португалия')
       markup.add(btn_Italy, btn_Greece, btn_Tunis, btn_Marocco, btn_OAE, btn_Turkey, btn_BlackSea, btn_Potrugal)
       bot.send_message(message.chat.id, text='Выбери страну, в которую ты хочешь отправиться', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text='Прости, я не понял тебя')



if __name__ == '__main__':
    bot.infinity_polling()
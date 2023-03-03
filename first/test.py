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
       btn_Italy = types.KeyboardButton('Италия 🇮🇹')
       btn_Greece = types.KeyboardButton('Греция 🇬🇷')
       btn_Tunis = types.KeyboardButton('Тунис 🇹🇳')
       btn_Marocco = types.KeyboardButton('Марокко 🇲🇦')
       btn_OAE = types.KeyboardButton('ОАЭ 🇦🇪')
       btn_Turkey = types.KeyboardButton('Турция 🇹🇷')
       btn_BlackSea = types.KeyboardButton('Черноморское побережье 🇷🇺')
       btn_Potrugal = types.KeyboardButton('Португалия 🇵🇹')
       btn_back = types.KeyboardButton('Вернуться на главную ↩️')
       markup.add(btn_Italy, btn_Greece, btn_Tunis, btn_Marocco, btn_OAE, btn_Turkey, btn_BlackSea, btn_Potrugal, btn_back)
       bot.send_message(message.chat.id, text='Выбери страну, в которую ты хочешь отправиться\nЯ отправлю тебе список курортов, которые доступны у нас', reply_markup=markup)

    elif message.text == 'Италия 🇮🇹':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `italy`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Греция 🇬🇷':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `greece`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Тунис 🇹🇳':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `tunis`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Марокко 🇲🇦':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `marocco`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'ОАЭ 🇦🇪':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `oae`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Турция 🇹🇷':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `turkey`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Черноморское побережье 🇷🇺':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `blacksea`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Португалия 🇵🇹':
        with connection.cursor() as cursor:
            query = "SELECT * FROM `portugal`"
            cursor.execute(query)
            rows = cursor.fetchall()
            result = ''
        for row in rows:
            print(row['city'])
            result += row['city'] + '\n'
        bot.send_message(message.chat.id, text=result)

    elif message.text == 'Вернуться на главную ↩️':
        start(message)


if __name__ == '__main__':
    bot.infinity_polling()
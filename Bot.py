import telebot

API_TOKEN = '1000707049:AAF-8seTHMnjZxcL0504N3G0PP6tUdESES0'

bot = telebot.TeleBot(API_TOKEN)
markup =telebot.types.ReplyKeyboardMarkup()
itembtn1 = telebot.types.KeyboardButton('a')
itembtn2 = telebot.types.KeyboardButton('v')
itembtn3 = telebot.types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3) 


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "хуй":
         bot.reply_to(message, "ты пидор", reply_markup=markup) 


bot.polling()

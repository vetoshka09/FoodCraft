import telebot

bot = telebot.TeleBot('7879647049:AAHaIDM-aaXPeYJNgk24JMWSSahXKbLT6E0')

@bot.message_handler(commands=['start', 'приве', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Помогу <u>чу-чуть</u> позже) <b>@vetoshka</b>', parse_mode='html')


bot.polling(none_stop=True)
import telebot

bot = telebot.TeleBot("1627591949:AAEKchQi8DlJEg2vqgbNsDFWP1Ca0_Ax1Pg")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    bot.send_message(message.from_user.id, "you sent "+text)
    int_value = int(text)
    bot.send_message(message.from_user.id, "square "+str(int_value**2))


bot.polling()

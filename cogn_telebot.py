import telebot
import constants

bot = telebot.TeleBot(constants.token)

#---------------------Message handlers: for commands---------------------

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/reboot', '/stop')
    user_markup.row('Supervisor', 'New Comer')
    user_markup.row('Buddy', 'Recruiter')
    bot.send_message(message.from_user.id, 'Greetings')
    bot.send_message(message.from_user.id, 'Choose your destiny!', reply_markup=user_markup)

@bot.message_handler(commands=['reboot'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/reboot', '/stop')
    user_markup.row('New Comer', 'Supervisor')
    user_markup.row('Buddy', 'Recruiter')
    bot.send_message(message.from_user.id, 'Choose your destiny!', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Thanks for talking to me =)', reply_markup=hide_markup)

#---------------------Message handlers: for 'Supervisor' choise---------------------

@bot.message_handler(content_types=['text'])
def handle_supervizor(message):
    if message.text == 'Supervisor':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)

#---------------------Message handlers: for 'New Comer' choise---------------------

    if message.text == 'New Comer':
        bot.send_message(message.from_user.id, 'Welcome to Phillip Morris! It is your first day, happy to get you on board!')
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)
    if message.text == 'Get sticker':
        bot.send_sticker(message.from_user.id, 'CAADAgADXgAD1jUSAAHMmC9kAAFQGeUC')

#---------------------Message handlers: for 'Buddy' choise---------------------

    if message.text == 'Buddy':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)

#---------------------Message handlers: for 'Recruiter' choise---------------------

    if message.text == 'Recruiter':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)


bot.polling(none_stop=True, interval=0)

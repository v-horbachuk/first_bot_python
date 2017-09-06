import telebot
import time

#My_TOKEN: 408316237:AAGFODWWvu-6mOXRBc_klCIlDKV_5lPATMk

bot = telebot.TeleBot('350637828:AAHlEKLAi_WSV0JGixo5kpZvy6un88-PoNk')

#---------------------Message handlers: for commands---------------------

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Неу!')
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/prior_to_start', '/stop')
    user_markup.row('New Comer', 'Buddy')
    user_markup.row('Supervisor')
    bot.send_message(message.from_user.id, 'Which experience do you want me to demonstrate?', reply_markup=user_markup)

@bot.message_handler(commands=['prior_to_start'])
def handle_prior(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/prior_to_start', '/stop')
    user_markup.row('New Comer', 'Buddy')
    user_markup.row('Supervisor')
    bot.send_message(message.from_user.id, 'Which experience do you want me to demonstrate?', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Good luck =)', reply_markup=hide_markup)

    #---------------------Message handlers---------------------

@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
#____________________________________________________________________________________
# ---------------------Message handlers: for 'Supervisor' choise---------------------
#____________________________________________________________________________________

    if message.text == 'Supervisor':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('1st dаy', '1st wеek')
        user_markup.row('1st 90 dаys', '1st yeаr')
        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == '1st dаy':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
    if message.text == '1st wеek':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
    if message.text == '1st 90 dаys':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
    if message.text == '1st yeаr':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
#__________________________________________________________________________________
#---------------------Message handlers: for 'New Comer' choise---------------------
#__________________________________________________________________________________

    if message.text == 'New Comer':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('1st day', '1st week')
        user_markup.row('1st 90 days', '1st year')
        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == '1st day':
        bot.send_message(message.from_user.id, 'Welcome to Phillip Morris! It is your first day, happy '
                                               'to get you on board!')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'I am Cognitive HR Robot, I can guide you what you have to do today in '
                                               'the company to make the process of adaptation easier, '
                                               'faster & more interesting.')
        time.sleep(6)
        bot.send_message(message.from_user.id, 'I am also able to manage all routing and reporting process between you,'
                                               ' your Supervisor and Buddy to save your time.')
        time.sleep(4)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Hello! I am ready to go!')
        bot.send_message(message.from_user.id, 'Use custom keyboard below to reply back and lets get started',
                         reply_markup=user_markup)
    if message.text == 'Hello! I am ready to go!':
        bot.send_message(message.from_user.id, 'First thing is simple administration part')
        time.sleep(2)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Nice! Loving it!')
        bot.send_message(message.from_user.id, 'You have to get all equipment you need (computer, '
                                               'telephone, badge, etc.)', reply_markup=user_markup)
    if message.text == 'Nice! Loving it!':
        bot.send_message(message.from_user.id, 'Arrange a meeting with your Buddy who will help you '
                                               'during an integration period')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'He will do an another cool things also')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Like introducing you to the team')
        time.sleep(2)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Gotcha! What else I can ask my Buddy to help with?')
        bot.send_message(message.from_user.id,
                         'Arranging a tour around the Office and your workplace',
                         reply_markup=user_markup)
    if message.text == 'Gotcha! What else I can ask my Buddy to help with?':
        bot.send_message(message.from_user.id, 'Well, he will provide you basic '
                                               'information about how to book conference rooms,')
        time.sleep(3)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Some process for my performance & development?')
        bot.send_message(message.from_user.id,
                         'how to use communication systems such as Outlook, phone book, '
                         'instant messenger (MS Lync) etc.',
                         reply_markup=user_markup)
    if message.text == 'Some process for my performance & development?':
        bot.send_message(message.from_user.id, 'Yeah, so there a few steps for the first time:')
        time.sleep(3)
        bot.send_message(message.from_user.id, '1. Ask your Buddy to take you to "Environment, Health and Safety"'
                                               ' and to "Information Services" trainings')
        time.sleep(5)
        bot.send_message(message.from_user.id, '2. Then your Supervisor will review your Job Description '
                                               'and discuss your main accountabilities')
        time.sleep(5)
        bot.send_message(message.from_user.id, '3. You also have to learn about the PMU On-Boarding Tool and get '
                                               'Welcome Word from PMU Managing Director online')
        time.sleep(5)
        url_button = telebot.types.InlineKeyboardButton('PMU', url='http://workpoint.pmiapps.biz/teams'
                                                                   '/HRTS1/PIT/default.aspx')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "Find this info under this link:", reply_markup=inline_keyboard)
        bot.send_message(message.from_user.id, '4. Learn the Guide Book of Success (The PMI Code of Conduct) and '
                                               'Principles & Practices relevant for your Department')
        time.sleep(6)
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton('PMI', url='http://pmiprinciples.app.pmi/English/_layouts/PMI/'
                                                                   'PPP/FrontEnd/index.aspx?c=Ukraine&tabNumber=1')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "Take the links:", reply_markup=inline_keyboard)
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton('PP', url='http://guidebookforsuccess.pmiapps.biz/'
                                                                  'Pages/home.aspx')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "and", reply_markup=inline_keyboard)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('kk, any review after?')
        bot.send_message(message.from_user.id, 'Checked it?', reply_markup=user_markup)
    if message.text == 'kk, any review after?':
        bot.send_message(message.from_user.id, 'Great question!')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Yes, definitely!')
        time.sleep(1)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Awesome! Thank you!')
        bot.send_message(message.from_user.id, 'Share your first feedback Supervisor at the end of the day and '
                                               'review the plan for the [first week](http://workpoint.pmiapps.biz/teams/'
                                               'HRTS1/PIT/Documents/For%20New%20Comer/02.'
                                               '%20New%20Comer%20First%20Week.pdf)', reply_markup=user_markup,
                                               parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Awesome! Thank you!':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Thanks, bye!')
        bot.send_message(message.from_user.id, 'Have a great day! See you later.', reply_markup=user_markup)
    if message.text == 'Thanks, bye!':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Use commands below', reply_markup=user_markup)

#====================================  First week ===========================================

    if message.text == '1st week':
        bot.send_message(message.from_user.id, 'Hey New Comer :)')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'This is your first week in Phillip Morris which is an engaging and '
                                               'excitingperiod when you learn more about the Company.')
        time.sleep(4)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Hey! Great! Tell me.')
        bot.send_message(message.from_user.id, 'I will introduce you a list of things that should be done.',
                         reply_markup=user_markup)
    if message.text == 'Hey! Great! Tell me.':
        bot.send_message(message.from_user.id, 'Yeah, so basically it will be a first week guide line.')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'First a couple of things are about administration of the stuff.')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'Basically it is:')
        time.sleep(1)
        bot.send_message(message.from_user.id, '1. Checking if you have all equipment you need to perform your job'
                                               'You can contact HelpDesk (HelpDeskUkraine.pmi@pmi.com) for help, '
                                               'or ask your @Supervisor or @Buddy for assistance')
        time.sleep(5)
        bot.send_message(message.from_user.id, '2. Learning about [PMUBenefits](http://workpoint.pmiapps.biz/teams/'
                                               'HRTS2/ECABU/Pages/default.aspx)',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, '3. Learning about [OfficeSupportServices](http://workpoint.pmiapps.biz/'
                                               'teams/SSTS2/PGS/Pages/default.aspx) '
                                               'where you can find all issues, connected to administrative services.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id, '4. Getting an information about how to arrange [BusinessTrips](http://'
                                               'workpoint.pmiapps.biz/teams/SSTS2/PBT/Pages/default.aspx).'
                                               'You have to keep the [list](http://workpoint.pmiapps.biz/teams/SSTS2/PBT'
                                               '/Travel%20docs/PMU-PMSD%20Travel%20Coordinators%20Oct%2013%202015.xlsx) '
                                               'of departments and regional offices '
                                               'assistants at hand to clarify any travel-related questions.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(6)
        bot.send_message(message.from_user.id, '5. Learning about [IMDLplatform](http://imdl-service.app.pmi/) '
                                               'that allows to request different accesses and roles '
                                               'to internal PMU/PMI systems.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id, 'You can also ask your @Buddy to help here.')
        time.sleep(2)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Cool, awesome! Thanks!')
        bot.send_message(message.from_user.id, '6. Reviewing Records and Information Management Platform ([RIM](http://'
                                               'www.intranet.pmi/UA/eng/EMPSERVICES/RIM/content/Default.aspx)) '
                                               'with your Buddy and learn RIM principles.', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Cool, awesome! Thanks!':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Anything regarding my performance & development ?')
        bot.send_message(message.from_user.id, 'You welcome!', reply_markup=user_markup)
    if message.text == 'Anything regarding my performance & development ?':
        bot.send_message(message.from_user.id, 'For sure!')
        time.sleep(1)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('That\'s clear, what else ?')
        bot.send_message(message.from_user.id, 'You have to continue learning PMI Principles and Practices '
                                               '([PMI CompliancePlatform](http://www.intranet.pmi/hq/depts/compl/'
                                               'content/default.aspx) related to your job.', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'That\'s clear, what else ?':
        bot.send_message(message.from_user.id, 'Yeah, just making sure you remember that.')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'You have to learn PMU Structure and Departments')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Take the useful links: [PMU Organizational Chart](http://charts.pmi/'
                                               'published/UA/UA_Orgchart.htm), [PMU Departments OnePlacePages](http://'
                                               'oneplace.pmiapps.biz/)',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Then, complete [Video Intro Courses](http://workpoint.pmiapps.biz/'
                                               'teams/HRTS1/PIT/Lists/Intro%20360%20Homepage/AllItems.aspx) '
                                               'to learn PMU Functions and watch [Kharkiv Factory Online 3D Tour]'
                                               '(http://workpoint.pmiapps.biz/teams/OPTS2/KFO3T/Pages/default.aspx)',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Also, take your Buddy and learn more about [YourHR Self-Service Portal]'
                                               '(https://pmichsaphrp01.app.pmi/pmintl.com~hrss2g~web~main/UI) '
                                               'and [iLearn Platform](http://www.intranet.pmi/hq/depts/is/fg/hrsystm/'
                                               'content/services/ishrsyst_ilearn.aspx)',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('How to start that course?')
        bot.send_message(message.from_user.id, 'Then... good thing is to learn about [PMI Global Functions](http://'
                                               'www.intranet.pmi/HQ/DEPTS/content/GlobalFunctions.aspx) '
                                               'and complete PMI Introduction e-learning.', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'How to start that course?':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Thanks!')
        bot.send_message(message.from_user.id, 'Good question! You open the *On-line program* there, then access '
                                               'through YourHR Self-Service Portal iLearn, search in catalogue '
                                               '*Introduction Tool* and click *Start Course*', reply_markup=user_markup)
    if message.text == 'Thanks!':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Woah, let me know :)')
        bot.send_message(message.from_user.id, 'That is not a final thing :)', reply_markup=user_markup)
    if message.text == 'Woah, let me know :)':
        bot.send_message(message.from_user.id, 'You also have to learn about Managing and Apprising process ([MAP]'
                                               '(http://workpoint.pmiapps.biz/references/WIKI3/MATR/Wiki%20Page'
                                               '/Home.aspx)) and complete MAP e-learning.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Got it, cool!')
        bot.send_message(message.from_user.id, 'And finally discuss [Integration Objectives](http://workpoint.pmiapps.'
                                               'biz/references/WIKI3/MATR/Wiki%20Page/Interim%20Review%20(IRW).aspx) '
                                               'for the first [90 days](http://workpoint.pmiapps.biz/teams/HRTS1/PIT/'
                                               'Documents/For%20New%20Comer/03.%20New%20Comer%2090%20Days.pdf) '
                                               'and [Development Plan](http://video.app.pmi/viewerportal/pmi/'
                                               'contentprovider.do;jsessionid=nosession?eventContentId=68791) '
                                               'with your Supervisor and fill [Interim Review Form](http://video.app.'
                                               'pmi/viewerportal/pmi/contentprovider.do;jsessionid='
                                               'nosession?eventContentId=69086)', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Got it, cool!':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Anything regarding culture, network building?')
        bot.send_message(message.from_user.id, 'Yeah!', reply_markup=user_markup)
    if message.text == 'Anything regarding culture, network building?':
        bot.send_message(message.from_user.id, 'Yes, so just discuss with your Buddy regarding office practicers, '
                                               'breaks, working hours, dress code, '
                                               'smoking rules, vacation procedure etc.')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'Then review [PMI abbreviations](http://workpoint.pmiapps.biz/teams/'
                                               'HRTS1/PIT/Documents/Supporting%20Files/PMI_Abbreviations.pdf) '
                                               'list with him',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Sounds good! any process review?')
        bot.send_message(message.from_user.id, 'And attend a follow-up meeting with him', reply_markup=user_markup)
    if message.text == 'Sounds good! any process review?':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Thank you!')
        bot.send_message(message.from_user.id, 'Sure, finally at the end of first week meet with your @Supervisor '
                                               'and discuss your integration progress!', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Thank you!':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'You are welcome! See you!', reply_markup=user_markup)

    # ====================================  First 90 days ===========================================

    if message.text == '1st 90 days':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
    if message.text == '1st year':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
#______________________________________________________________________________
#---------------------Message handlers: for 'Buddy' choise---------------------
#______________________________________________________________________________

    if message.text == 'Buddy':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('1st daу', '1st wееk')
        user_markup.row('1st 90 daуs')
        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == '1st daу':
        bot.send_message(message.from_user.id, 'Hey Mister! Congratulations, you have become a Buddy!')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'This is a very important role in our Company, as Buddy is the person '
                                               'who can help New Comer to adapt to Company fast and engaging. '
                                               'You should prepare to meet New Comer together with the Supervisor')
        time.sleep(4)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Hey, ok cool! Give me an info about New Comer')
        bot.send_message(message.from_user.id, 'Which will happen tomorrow!', reply_markup=user_markup)
    if message.text == 'Hey, ok cool! Give me an info about New Comer':
        url_button = telebot.types.InlineKeyboardButton('New comer\'s CV', url='work.ua')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "Yes, sure! Here you go:", reply_markup=inline_keyboard)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Ok, thanks! What I need to do?')
        bot.send_message(message.from_user.id, 'Checked it?', reply_markup=user_markup)
    if message.text == 'Ok, thanks! What I need to do?':
        bot.send_message(message.from_user.id, 'There are few simple steps')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'First thing is you have to be aware of all needs of New Comer '
                                               'during the first period and be ready to help '
                                               'Supervisor of New Comer to arrange them')
        time.sleep(4)
        bot.send_message(message.from_user.id, 'Then, together with Supervisor, inform other team members and reception'
                                               ' about the arrival of New Comer')
        time.sleep(3)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Got it, who is a Supervisor?')
        bot.send_message(message.from_user.id, 'And of course you have to agree with his Supervisor the plan of your '
                                               'actions during the integration process', reply_markup=user_markup)
    if message.text == 'Got it, who is a Supervisor?':
        url_button = telebot.types.InlineKeyboardButton('Supervisor info', url='http://lotr.wikia.com/wiki/Gandalf')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "One sec, here is the PM link to him:", reply_markup=inline_keyboard)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Ok, anything else?')
        bot.send_message(message.from_user.id, 'Checked it?', reply_markup=user_markup)
    if message.text == 'Ok, anything else?':
        bot.send_message(message.from_user.id, 'Yep, take a look please of On-Boarding Tool and '
                                               'Welcome Word from PMU Managing Director')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'And get prepared to present it to New Comer')
        time.sleep(2)
        url_button = telebot.types.InlineKeyboardButton('OnBoarding', url='http://workpoint.pmiapps.biz/teams/HRTS1/PIT/default.aspx')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "here are the direct links to that info:", reply_markup=inline_keyboard)
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton('WelcomeWord', url='http://oneplace.pmiapps.biz/')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "and", reply_markup=inline_keyboard)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Remember, New Comer first time will be tomorrow at 10 am!')
        time.sleep(3)
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Awesome! Thank you for the support!')
        bot.send_message(message.from_user.id, 'I set an event in your calendar for it!', reply_markup=user_markup)
    if message.text == 'Awesome! Thank you for the support!':
        user_markup.row('/prior_to_start', '/stop')
        user_markup.row('Bye')
        bot.send_message(message.from_user.id, 'You are welcome! See you tomorrow, will ping you!', reply_markup=user_markup)
    if message.text == 'Bye':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Have a nice day!',
                         reply_markup=user_markup)
    if message.text == '1st wееk':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)
    if message.text == '1st 90 daуs':
        user_markup.row('/prior_to_start', '/stop')
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)


#---------------------Message handlers: for 'Recruiter' choise---------------------

    if message.text == 'Recruiter':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)


bot.polling(none_stop=True, interval=0)

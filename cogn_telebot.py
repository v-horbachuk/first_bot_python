#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import time

#My_TOKEN: 408316237:AAGFODWWvu-6mOXRBc_klCIlDKV_5lPATMk

bot = telebot.TeleBot('350637828:AAHlEKLAi_WSV0JGixo5kpZvy6un88-PoNk')

#---------------------Message handlers: for commands---------------------

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Неу!')
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    user_markup.row('NEW COMER', 'BUDDY', 'SUPERVISOR')
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

    if message.text == 'SUPERVISOR':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row('Before Start', 'Day 1', 'Week 1')
        user_markup.row('1st Month - 90 Days', 'Year 1st')

        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == 'Before Start':
        user_markup.row('Hey! Great, do it!')
        bot.send_message(message.from_user.id, 'Hey Supervisor! I\'m going to give a quick guide to be prepared for New Comer',
                         reply_markup=user_markup)

    if message.text == 'Hey! Great, do it!':
        bot.send_message(message.from_user.id,
                         'First part is ADMINISTRATION\'s part')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'You have to prepare working place for your New Comer via Administration Department: Working Place/Name Plate/Badge and Necessary Stationary')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         '[Email to Administration](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Letter%20to%20Administation.msg) for Kyiv HQ and Factory or contact your local Supervisor Regional Administration for Regional Offices', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Then check if You have received an IMDL request for New Comer’s account (in your Outlook) an activated it by following the link from the Outlook message or via [My Approvals](https://myapprovals.pmiaapps.bizx)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('Ok, other stuff ?')
        bot.send_message(message.from_user.id,
                         'And finally request the [necessary IS equipment](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Letter%20to%20IS%20Help%20Desk.msg) (PC, phone, etc.) & [accesses](http://imdl-service.app.pmi) to shared drives for your New Comer', reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Ok, other stuff ?':
        bot.send_message(message.from_user.id,
                         'Yeah, so pls ensure you have the Job Description for your New Comer prepared')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'HR or Supervisor Regional Administration will arrange for New Comer the “must-have” training on the 1st Day: Environment, Health and Safety Training and Information Services Training')
        time.sleep(2)
        user_markup.row('Awesome, give the culture\'s level')
        bot.send_message(message.from_user.id,
                         'Review the Inductions available for New Comer and select the applicable modules (Intro 360 Video, Kharkiv Factory Online 3D Tour, Registration to Introduction Trainings Into Functions)', reply_markup=user_markup)

    if message.text == 'Awesome, give the culture\'s level':
        bot.send_message(message.from_user.id,
                         'Sure, you have to inform your team and colleagues about a New Comer')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Pre-select [Buddy](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Who_is_Buddy.pdf) (the peer who has worked about 1 year in similar position) to support the New Comer', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('OK, that makes sense.')
        bot.send_message(message.from_user.id,
                         'And basically that\'s it. Next level – Checklist for the First Day', reply_markup=user_markup)

    if message.text == 'OK, that makes sense.':
        bot.send_message(message.from_user.id,
                         'See you later!')


    if message.text == 'Day 1':
        bot.send_message(message.from_user.id, 'Hey Mister! You are Supervisor and you have only one opportunity to make a first impression.')
        time.sleep(2)
        user_markup.row('Then lets crush it')
        bot.send_message(message.from_user.id, 'Try to make the First Day positively memorable for your New Comer. I will provide you a short guide to help you with it.',
                         reply_markup=user_markup)

    if message.text == 'Then lets crush it':
        bot.send_message(message.from_user.id, 'Ok, first thing check if New Comer got all equipment, he/she needs (computer, telephone, badge, etc.)')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Welcome and greet New Comer. Introduce him/her to your Team, Department Head and other colleagues')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Introduce Buddy to New Comer')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Show New Comer the Office and his/her workplace')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Arrange lunch with New Comer')
        time.sleep(2)
        user_markup.row('I\'m the best here :) Other?')
        bot.send_message(message.from_user.id, 'Ensure that Buddy explained New Comer basic information such as how to book conference rooms, how to use communication systems including phone book and instant messaging (MS Lync) etc.', reply_markup=user_markup)

    if message.text == 'I\'m the best here :) Other?':
        bot.send_message(message.from_user.id,
                         'That is great to hear! ;)')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'You also have to Send New Comer to Environment, Health and Safety Training and Information Systems Training')
        time.sleep(4)
        bot.send_message(message.from_user.id,
                         'Then provide New Comer with the [Job Description](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Job%20Description%20Template.doc) and discuss main accountabilities', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id,
                         'Familiarize New Comer with Company [Intranet](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id,
                         'Present [PMU On-Boarding Tool](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/default.aspx) and Welcome Word from PMU Managing Director to New Comer', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id,
                         'Introduce the [Guide Book of Success](https://guidebookforsuccess.pmiapps.biz/Pages/home.aspx) (The PMI Code of Conduct) and [Principles & Practices](http://pmiprinciples.app.pmi/English/_layouts/PMI/PPP/FrontEnd/index.aspx?c=Ukraine&tabNumber=1) relevant for your Department', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        user_markup.row('Thanks for help! Awesome!')
        bot.send_message(message.from_user.id,
                         'And finally collect the first feedback from New Comer and agree the plan for the first week with him/her', reply_markup=user_markup)

    if message.text == 'Thanks for help! Awesome!':
        bot.send_message(message.from_user.id,
                         'Just make it happen in best way!')


    if message.text == 'Week 1':
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)

    if message.text == '1st Month - 90 Days':
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)

    if message.text == 'Year 1st':
        bot.send_message(message.from_user.id, 'Sorry! This part is under construction. Try again later!',
                         reply_markup=user_markup)


#__________________________________________________________________________________
#---------------------Message handlers: for 'New Comer' choise---------------------
#__________________________________________________________________________________

    if message.text == 'NEW COMER':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row('First Day', 'First Week')
        user_markup.row('First 90 Days', 'First Year')
        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == 'First Day':
        bot.send_message(message.from_user.id, 'Welcome to Phillip Morris! It is your first day, happy '
                                               'to get you on board!')
        time.sleep(3)
        bot.send_message(message.from_user.id, 'I am Cognitive HR Robot, I can guide you what you have to do today in '
                                               'the company to make the process of adaptation easier, '
                                               'faster & more interesting.')
        time.sleep(4)
        bot.send_message(message.from_user.id, 'I am also able to manage all routing and reporting process between you,'
                                               ' your Supervisor and Buddy to save your time.')
        time.sleep(4)
        user_markup.row('Hello! I am ready to go!')
        bot.send_message(message.from_user.id, 'Use custom keyboard below to reply back and lets get started',
                         reply_markup=user_markup)
    if message.text == 'Hello! I am ready to go!':
        bot.send_message(message.from_user.id, 'First thing is simple administration part')
        time.sleep(2)
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
        user_markup.row('Gotcha! What else I can ask my Buddy to help with?')
        bot.send_message(message.from_user.id,
                         'Arranging a tour around the Office and your workplace',
                         reply_markup=user_markup)
    if message.text == 'Gotcha! What else I can ask my Buddy to help with?':
        bot.send_message(message.from_user.id, 'Well, he will provide you basic '
                                               'information about how to book conference rooms,')
        time.sleep(3)
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
        time.sleep(3)
        bot.send_message(message.from_user.id, '2. Then your Supervisor will review your Job Description '
                                               'and discuss your main accountabilities')
        time.sleep(3)
        bot.send_message(message.from_user.id, '3. You also have to learn about the PMU On-Boarding Tool and get '
                                               'Welcome Word from PMU Managing Director online')
        time.sleep(3)
        url_button = telebot.types.InlineKeyboardButton('PMU', url='http://workpoint.pmiapps.biz/teams'
                                                                   '/HRTS1/PIT/default.aspx')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "Find this info under this link:", reply_markup=inline_keyboard)
        bot.send_message(message.from_user.id, '4. Learn the Guide Book of Success (The PMI Code of Conduct) and '
                                               'Principles & Practices relevant for your Department')
        time.sleep(3)
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
        user_markup.row('kk, any review after?')
        bot.send_message(message.from_user.id, 'Checked it?', reply_markup=user_markup)
    if message.text == 'kk, any review after?':
        bot.send_message(message.from_user.id, 'Great question!')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Yes, definitely!')
        time.sleep(1)
        user_markup.row('Awesome! Thank you!')
        bot.send_message(message.from_user.id, 'Share your first feedback Supervisor at the end of the day and '
                                               'review the plan for the [first week](http://workpoint.pmiapps.biz/teams/'
                                               'HRTS1/PIT/Documents/For%20New%20Comer/02.'
                                               '%20New%20Comer%20First%20Week.pdf)', reply_markup=user_markup,
                                               parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Awesome! Thank you!':
        user_markup.row('Thanks, bye!')
        bot.send_message(message.from_user.id, 'Have a great day! See you later.', reply_markup=user_markup)
    if message.text == 'Thanks, bye!':
        bot.send_message(message.from_user.id, 'Use commands below', reply_markup=user_markup)

#====================================  First week ===========================================

    if message.text == 'First Week':
        bot.send_message(message.from_user.id, 'Hey New Comer :)')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'This is your first week in Phillip Morris which is an engaging and '
                                               'excitingperiod when you learn more about the Company.')
        time.sleep(3)
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
        time.sleep(3)
        bot.send_message(message.from_user.id, '2. Learning about [PMUBenefits](http://workpoint.pmiapps.biz/teams/'
                                               'HRTS2/ECABU/Pages/default.aspx)',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, '3. Learning about [OfficeSupportServices](http://workpoint.pmiapps.biz/'
                                               'teams/SSTS2/PGS/Pages/default.aspx) '
                                               'where you can find all issues, connected to administrative services.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
        bot.send_message(message.from_user.id, '4. Getting an information about how to arrange [BusinessTrips](http://'
                                               'workpoint.pmiapps.biz/teams/SSTS2/PBT/Pages/default.aspx).'
                                               'You have to keep the [list](http://workpoint.pmiapps.biz/teams/SSTS2/PBT'
                                               '/Travel%20docs/PMU-PMSD%20Travel%20Coordinators%20Oct%2013%202015.xlsx) '
                                               'of departments and regional offices '
                                               'assistants at hand to clarify any travel-related questions.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
        bot.send_message(message.from_user.id, '5. Learning about [IMDLplatform](http://imdl-service.app.pmi/) '
                                               'that allows to request different accesses and roles '
                                               'to internal PMU/PMI systems.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
        bot.send_message(message.from_user.id, 'You can also ask your @Buddy to help here.')
        time.sleep(2)
        user_markup.row('Cool, awesome! Thanks!')
        bot.send_message(message.from_user.id, '6. Reviewing Records and Information Management Platform ([RIM](http://'
                                               'www.intranet.pmi/UA/eng/EMPSERVICES/RIM/content/Default.aspx)) '
                                               'with your Buddy and learn RIM principles.', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Cool, awesome! Thanks!':
        user_markup.row('Anything regarding my performance & development ?')
        bot.send_message(message.from_user.id, 'You welcome!', reply_markup=user_markup)
    if message.text == 'Anything regarding my performance & development ?':
        bot.send_message(message.from_user.id, 'For sure!')
        time.sleep(1)
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
        user_markup.row('How to start that course?')
        bot.send_message(message.from_user.id, 'Then... good thing is to learn about [PMI Global Functions](http://'
                                               'www.intranet.pmi/HQ/DEPTS/content/GlobalFunctions.aspx) '
                                               'and complete PMI Introduction e-learning.', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'How to start that course?':
        user_markup.row('Thanks!')
        bot.send_message(message.from_user.id, 'Good question! You open the *On-line program* there, then access '
                                               'through YourHR Self-Service Portal iLearn, search in catalogue '
                                               '*Introduction Tool* and click *Start Course*', reply_markup=user_markup)
    if message.text == 'Thanks!':
        user_markup.row('Woah, let me know :)')
        bot.send_message(message.from_user.id, 'That is not a final thing :)', reply_markup=user_markup)
    if message.text == 'Woah, let me know :)':
        bot.send_message(message.from_user.id, 'You also have to learn about Managing and Apprising process ([MAP]'
                                               '(http://workpoint.pmiapps.biz/references/WIKI3/MATR/Wiki%20Page'
                                               '/Home.aspx)) and complete MAP e-learning.',
                                                parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(3)
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
        user_markup.row('Sounds good! any process review?')
        bot.send_message(message.from_user.id, 'And attend a follow-up meeting with him', reply_markup=user_markup)
    if message.text == 'Sounds good! any process review?':
        user_markup.row('Thank you!')
        bot.send_message(message.from_user.id, 'Sure, finally at the end of first week meet with your @Supervisor '
                                               'and discuss your integration progress!', reply_markup=user_markup,
                                                parse_mode='markdown', disable_web_page_preview=True)
    if message.text == 'Thank you!':
        bot.send_message(message.from_user.id, 'You are welcome! See you!', reply_markup=user_markup)

    # ====================================  First 90 days ===========================================

    if message.text == 'First 90 Days':
        bot.send_message(message.from_user.id, 'Hello dear New Comer ;)')
        time.sleep(1)
        bot.send_message(message.from_user.id,
                         'I am going to tell you about a plan of super exiting period - First 90 Days')
        time.sleep(2)

        user_markup.row('Yo my Cognitive one! Give me more info!')
        bot.send_message(message.from_user.id,
                         'Basically it is about focusing on delivering first results, learning the job, company culture and network building.',
                         reply_markup=user_markup)
    if message.text == 'Yo my Cognitive one! Give me more info!':
        bot.send_message(message.from_user.id, 'So there are 3 main phases:')
        time.sleep(1)
        bot.send_message(message.from_user.id, '1. Performance & Development')
        time.sleep(2)
        bot.send_message(message.from_user.id, '2. Internal Communication & Network Building')
        time.sleep(1)

        user_markup.row('Ready to go deeper!')
        bot.send_message(message.from_user.id, '3. Progress review', reply_markup=user_markup)
        time.sleep(2)

    if message.text == 'Ready to go deeper!':
        bot.send_message(message.from_user.id, 'Great!')
        time.sleep(1)
        bot.send_message(message.from_user.id,
                         'First thing you have to attend relevant local in-class induction into Functions:')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Commercial & Field visit')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Operations & Factory Tour')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Support Functions: Finance, HR, IS, Legal, CA')
        time.sleep(1)
        user_markup.row('Wow! That is prerry interesting!')
        bot.send_message(message.from_user.id,
                         'take the link and ask your Supervisor for signing in into the relevant trainings',
                         reply_markup=user_markup)
        bot.send_message(message.from_user.id,
                         '[Kharkiv Factory Online 3D Tour](https://workpoint.pmiapps.biz/teams/OPTS2/KFO3T/Pages/default.aspx)',
                         parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Wow! That is pretty interesting!':
        bot.send_message(message.from_user.id, 'That is only a start :)')
        time.sleep(1)
        bot.send_message(message.from_user.id,
                         'Next things you have to complete online training “Understanding People Management”, if you are a people manager')
        time.sleep(1)
        bot.send_message(message.from_user.id,
                         'Also complete all Compliance trainings applicable for your Job, - you will get an email with list of them.')
        time.sleep(1)
        bot.send_message(message.from_user.id,
                         'Then study an info on all tobacco issues, learn about Career Stages and Talent Management approach')
        time.sleep(1)

        user_markup.row('Oh nice! What\'s under communication stuff ?')
        bot.send_message(message.from_user.id,
                         '[Tobacco regulation issues](https://www.pmi.com/our-business/about-us/our-views/regulation)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        bot.send_message(message.from_user.id,
                         '[Career Stages Guide](http://www.intranet.pmi/HQ/DEPTS/HR/Acti/MAP/content/Career_Stages_at_PMI_FLASH_page.aspx)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        bot.send_message(message.from_user.id,
                         '[Talent Review Process](https://workpoint.pmiapps.biz/references/WIKI3/MATR/Wiki%20Page/Talent%20Review.aspx)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Oh nice! What\'s under communication stuff ?':
        bot.send_message(message.from_user.id,
                         'Yep, first one is you have to learn  PMI 7 Key Behaviors and understand how they relate to the job')
        bot.send_message(message.from_user.id,
                         '[PMI 7 Key Behaviors](http://pmicore.pmiapps.biz/Pages/behaviors/home.aspx)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Then please establish the necessary network among colleagues and peers. Your Buddy can help you here.')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'And last thing is being aware about the Internal Communication Channels:')
        bot.send_message(message.from_user.id,
                         '[PMU Engagement Program](https://stsprd01.pmiapps.biz/adfs/ls/IdpInitiatedSignon.aspx?RelayState=RPID%3Dhttps%253A%252F%252Fwww.successfactors.eu%26RelayState%3Dhttps%253A%252F%252Fperformancemanager.successfactors.eu%252Fsaml2%252FSAMLAssertionConsumer%253Fcompany%253DPMI)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         '[Aromat – PMU Corporate Magazine](http://www.intranet.pmi/UA/eng/NEWS/PMUNewsletter/content/Aromat.aspx)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         '[Lunch & Learn - sessions with PMU Management](http://video.app.pmi/viewerportal/pmi/channel.do?channelId=esc_prg_cntr_chn:2852)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         '[PMU & PMI](https://login.pmiapps.biz/my.policy)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)

        bot.send_message(message.from_user.id,
                         'Aaaaand fresh information about cultural life and events in Ukraine:')

        user_markup.row('Thank you, now we are talking!')
        bot.send_message(message.from_user.id,
                         '[LAMP Newsletter](https://workpoint.pmiapps.biz/teams/BBTS1/UPC/LAMP%20Newsletter/Forms/AllItems.aspx)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)

    if message.text == 'Thank you, now we are talking!':
        user_markup.row('Give me the process review part')
        bot.send_message(message.from_user.id, 'Glad you like that!',
                         reply_markup=user_markup)
        time.sleep(2)

    if message.text == 'Give me the process review part':
        bot.send_message(message.from_user.id,
                         'Yeah, so basically you have to have  follow-up meeting with your Buddy for review of your integration process')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Then provide your feedback to HR on Integration Process you’ve experienced')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'And finally meet with Supervisor to discuss your integration period progress and setup new objectives for the next period')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Links below could be useful for you:')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         '[How to prepare for Integration Review meeting (MAP)](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/NC_How_to_prepare_for_integration_meeting_MAP.pdf)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)
        user_markup.row('Great! I\'m surer excited!')
        bot.send_message(message.from_user.id,
                         '[How to prepare for Integration Review meeting (FTO)](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/NC_How_to_prepare_for_integration_meeting_FTO.pdf)',
                         reply_markup=user_markup,
                         parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Great! I\'m surer excited!':
        bot.send_message(message.from_user.id, 'Seee you! :)')


    if message.text == 'First Year':
        bot.send_message(message.from_user.id, 'Hey man, I\'m going to tell you regarding First Year checklist')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'The first year in the company is the time when you become fully aware of what you are expected to do, start contributing and building effective working relations and network.')
        time.sleep(2)
        user_markup.row('Hey, give this list!')
        bot.send_message(message.from_user.id, 'The checklist for this period will help you to review all key points for New Comer.', reply_markup=user_markup)


    if message.text == 'Hey, give this list!':
        bot.send_message(message.from_user.id, 'So the first main part is COMPANY STRATEGIC GOALS AND VALUES which include items below:')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you know the [company\'s strategy](http://www.intranet.pmi/HQ/PmiWorl/content/PMI_goals_strategies.aspx) and can explain it to new colleagues.', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you know [PMI 7 Key Behaviors](http://pmicore.pmiapps.biz/Pages/behaviors/home.aspx) and understands how they relate to your job', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you know [PMI Global Structure](http://www.intranet.pmi/HQ/PmiWorl/OrgChar/content/timevision.aspx) and roles of [Global Functions](http://www.intranet.pmi/HQ/DEPTS/content/GlobalFunctions.aspx)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('Ok, what about performance ?')
        bot.send_message(message.from_user.id, 'Ensure that you know [PMU overall structure, roles](http://charts.pmi/published/UA/UA_Orgchart.htm) of different departments and how they [collaborate cross- functionally](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d)', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Ok, what about performance ?':
        bot.send_message(message.from_user.id, 'Yes, main points below:')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you clearly understand how your job supports the company’s objectives and have clarity on the deliverables that would miss, meet or exceed your annual [performance objectives](http://video.app.pmi/viewerportal/pmi/contentprovider.do;jsessionid=nosession?eventContentId=69086)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you have actionable MAP Individual [Development Plan](http://video.app.pmi/viewerportal/pmi/contentprovider.do;jsessionid=nosession?eventContentId=68791), using the [70-20-10 principle](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/70-20-10_principle.pdf)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Attend fundamentals training on your personal and/or managerial effectiveness: for [Specialists](http://video.app.pmi/viewerportal/pmi/contentprovider.do;jsessionid=nosession?eventContentId=77319) and For [People Managers](http://video.app.pmi/viewerportal/pmi/contentprovider.do;jsessionid=nosession?eventContentId=77322)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that you know about [Career Development Principles](http://www.intranet.pmi/HQ/DEPTS/HR/Acti/MAP/content/Career_Stages_at_PMI_FLASH_page.aspx) and [Career Opportunities](https://workpoint.pmiapps.biz/references/HRRS1/PHJO/Lists/English/AllItems.aspx)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('Oh my God, it\'s a best company in the entire world!')
        bot.send_message(message.from_user.id, 'Ensure you have open dialogue with your Supervisor on your performance and development progress, as well as you give a [feedback](http://video.app.pmi/viewerportal/pmi/contentprovider.do;jsessionid=nosession?eventContentId=69080) on his/her leadership effectiveness', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Oh my God, it\'s a best company in the entire world!':
        bot.send_message(message.from_user.id, 'That is true!')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'The final piece in the process is INTERNAL COMMUNCATION & NETWORK BUILDING')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'You have to Ensure that you have built effective network within the company and know company’s Internal Communication Channels')
        time.sleep(2)
        user_markup.row('Thank you so much!')
        bot.send_message(message.from_user.id, 'And Ensure that you know company’s Employer Brand and actively contribute to [PMU Referral Program](https://workpoint.pmiapps.biz/references/HRRS1/PHJO/Lists/Employee%20Referral%20Program/AllItems.aspx)', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Thank you so much!':
        bot.send_message(message.from_user.id, 'You are Welcome!')



    #______________________________________________________________________________
#---------------------Message handlers: for 'Buddy' choise---------------------
#______________________________________________________________________________

    if message.text == 'BUDDY':
        user_markup.row('Prior to Start', '1st Day')
        user_markup.row('1st Week', '1st 90 Days')
        bot.send_message(message.from_user.id, 'Please, select time period', reply_markup=user_markup)
    if message.text == 'Prior to Start':
        bot.send_message(message.from_user.id, 'Hey Mister! Congratulations, you have become a Buddy!')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'This is a very important role in our Company, as Buddy is the person '
                                               'who can help New Comer to adapt to Company fast and engaging. '
                                               'You should prepare to meet New Comer together with the Supervisor')
        time.sleep(4)
        user_markup.row('Hey, ok cool! Give me an info about New Comer')
        bot.send_message(message.from_user.id, 'Which will happen tomorrow!', reply_markup=user_markup)
    if message.text == 'Hey, ok cool! Give me an info about New Comer':
        url_button = telebot.types.InlineKeyboardButton('New comer\'s CV', url='work.ua')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "Yes, sure! Here you go:", reply_markup=inline_keyboard)
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
        user_markup.row('Got it, who is a Supervisor?')
        bot.send_message(message.from_user.id, 'And of course you have to agree with his Supervisor the plan of your '
                                               'actions during the integration process', reply_markup=user_markup)
    if message.text == 'Got it, who is a Supervisor?':
        url_button = telebot.types.InlineKeyboardButton('Supervisor info', url='http://lotr.wikia.com/wiki/Gandalf')
        inline_keyboard.add(url_button)
        bot.send_message(message.from_user.id, "One sec, here is the PM link to him:", reply_markup=inline_keyboard)
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
        user_markup.row('Awesome! Thank you for the support!')
        bot.send_message(message.from_user.id, 'I set an event in your calendar for it!', reply_markup=user_markup)
    if message.text == 'Awesome! Thank you for the support!':
        user_markup.row('Bye')
        bot.send_message(message.from_user.id, 'You are welcome! See you tomorrow, will ping you!', reply_markup=user_markup)
    if message.text == 'Bye':
        bot.send_message(message.from_user.id, 'Have a nice day!')


    if message.text == '1st Day':
        bot.send_message(message.from_user.id, 'Hey Buddy! Game time! :)')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'You have only one opportunity to make a first impression.')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Try to make the First Day positively memorable for your New Comer.')
        time.sleep(2)
        user_markup.row('Hey dude! Yeah, guide me here, pls!')
        bot.send_message(message.from_user.id, 'Here is short checklist to help you.',
                         reply_markup=user_markup)

    if message.text == 'Hey dude! Yeah, guide me here, pls!':
        bot.send_message(message.from_user.id, 'Meet and greet New Comer. New Comer’s Supervisor should arrange this meeting')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Show New Comer the Office and his/her workplace')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Explain New Comer basic information such as how to book conference rooms, how to use communication systems including phone book and instant messaging (MS Lync) etc.')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Send New Comer to Environment, Health and Safety Training and Information Systems Training')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Familiarize New Comer with Company [Intranet](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('Sounds Easy! I\'m ready to go!')
        bot.send_message(message.from_user.id, 'Present [PMU On-Boarding Tool](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/default.aspx) and Welcome Word from PMU Managing Director to New Comer',
                         reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Sounds Easy! I\'m ready to go!':
        bot.send_message(message.from_user.id, 'Good luck!')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Make it happen!')



    if message.text == '1st Week':
        user_markup.row('Hey! Me too!')
        bot.send_message(message.from_user.id, 'Hey Buddy! Happy to ping you again!',
                         reply_markup=user_markup)

    if message.text == 'Hey! Me too!':
        bot.send_message(message.from_user.id, 'I want to provide you a checklist for the first week as a Buddy. Just a things that should be done')
        time.sleep(2)
        user_markup.row('Ready to pool the data :)')
        bot.send_message(message.from_user.id, 'The first week of New Comer’s integration should be engaging and he/she will have an opportunity to know more about the Company. The checklist for the first week will guide you how to help New Comer in this journey.',
                         reply_markup=user_markup)

    if message.text == 'Ready to pool the data :)':
        bot.send_message(message.from_user.id, 'There are a 4 main things: ADMINISTRATION, NEW COMER’S PERFORMANCE & DEVELOPMENT, PMI CULTURE & NETWORK BUILDING, PROGRESS REVIEW')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'The first part includes next things:')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'You have to ensure that New Comer has all equipment he/she needs to complete his/her job duties. You can contact HelpDeskUkraine.pmi@pmi.com for assistance')
        time.sleep(4)
        bot.send_message(message.from_user.id, 'Also review [IMDL platform](http://imdl-service.app.pmi) with New Comer that allows to request different accesses and roles to internal PMU/PMI systems', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id, 'Ensure that New Comer gets information about how to arrange [Business trips and travels](https://workpoint.pmiapps.biz/teams/SSTS2/PBT/Pages/default.aspx) and have the [list of the departments and regional offices’ assistants](https://workpoint.pmiapps.biz/teams/SSTS2/PBT/Travel%20docs/PMU-PMSD%20Travel%20Coordinators%20Oct%2013%202015.xlsx) at hand to clarify any travel-related questions', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        user_markup.row('Good, give me the next tasty ;)')
        bot.send_message(message.from_user.id, 'And review Information [Management Platform (RIM)](http://www.intranet.pmi/UA/eng/EMPSERVICES/RIM/content/Default.aspx) with New Comer to learn more about company’s information record', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Good, give me the next tasty ;)':
        bot.send_message(message.from_user.id, 'Next thing is ensuring that New Comer learns about [PMU Structure](http://charts.pmi/published/UA/UA_Orgchart.htm) and [Departments](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        bot.send_message(message.from_user.id, 'Ensure that New Comer completes [Video Induction Courses](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Lists/Intro%20360%20Homepage/AllItems.aspx) about PMU Functions and watches the [Kharkiv Factory Online 3D Tour](https://workpoint.pmiapps.biz/teams/OPTS2/KFO3T/Pages/default.aspx)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(4)
        user_markup.row('A nice!) Let\'s go to culture\'s part.')
        bot.send_message(message.from_user.id, 'And you have to navigate through [YourHR Self-Service Portal](https://pmichsaphrp01.app.pmi/pmintl.com~hrss2g~web~main/UI) and [iLearn Platform](http://www.intranet.pmi/hq/depts/is/fg/hrsystm/content/services/ishrsyst_ilearn.aspx) with New Comer', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'A nice!) Let\'s go to culture\'s part.':
        bot.send_message(message.from_user.id, 'Glad you are interested!')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'First you Provide information about office practices, breaks, working hours, dress code, smoking rules, vacation request procedure etc. to New Comer')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Then review [PMI abbreviations](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/PMI_Abbreviations.pdf) list with New Comer', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Engage other Colleagues to get acquainted with New Comer')
        time.sleep(2)
        user_markup.row('That\'s funny part :)')
        bot.send_message(message.from_user.id, 'And Arrange a follow-up meeting during the integration period with New Comer', reply_markup=user_markup)

    if message.text == 'That\'s funny part :)':
        bot.send_message(message.from_user.id, 'Yeah ;)')
        time.sleep(2)
        user_markup.row('No problem, will do that!')
        bot.send_message(message.from_user.id, 'And last thing by provess review perspective you have to Provide feedback on New Comer’s integration to @Supervisor', reply_markup=user_markup)

    if message.text == 'No problem, will do that!':
        bot.send_message(message.from_user.id, 'Then ok, have a productive time!')


    if message.text == '1st 90 Days':
        bot.send_message(message.from_user.id, 'Hey, I\'m going to give you a quick guide for your First 90 days as a Buddy!')
        user_markup.row('Yay! Loving it, sure, tell me!')
        bot.send_message(message.from_user.id, 'Ready to listen?',
                         reply_markup=user_markup)

    if message.text == 'Yay! Loving it, sure, tell me!':
        bot.send_message(message.from_user.id, 'Basically, what you have to do is')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure that New Comer established the necessary network among colleagues and peers')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Ensure New Comer is aware about the Internal Communication Channels within the company:')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                     '[We better & More Platform in JAM](https://stsprd01.pmiapps.biz/adfs/ls/IdpInitiatedSignon.aspx?RelayState=RPID%3Dhttps%253A%252F%252Fwww.successfactors.eu%26RelayState%3Dhttps%253A%252F%252Fperformancemanager.successfactors.eu%252Fsaml2%252FSAMLAssertionConsumer%253Fcompany%253DPMI) - PMU Engagement Program via PMI Social Network', parse_mode='markdown', disable_web_page_preview=True)
        bot.send_message(message.from_user.id, '[Aromat](http://www.intranet.pmi/UA/eng/NEWS/PMUNewsletter/content/Aromat.aspx) - Corporate magazine', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, '[Lunch & Learn](http://video.app.pmi/viewerportal/pmi/channel.do?channelId=esc_prg_cntr_chn:2852) - sessions with Management', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Organizational Announcements @ [PMU & PMI](https://oneplace.pmiapps.biz)', parse_mode='markdown', disable_web_page_preview=True)
        time.sleep(2)
        user_markup.row('Rodger that, what else ?')
        bot.send_message(message.from_user.id, '[LAMP Newsletter](https://workpoint.pmiapps.biz/teams/BBTS1/UPC/LAMP%20Newsletter/Forms/AllItems.aspx) - fresh information about cultural life and events in Ukraine', reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

    if message.text == 'Rodger that, what else ?':
        bot.send_message(message.from_user.id, 'Ok, another things to be done:')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Schedule and hold follow up meetings once a week during the first month and once in two weeks during second and third month to address New Comer’s queries and to check on the progress')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Meet with New Comer at the end of third month to review his/her checklist and to plan future actions from his/her sides to complete other tasks')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Provide feedback on New Comer\'s integration to his/her Supervisor')
        time.sleep(2)
        user_markup.row('Thnx, that\'s good to know')
        bot.send_message(message.from_user.id, 'Provide feedback to HR on Integration Process', reply_markup=user_markup)

    if message.text == 'Thnx, that\'s good to know':
        bot.send_message(message.from_user.id, 'Np, see you later!')



    #---------------------Message handlers: for 'Recruiter' choise---------------------

    if message.text == 'Recruiter':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row('/reboot', '/stop')
        user_markup.row('Get pic', 'Get sticker')
        bot.send_message(message.from_user.id, 'Anything else?', reply_markup=user_markup)


bot.polling(none_stop=True, interval=0)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import hashlib
import json
import re

#My_TOKEN: 408316237:AAGFODWWvu-6mOXRBc_klCIlDKV_5lPATMk

# bot = telebot.TeleBot('390870025:AAGlAcwly_JPNWPjeu8QNfQcFN9L-Pb7Wmo')
bot = telebot.TeleBot('468838039:AAFCpKr3ElV1XgW7Gf58Fexpgs-TfN7l8Xg')


def get_users_data(role):
	with open("users.json", "r") as f:
		all_users = json.load(f)
	for key, item in all_users.items():
		if item['role'] == role:
			user = dict()
			user['id'] = item['id']
			user['first_name'] = item['first_name']
			return user


class User(object):
	nc = get_users_data(1)
	b = get_users_data(2)
	s = get_users_data(3)
	hr = get_users_data(0)

	def __init__(self, email, role):
		self.email = email
		self.role = role
		self.hashed_email = self.generate_hash(email)
		self.telegram_user_id = None
		self.phone_number = None
		self.valid = 0
		self.first_name = None

	# ---------------------Function for SMTP---------------------
	@staticmethod
	def send_mail(email, hased_email):
		print(email, hased_email)
		fromaddr = "info@morbax.com"
		toaddr = str(email)
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Onboarding Experience"
		link = 'https://telegram.me/morbax_bot?start={0}'.format(hased_email)
		body = 'Hello dear friend. We are glad to invite you to our Telegram Onboarding Tool. Use the link to ' \
				   'discover this great experience! ' + '{0}'.format(link)
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('mail.ukraine.com.ua', 2525)
		server.starttls()
		server.login(fromaddr, "Morbax-2017")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
	# -------------------------------------------------------------

	@staticmethod
	def generate_hash(email):
		hash_code = hashlib.md5(email.encode('utf-8')).hexdigest()
		return hash_code

	@staticmethod
	def get_users():
		with open("users.json", "r") as f:
			users = json.load(f)
		return users

	def get_dict(self):
		user_dict = {'mail': self.email,
					 'hash': self.hashed_email,
					 'role': self.role,
					 'id': self.telegram_user_id,
					 'valid': self.valid,
					 'first_name': self.first_name}
		return user_dict

	def add_user(self, users):
		data = self.get_dict()
		users[self.hashed_email] = data
		users_json = json.dumps(users, ensure_ascii=False)
		with open("users.json", "w") as f:
			f.write(users_json)

	@staticmethod
	def enrange_users(users):
		users_json = json.dumps(users, ensure_ascii=False)
		with open("users.json", "w") as f:
			f.write(users_json)



#--------------------------------------------------------------------

#---------------------Functions for DEEP LINKING---------------------

def extract_unique_code(text):
	splitted = text.split()
	return splitted[1] if len(splitted) > 1 else None  # Extracts the unique_code from the sent /start command.

def reply_markup(message, bot_message, answer):
	user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	if isinstance(answer, list):
		user_markup.row(answer[0], answer[1])
	else:
		user_markup.row(answer)
	bot.send_message(message.from_user.id, bot_message, reply_markup=user_markup)


@bot.message_handler(commands=['start', 'restart'])
def redirect_to_jorney(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	unique_code = extract_unique_code(message.text)
	print(unique_code)
	users = User.get_users()
	if unique_code:                                        # if the '/start' command contains a unique_code
		user_role = users[unique_code]['role']
		print(message.chat.id)
		users[unique_code]['id'] = message.chat.id
		users[unique_code]['first_name'] = message.from_user.first_name
		User.enrange_users(users)
		if user_role == 0:
			bot.send_message(message.from_user.id, 'Нi dear HR Manager!')
			bot.send_message(message.from_user.id, 'What do you want me to help you with?')
			user_markup.row('LAUNCH A NEW ONBOARDING')
			bot.send_message(message.from_user.id, 'Please, select option below', reply_markup=user_markup)
		elif user_role == 1:
			user_markup.row('Rock on!')
			bot.send_message(message.from_user.id, 'Hi there, New comer!', reply_markup=user_markup)
		elif user_role == 3:
			user_markup.row('Let\'s go!')
			bot.send_message(message.from_user.id, 'Hi there, Supervisor!', reply_markup=user_markup)
		elif user_role == 2:
			user_markup.row('Chop Chop!')
			bot.send_message(message.from_user.id, 'Hi there, Buddy!', reply_markup=user_markup)
	else:
		for key, item in users.items():
			if item['id'] == message.from_user.id:
				user_role = item['role']
				if user_role == 0:
					bot.send_message(message.from_user.id, 'Нi dear HR Manager!')
					bot.send_message(message.from_user.id, 'What do you want me to help you with?')
					user_markup.row('LAUNCH A NEW ONBOARDING')
					bot.send_message(message.from_user.id, 'Please, select option below', reply_markup=user_markup)
				elif user_role == 1:
					user_markup.row('Rock on!')
					bot.send_message(message.from_user.id, 'Hi there, New comer!', reply_markup=user_markup)
				elif user_role == 3:
					user_markup.row('Let\'s go!')
					bot.send_message(message.from_user.id, 'Hi there, Supervisor!', reply_markup=user_markup)
				elif user_role == 2:
					user_markup.row('Chop Chop!')
					bot.send_message(message.from_user.id, 'Hi there, Buddy!', reply_markup=user_markup)
				elif user_role == 9:
					bot.send_message(message.from_user.id, 'Нi, Admin')
					bot.send_message(message.from_user.id, 'You have to add HR e-mail')
					user_markup.row('ADD HR E-MAIL')
				break
		else:
			user_markup.row('/stop')
			bot.send_message(message.from_user.id, "Please visit me via a provided URL from the website.", reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.from_user.id, 'Good luck =)', reply_markup=hide_markup)
#__________________________________________________________________________________
#---------------------Message handlers: for 'Admin's' choise---------------------
#__________________________________________________________________________________

@bot.message_handler(content_types=['text'])
def handle_hr(message):
	if message.text == 'ADD HR E-MAIL':
		bot.send_message(message.from_user.id, 'Type HR\'s e-mail like in the example \"h:E-MAIL\" without spaces and press Enter')
	if re.match(r'^h:', message.text):
		e_mail = message.text[2:].strip()  # save Newcomer's e-mail
		role = 0  # role == 1 ===> This is HR
		hr = User(e_mail, role)
		users = hr.get_users()
		hr.add_user(users)
		User.send_mail(hr.email, hr.hashed_email)
		user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		user_markup.row('ADD ANOTHER HR E-MAIL', '/stop')
		bot.send_message(message.from_user.id,
						 'HR got an invitation! Choose some options below', reply_markup=user_markup)
	if message.text == 'ADD ANOTHER HR E-MAIL':
		bot.send_message(message.from_user.id,
						 'Type HR\'s e-mail like in the example \"h:E-MAIL\" without spaces and press Enter')

#__________________________________________________________________________________
#---------------------Message handlers: for 'Recruiter's' choise---------------------
#__________________________________________________________________________________

	inline_keyboard = telebot.types.InlineKeyboardMarkup()
	user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	if message.text == 'LAUNCH A NEW ONBOARDING' or message.text == 'SETUP ANOTHER ONBOARDING':
		bot.send_message(message.from_user.id, 'Lets start from a New Comer')
		bot.send_message(message.from_user.id, 'Enter New Comer\'s email address like in the example \"n:E-MAIL\" without spaces')
		bot.send_message(message.from_user.id, 'An email is a mandatory field in our system')
	if re.match(r'^n:', message.text):
		e_mail = message.text[2:].strip() #save Newcomer's e-mail
		role = 1               # role == 1 ===> This is Newcomer
		newcomer = User(e_mail, role)
		users = newcomer.get_users()
		newcomer.add_user(users)
		bot.send_message(message.from_user.id,
					 'Ok, lets enter Budy\'s contact info')
		bot.send_message(message.from_user.id,
					 'Enter his email like in the example \"b:E-MAIL\" without spaces')
	if re.match(r'^b:', message.text):
		e_mail = message.text[2:].strip()  # save Newcomer's e-mail
		role = 2  # role == 2 ===> This is Buddy
		buddy = User(e_mail, role)
		users = buddy.get_users()
		buddy.add_user(users)
		bot.send_message(message.from_user.id,
					 'Ok, lets enter Supervisor\'s contact info')
		bot.send_message(message.from_user.id,
					 'Enter his email like in the example \"s:E-MAIL\" without spaces')
	if re.match(r'^s:', message.text):
		e_mail = message.text[2:].strip()  # save Newcomer's e-mail
		role = 3  # role == 3 ===> This is Supervisor
		supervisor = User(e_mail, role)
		users = supervisor.get_users()
		supervisor.add_user(users)
		user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		user_markup.row('INVITE')
		user_markup.row('SETUP ANOTHER ONBOARDING')
		bot.send_message(message.from_user.id,
						 'Ok, cool, seems like all set. Please, click button \'INVITE\'. Users will receive an email with link to HRBot to start onboarding process', reply_markup=user_markup)
	if message.text == 'INVITE':
		users = User.get_users()
		for key, item in users.items():
			if item['role'] == 1 and item['valid'] == 0:
				newcomer = User(item['mail'], item['hash'])
				item['valid'] = 1
				User.enrange_users(users)
			elif item['role'] == 2 and item['valid'] == 0:
				buddy = User(item['mail'], item['hash'])
				item['valid'] = 1
				User.enrange_users(users)
			elif item['role'] == 3 and item['valid'] == 0:
				supervisor = User(item['mail'], item['hash'])
				item['valid'] = 1
				User.enrange_users(users)
		User.send_mail(newcomer.email, newcomer.hashed_email)
		User.send_mail(buddy.email, buddy.hashed_email)
		User.send_mail(supervisor.email, supervisor.hashed_email)
		user_markup.row('SETUP ANOTHER ONBOARDING', '/stop')
		bot.send_message(message.from_user.id,
						 'Everybody got an invitation! Choose some options below', reply_markup=user_markup)

#__________________________________________________________________________________
#---------------------Message handlers: for 'New Comer' choise---------------------
#__________________________________________________________________________________

	if message.text == 'Rock on!':
		user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		bot.send_message(message.from_user.id, 'Hello {}! Welcome to Phillip Morris! It is your first day, happy to get you on board!'.format(User.nc['first_name']))
		reply_markup(message, 'I am your digital advisor CognitiveHRbot, I can guide you through the steps that will help you to make the process of your adaptation easier, '
							  'faster & more interesting. Use custom keyboard below to reply and lets get started!', 'Hello! I am ready to go!')
		bot.register_next_step_handler(message, newcomer_first_reply)
	if message.text == 'Hello! I am ready to go!':
		bot.register_next_step_handler(message, newcomer_first_reply)
	if message.text == 'Yes! What else I can ask my Buddy for help?':
		bot_message = '{} had a meeting with his Buddy!'.format(User.nc['first_name'])
		bot.send_message(User.hr['id'], bot_message)
		bot.send_message(User.s['id'], bot_message)
		reply_markup(message,'Well, he will provide you basic information about how to book conference '
		                     'rooms, how to use communication systems such as Outlook, phone book, instant messenger '
		                     '(MS Lync) etc.', 'Anything for my performance & development?')
	if message.text == 'No! But what else I can ask my Buddy for help?':
		bot_message = '{} didn\'t have a meeting with his Buddy!'.format(User.nc['first_name'])
		bot.send_message(User.hr['id'], bot_message)
		bot.send_message(User.s['id'], bot_message)
		reply_markup(message, 'Well, he will provide you basic information about how to book conference '
		                      'rooms, how to use communication systems such as Outlook, phone book, instant messenger '
		                      '(MS Lync) etc.', 'Anything for my performance & development?')
	if message.text == 'Anything for my performance & development?':
		bot_message = 'Yeah, so there a few steps for the first time:\n ' \
		              '- 1. Ask your Buddy or HR to take you to "Environment, Health and Safety" and  to "Information Services" trainings;\n' \
		              '- 2. Then your Supervisor will review your Job Description and discuss your main accountabilities;\n' \
		              '- 3. You also have to learn about the [PMU On-Boarding Tool](http://oneplace.pmiapps.biz/collab/HRTS1/PIT/Lists/Main%20Page/AllItems.aspx) and get Welcome Word from PMU Managing Director online;\n' \
		              '- 4. Learn the [Guide Book of Success (The PMI Code of Conduct)](http://guidebookforsuccess.pmiapps.biz/Pages/home.aspx?page=home) and [Principles & Practices](http://pmiprinciples.app.pmi/TEMPLATE/LAYOUTS/PMI/PPP/FrontEnd/index.aspx?c=Ukraine&language=English&tabNumber=1) relevant for your Department.'
		bot.send_message(message.from_user.id, bot_message, parse_mode='markdown', disable_web_page_preview=True)
		reply_markup(message, 'Tell me when it is done', 'Done. What else?')
		bot.register_next_step_handler(message, newcomer_third_reply)
	if message.text == 'Done. What else?':
		bot_message = 'Then provide New Comer with the [Job Description](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Job%20Description%20Template.doc) and discuss main accountabilities4\n' \
		              '- Familiarize New Comer with Company [Intranet](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d);\n' \
		              '- Present [PMU On-Boarding Tool](http://oneplace.pmiapps.biz/collab/HRTS1/PIT/Pages/default.aspx?) and Welcome Word from PMU Managing Director to New Comer;\n' \
		              '- Introduce the [Guide Book of Success](https://guidebookforsuccess.pmiapps.biz/Pages/home.aspx) (The PMI Code of Conduct) and [Principles & Practices](http://pmiprinciples.app.pmi/English/_layouts/PMI/PPP/FrontEnd/index.aspx?c=Ukraine&tabNumber=1) relevant for your Department.'
		bot.send_message(User.hr['id'], bot_message, parse_mode='markdown', disable_web_page_preview=True)
		bot.send_message(User.s['id'], bot_message, parse_mode='markdown', disable_web_page_preview=True)
		bot.register_next_step_handler(message, newcomer_third_reply)
	if message.text == 'Awesome! Thank you!':
		reply_markup(message, 'Have a great day! See you tomorrow.', '/restart')
	# ____________________________________________________________________________________
	# ---------------------Message handlers: for 'Supervisor' choise---------------------
	# ____________________________________________________________________________________

	if message.text == 'Let\'s go!':
		user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		bot_message = 'Hey {0}! You are Supervisor and you have only one opportunity to make' \
					  ' a first impression. Try to make the First Day positively memorable for' \
					  ' your New Comer. I will provide you a short guide to help you with it.'.format(User.s['first_name'])
		answer = 'Let\'s start the game!'
		reply_markup(message, bot_message, answer)
		# bot.send_message(message.from_user.id, 'Hey Mister! You are Supervisor and you have only one opportunity to make a first impression.')
		time.sleep(2)
		# user_markup.row('Then lets crush it')
		# bot.send_message(message.from_user.id, 'Try to make the First Day positively memorable for your New Comer. I will provide you a short guide to help you with it.',
		# 				 reply_markup=user_markup)

	if message.text == 'Let\'s start the game!':
		bot_message = 'Ok, first thing - check if {0} got all equipment,' \
					  ' he/she needs (computer, telephone, badge, etc.)'.format(User.nc['first_name'])
		bot.send_message(message.from_user.id, bot_message)
		time.sleep(2)

		bot.send_message(message.from_user.id, 'Welcome and greet New Comer. Introduce him/her to your Team, Department Head and other colleagues')
		time.sleep(2)
		bot_message = 'After welcome and greet New Comer.' \
					  ' Introduce him/her to your Team, Department Head and other colleagues,' \
					  ' Introduce {0} to {1}'.format(User.b['first_name'], User.nc['first_name'])
		bot.send_message(message.from_user.id, bot_message)
		time.sleep(2)
		bot_message = 'Done?'
		answer = 'Ok! Done!'
		# SHOULD BE PUSHED AS NOTIFICATION TO HR
		reply_markup(message, bot_message, answer)

	if message.text == 'Ok! Done!':
		bot_message = 'Now arrange a lunch with {0}.' \
					  ' During this ensure that Buddy explained' \
					  ' him/her basic information such as how to book conference rooms,' \
					  ' how to use communication systems including phone book and instant messaging' \
					  ' (MS Lync), he has shown him his office and'.format(User.nc['first_name'])
		answer = 'I\'m the best here :) Other?'
		reply_markup(message, bot_message, answer)
		# bot.send_message(message.from_user.id, 'Ensure that Buddy explained New Comer basic information such as how to book conference rooms, how to use communication systems including phone book and instant messaging (MS Lync) etc.', reply_markup=user_markup)

	if message.text == 'I\'m the best here :) Other?':
		bot_message = 'You also have to Send New Comer to Environment,' \
					  ' Health and Safety Training and Information Systems Training'
		bot.send_message(message.from_user.id, bot_message)
		time.sleep(4)
		bot_message = 'Then provide {0} with the [Job Description](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/Documents/Supporting%20Files/Job%20Description%20Template.doc) and discuss main accountabilities4\n' \
					  '- Familiarize New Comer with Company [Intranet](https://login.pmiapps.biz/F5Networks-SSO-Req?SSO_ORIG_URI=aHR0cHM6Ly9vbmVwbGFjZS5wbWlhcHBzLmJpei8%3d);\n' \
					  '- Present [PMU On-Boarding Tool](http://oneplace.pmiapps.biz/collab/HRTS1/PIT/Pages/default.aspx?) and Welcome Word from PMU Managing Director to New Comer;\n' \
					  '- Introduce the [Guide Book of Success](https://guidebookforsuccess.pmiapps.biz/Pages/home.aspx) (The PMI Code of Conduct) and [Principles & Practices](http://pmiprinciples.app.pmi/English/_layouts/PMI/PPP/FrontEnd/index.aspx?c=Ukraine&tabNumber=1)' \
					  ' relevant for your Department.'.format(User.nc['first_name'])
		bot.send_message(message.from_user.id, bot_message, parse_mode='markdown', disable_web_page_preview=True)
		time.sleep(4)
		bot_message = 'Tell me when it is done'
		answer = 'Done!'
		# NOTIFICATION SHOULD BE PUSHED TO HR
		reply_markup(message, bot_message, answer)

	if message.text == 'Done!':
		bot_message = 'Super! And finally collect the first feedback from ' \
					  'New Comer and agree the plan for the first week with him/her.'
		answer = 'Thanks for help! Awesome!'
		reply_markup(message, bot_message, answer)

	if message.text == 'Thanks for help! Awesome!':
		bot_message = 'Just make it happen in best way!'
		answer = '/restart'
		reply_markup(message, bot_message, answer)
		# user_markup.row('/restart')
		# bot.send_message(message.from_user.id,
		#                  'Just make it happen in best way!', reply_markup=user_markup)

#______________________________________________________________________________
#---------------------Message handlers: for 'Buddy' choise---------------------
#______________________________________________________________________________

	if message.text == 'Chop Chop!':
		bot_message = 'Hey {0}! Game time! :) ' \
					  'You have only one opportunity to make a first impression.' \
					  ' Try to make the First Day positively memorable for {1}.' \
					  ' Here is short checklist to help you.'.format(User.b['first_name'], User.nc['first_name'])
		answer = 'Yeah, guide me here, please!'
		# reply_markup(message, bot_message, answer)
		# user_markup.row('Hey dude! Yeah, guide me here, pls!')
		#
		# bot.send_message(message.from_user.id, 'Here is short checklist to help you.',
		#                  reply_markup=user_markup)
		reply_markup(message, bot_message, answer)
	if message.text == 'Yeah, guide me here, please!':
		bot_message = 'Meet and greet New Comer {0}. ' \
					  'New Comer’s Supervisor {1} should' \
					  ' arrange this meeting.'.format(User.nc['first_name'], User.s['first_name'])
		bot.send_message(message.from_user.id, bot_message)
		time.sleep(2)
		bot_message = 'It happened?'
		answer = ['Yes', 'No']
		# NOTIFICATION SHOULD BE PUSHED
		reply_markup(message, bot_message, answer)

	if message.text == 'Yes':
		bot_message = 'After show New Comer the Office and his/her' \
					  ' workplace and explain to him/her basic information' \
					  ' such as how to book conference rooms, how to use' \
					  ' communication systems including phone book and' \
					  ' instant messaging (MS Lync) etc.\n' \
					  'Also send New Comer to Environment, Health and' \
					  ' Safety Training and Information Systems Training.'
		answer = 'Ok. Done!'
		# NOTIFICATION SHOULD BE PUSHED TO HR
		reply_markup(message, bot_message, answer)
	if message.text == 'No':
		bot_message = 'After show New Comer the Office and his/her' \
					  ' workplace and explain to him/her basic information' \
					  ' such as how to book conference rooms, how to use' \
					  ' communication systems including phone book and' \
					  ' instant messaging (MS Lync) etc.\n' \
					  'Also send New Comer to Environment, Health and' \
					  ' Safety Training and Information Systems Training.'
		answer = 'Ok. Done!'
		# NOTIFICATION SHOULD BE PUSHED TO HR
		reply_markup(message, bot_message, answer)

	if message.text == 'Ok. Done!':
		bot_message = 'Now familiarize New Comer with [Company Intranet]' \
					  '(http://oneplace.pmiapps.biz/Pages/home.aspx) and' \
					  ' after present [PMU On-Boarding Tool]' \
					  '(http://oneplace.pmiapps.biz/collab/HRTS1/PIT/Pages/default.aspx?)' \
					  ' and Welcome Word from PMU Managing Director to New Comer.'
		answer = 'Easy! Done!:)'
		# NOTIFICATION SHOULD BE PUSHED TO HR
		user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		user_markup.row('Easy! Done!:)')
		bot.send_message(message.from_user.id, bot_message, reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)
		# user_markup.row('Sounds Easy! I\'m ready to go!')
		# bot.send_message(message.from_user.id, 'Present [PMU On-Boarding Tool](https://workpoint.pmiapps.biz/teams/HRTS1/PIT/default.aspx) and Welcome Word from PMU Managing Director to New Comer',
		#                  reply_markup=user_markup, parse_mode='markdown', disable_web_page_preview=True)

	if message.text == 'Easy! Done!:)':
		bot.send_message(message.from_user.id, 'Super! Thank you')
		time.sleep(2)
		user_markup.row('/restart')
		bot.send_message(message.from_user.id, 'See you tomorrow:)', reply_markup=user_markup)

def newcomer_first_reply(message):
	try:
		if message.text == 'Hello! I am ready to go!':
			user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
			user_markup.row('Yes', 'No')
			msg = bot.reply_to(message, 'First thing is simple administration part. Did you get all '
									'equipment you need (computer, telephone, badge, etc.)?', reply_markup=user_markup)
			bot.register_next_step_handler(msg, newcomer_second_reply)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def newcomer_second_reply(message):
	try:
		if message.text == 'Yes':
			bot.send_message(User.hr['id'], '{} got all equipment he/she needs'.format(User.nc["first_name"]))
			bot.send_message(User.s['id'], '{} got all equipment he/she needs'.format(User.nc["first_name"]))
			bot.send_message(message.from_user.id, 'Super! Now it is a time to meet with your supervisor. He will introduce you to the team and to your Buddy.')
			user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
			user_markup.row('Yes! What else I can ask my Buddy for help?')
			user_markup.row('No! But what else I can ask my Buddy for help?')
			bot.reply_to(message, 'Buddy - is a guy who will help you during integration period. He (or Supervisor)'
			                            ' will give a tour around the office. Have you already met your buddy?',
			                   reply_markup=user_markup)
			# bot.register_next_step_handler(msg, newcomer_third_reply)
		else:
			print('else')
			bot.send_message(User.hr['id'], '{} didn\'t get all equipment he/she needs'.format(User.nc["first_name"]))
			bot.send_message(User.s['id'], '{} didn\'t get all equipment he/she needs'.format(User.nc["first_name"]))
			bot.send_message(message.from_user.id, 'Okay, your Supervisor will request it for you. Meet with him. He will introduce you to the team and to the Buddy. '
												   'Also you can remind him about equipment.')
			user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
			user_markup.row('Yes! What else I can ask my Buddy for help?')
			user_markup.row('No! But what else I can ask my Buddy for help?')
			bot.reply_to(message, 'Buddy - is a guy who will help you during integration period. He (or Supervisor)'
			                      ' will give a tour around the office. Have you already met your buddy?',
			             reply_markup=user_markup)
	except Exception as e:
		print(e)
		bot.reply_to(message, 'oooops')

def newcomer_third_reply(message):
	try:
		if message.text == 'Done. What else?':
			user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
			user_markup.row('Yes', 'No')
			msg = bot.reply_to(message, 'Have you received your induction plan? ', reply_markup=user_markup)
			bot.register_next_step_handler(msg, newcomer_fourth_reply)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def newcomer_fourth_reply(message):
	try:
		print(message.text)
		if message.text == 'Yes':
			bot.send_message(User.hr['id'], '{} got the introduction plan'.format(User.nc["first_name"]))
			bot.send_message(User.s['id'], '{} got the introduction plan'.format(User.nc["first_name"]))
		else:
			bot.send_message(User.hr['id'], '{} didn\'t get the introduction plan'.format(User.nc["first_name"]))
			bot.send_message(User.s['id'], '{} didn\'t get the introduction plan'.format(User.nc["first_name"]))
		reply_markup(message, 'Share your first feedback Supervisor at the end of the day and review the plan for the first week',
		             'Awesome! Thank you!')
	except Exception as e:
		print(e)
		bot.reply_to(message, 'oooops')

bot.polling(none_stop=True)

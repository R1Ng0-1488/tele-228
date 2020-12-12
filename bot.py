import telebot
import config
import dbworker

from telebot import types

bot = telebot.TeleBot(config.token)

def lose(message):
	kb_hidden = types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, f"Поздравляю, {message.chat.username}, вы вафлер!!!", reply_markup=kb_hidden)
	dbworker.set_status(message.chat.id, config.Status.START.value)

@bot.message_handler(commands=['start'])
def cmd_start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	shut = types.KeyboardButton(text='Шут')
	vafler = types.KeyboardButton(text='Вафлер')
	keyboard.add(shut, vafler)
	bot.send_message(message.chat.id, 'Ты шут или вафлёр?', reply_markup=keyboard)
	dbworker.set_status(message.chat.id, config.Status.SOSAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_status(message.chat.id) == config.Status.SOSAL.value)
def cmd_sosal(message):
	if message.text == 'Вафлер':
		lose(message)
	else:
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		yes = types.KeyboardButton(text='Да')
		no = types.KeyboardButton(text='Нет')
		keyboard.add(yes, no)
		bot.send_message(message.chat.id, 'Ты сосал?', reply_markup=keyboard)
		dbworker.set_status(message.chat.id, config.Status.NASOSAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_status(message.chat.id) == config.Status.NASOSAL.value)
def cmd_nasosal(message):
	if message.text == 'Нет':
		lose(message)
	else:
		bot.send_message(message.chat.id, 'Насосался?')
		dbworker.set_status(message.chat.id, config.Status.END.value)

@bot.message_handler(func=lambda message: dbworker.get_current_status(message.chat.id) == config.Status.END.value)
def cmd_nasosal(message):
	lose(message)

if __name__ == '__main__':
	bot.infinity_polling()

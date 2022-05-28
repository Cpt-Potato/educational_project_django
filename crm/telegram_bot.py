from telebot import TeleBot

from educational_project_django.settings import TELEGRAM_BOT_TOKEN, CHAT_ID

bot = TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler()
def send_message(name, phone):
    text = f'Новая заявка:\n{name}, {phone}'
    bot.send_message(chat_id=CHAT_ID, text=text)

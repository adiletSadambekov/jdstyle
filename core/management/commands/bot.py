from django.conf import settings
from django.core.management import BaseCommand

import telebot

bot = telebot.TeleBot(token=settings.TG_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, str(message.chat.id))


class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Telegram Bot'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        print('Bot starting...')
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
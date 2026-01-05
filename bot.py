import os
import telebot
from telebot import types

# 1. Настройка ключей
# TOKEN нужно будет добавить в настройки хостинга (Secrets/Environment Variables)
TOKEN = os.environ.get("BOT_TOKEN")
# URL — это ссылка, которую тебе выдаст Streamlit после деплоя
WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://твой-апп.streamlit.app")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем кнопку Mini App
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo(WEB_APP_URL)
    
    # Главная кнопка запуска
    btn = types.KeyboardButton("🚀 ЗАПУСТИТЬ VALI", web_app=web_app)
    markup.add(btn)
    
    # Приветственное сообщение
    welcome_text = (
        "💎 **VALI | Smart Audit** на связи!\n\n"
        "Я помогу тебе проверить инвойс на честность: \n"
        "• Найду ошибки в расчетах\n"
        "• Сверю цены с рынком Китая\n\n"
        "Нажми кнопку ниже, чтобы начать аудит 👇"
    )
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        parse_mode="Markdown", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("VALI Bot запущен...")
    bot.infinity_polling()

import telebot
from database import init_db, add_user

# ... твои настройки TOKEN и WEB_APP_URL ...

bot = telebot.TeleBot(TOKEN)
init_db() # Инициализируем базу при запуске

@bot.message_handler(commands=['start'])
def start(message):
    # Сохраняем пользователя в базу
    add_user(message.from_user.id, message.from_user.username)
    
    # Дальше твой код с кнопкой запуска Mini App
    # Важно: передаем user_id в ссылке, чтобы Streamlit узнал юзера
    web_app_url_with_id = f"{WEB_APP_URL}?user_id={message.from_user.id}"
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton("🚀 ЗАПУСТИТЬ VALI", web_app=telebot.types.WebAppInfo(web_app_url_with_id))
    markup.add(btn)
    
    bot.send_message(message.chat.id, "💎 Добро пожаловать в VALI!", reply_markup=markup)

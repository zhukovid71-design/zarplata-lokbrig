import os
import threading
import telebot
from flask import Flask

# --- НАСТРОЙКИ ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')  # Токен будет передан из переменных окружения
PRODUCT_URL = "https://zhukovid71-design.github.io/zarplata-lokbrig/"

# --- ИНИЦИАЛИЗАЦИЯ ---
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# --- ОБРАБОТЧИКИ БОТА ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "🚂 Добро пожаловать!\n\n"
        "💰 Стоимость доступа: 350 Telegram Stars.\n"
        "👉 Нажмите /buy, чтобы начать покупку."
    )

@bot.message_handler(commands=['buy'])
def handle_buy(message):
    bot.send_message(
        message.chat.id,
        "✅ Для оплаты переведите 350 Telegram Stars на этот бот.\n"
        "После оплаты отправьте команду /get_access, чтобы получить ссылку."
    )

@bot.message_handler(commands=['get_access'])
def send_access(message):
    bot.send_message(
        message.chat.id,
        f"🎁 Ваша ссылка для доступа:\n{PRODUCT_URL}\n\n"
        f"Сохраните её, чтобы пользоваться калькулятором."
    )

# --- ЗАПУСК БОТА В ОТДЕЛЬНОМ ПОТОКЕ ---
def run_bot():
    bot.infinity_polling()

# --- FLASK-ПРИЛОЖЕНИЕ ДЛЯ RENDER ---
@app.route('/')
def index():
    return "Bot is running!"

if __name__ == '__main__':
    thread = threading.Thread(target=run_bot)
    thread.start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
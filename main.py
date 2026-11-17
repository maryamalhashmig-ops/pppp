import os
from threading import Thread
import telebot
from flask import Flask

# 1. إعداد سيرفر الويب البسيط لإرضاء Render وفتح البورت
app = Flask(__name__)


@app.route("/")
def home():
  return "Bot is running 24/7 successfully!"


def run_flask():
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)


# تشغيل السيرفر في الخلفية بالتوازي مع البوت
t = Thread(target=run_flask)
t.start()


# 2. جلب توكن البوت بأمان من متغيرات البيئة في Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)


# 3. أكواد البوت والأوامر الخاصة بك
@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "أهلاً بك يا المرعب اليماني! البوت يعمل 24/7 بنجاح.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "تم استلام رسالتك بنجاح.")


# تشغيل البوت باستمرار
print("Bot and Flask server started successfully!")
bot.infinity_polling()

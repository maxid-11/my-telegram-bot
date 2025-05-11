from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters
import os
from supabase import create_client

# Твои данные (замени на свои)
TELEGRAM_TOKEN = "8086133202:AAHRb1-ZFCJFXWALymMV4FnAIy1hCMXe0SI"
SUPABASE_URL = "https://eixgmdftnxccxvnbguxx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpeGdtZGZ0bnhjY3h2bmJndXh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY5ODk3MDksImV4cCI6MjA2MjU2NTcwOX0.TR260Cmy8tr0y2IVzoiXvmMhYMR_nNEQ2Ka1fgAfYS8"
HF_TOKEN = "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"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Функция для ответа
def reply(update: Update, context):
    user_id = update.message.chat.id
    user_msg = update.message.text

    # Сохраняем сообщение в базу
    supabase.table("chats").upsert({"user_id": user_id, "messages": [user_msg]}).execute()

    # Отвечаем (пока заглушка)
    update.message.reply_text("Привет! Я пока учусь, скоро смогу отвечать!")

# Запуск бота
updater = Updater(TELEGRAM_TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()
updater.idle()
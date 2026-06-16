from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

print("BOT TOKEN:", TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FlashBot çalışıyor 🚀")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT STARTING...")

app.run_polling()

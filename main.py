import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN bulunamadı!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FlashBot çalışıyor 🚀")

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("BOT STARTING...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("BOT RUNNING 🚀")

    # Botun kapanmaması için
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

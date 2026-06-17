import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN bulunamadı!")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 FlashBot aktif!\n\n"
        "Komutları görmek için /yardim yaz."
    )

# /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 FlashBot aktif.\n"
        "Sunucu durumu: Çalışıyor 🚀"
    )

# /yardim
async def yardim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 FlashBot Komutları\n\n"
        "/start - Botu başlat\n"
        "/ping - Sistem durumu\n"
        "/yardim - Yardım menüsü\n"
        "/firsat - Günün fırsatını göster"
    )

# /firsat
async def firsat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Günün Fırsatı\n\n"
        "Samsung Galaxy Tab S10 FE\n"
        "Fiyat: 12.999 TL\n"
        "Normal: 15.999 TL\n\n"
        "💰 Tasarruf: 3.000 TL\n"
        "Kaynak: FlashBot Demo"
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("yardim", yardim))
    app.add_handler(CommandHandler("firsat", firsat))

    print("BOT STARTING...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("BOT RUNNING 🚀")

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

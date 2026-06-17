import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN bulunamadı!")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 FlashBot çalışıyor!\n\n"
        "Gerçek fırsatların peşindeyiz."
    )


# /yardim
async def yardim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 FlashBot Komutları:\n\n"
        "/start - Botu başlatır\n"
        "/ping - Sistem durumunu gösterir\n"
        "/hakkinda - FlashBot hakkında bilgi verir\n"
        "/firsat - Örnek fırsatı gösterir"
    )


# /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Sistem aktif!")


# /hakkinda
async def hakkinda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ FlashBot v1\n\n"
        "Gerçek indirimleri tespit etmeyi amaçlayan "
        "bir fırsat otomasyonu projesidir.\n\n"
        "Geliştirilmeye devam ediyor..."
    )


# /firsat
async def firsat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Günün Örnek Fırsatı\n\n"
        "📱 Samsung Galaxy Tab S9 FE\n"
        "💸 İndirim: %32\n"
        "🏪 Satıcı: Hepsiburada\n"
        "⭐ Güven Skoru: 9.2/10"
    )


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("yardim", yardim))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("hakkinda", hakkinda))
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

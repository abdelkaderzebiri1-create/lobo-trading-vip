
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐺 LOBO TRADING VIP\n"
        "البوت يعمل بنجاح!\n\n"
        "الأوامر:\n"
        "/status - حالة البوت\n"
        "/help - المساعدة"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 LOBO TRADING VIP يعمل الآن.\n"
        "📊 M1 و M5\n"
        "🌙 OTC\n"
        "تنبيه: لم يتم ربط مصدر أسعار موثوق بعد، "
        "لذلك لا توجد إشارات حقيقية حالياً."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐺 LOBO TRADING VIP\n"
        "استعمل /status لمعرفة حالة البوت."
    )

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()

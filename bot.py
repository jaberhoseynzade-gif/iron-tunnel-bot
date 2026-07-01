from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 8781596808:AAGUqSZ5oV9EA3Hs1-P2mI7GL5N32_6rWgs

keyboard = [
    ["🛒 خرید اشتراک"],
    ["💬 پشتیبانی"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 به IRON TUNNEL خوش آمدید\n\nیکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 خرید اشتراک":
        await update.message.reply_text(
            "💳 پلن‌ها:\n\n"
            "20GB ➜ 129,000\n"
            "30GB ➜ 199,000\n"
            "50GB ➜ 299,000\n"
            "100GB ➜ 399,000\n"
            "250GB ➜ 699,000\n\n"
            "💳 شماره کارت:\nXXXX-XXXX-XXXX-XXXX\n\n"
            "📷 بعد از پرداخت، رسید را ارسال کنید."
        )

    elif text == "💬 پشتیبانی":
        await update.message.reply_text("پشتیبانی: @bibi1242")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()

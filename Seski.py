from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# تابع شروع
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('سلام! به ربات من خوش اومدی.')

# تابع پاسخ به پیام‌ها
async def echo(update: Update, context: CallbackContext):
    user_message = update.message.text
    await update.message.reply_text(f'شما گفتید: {user_message}')

def main():
    # توکن ربات رو اینجا وارد کنید
    application = Application.builder().token("7569285769:AAEvKY0KhSqDVS-myc-dOs8jPj6RK2w_ghE").build()

    # دستور /start
    application.add_handler(CommandHandler("start", start))

    # پاسخ به پیام‌های کاربر
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # شروع ربات
    application.run_polling()

if __name__ == '__main__':
    main()
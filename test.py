from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تابع شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! به ربات من خوش اومدی.')

# تابع پاسخ به پیام‌ها
def echo(update: Update, context: CallbackContext):
    user_message = update.message.text
    update.message.reply_text(f'شما گفتید: {user_message}')

def main():
    # توکن ربات رو اینجا وارد کنید
    updater = Updater("7569285769:AAEvKY0KhSqDVS-myc-dOs8jPj6RK2w_ghE", use_context=True)

    dispatcher = updater.dispatcher

    # دستور /start
    dispatcher.add_handler(CommandHandler("start", start))

    # پاسخ به پیام‌های کاربر
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
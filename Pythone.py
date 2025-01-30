from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("سلام! من ربات تلگرامی تو هستم. چطور می‌تونم کمکت کنم؟")

def main():
    updater = Updater("7569285769:AAEvKY0KhSqDVS-myc-dOs8jPj6RK2w_ghE", use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

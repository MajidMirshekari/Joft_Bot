# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# # تابع شروع
# async def start(update: Update, context: CallbackContext):
#     await update.message.reply_text('سلام! به ربات من خوش اومدی.')

# # تابع پاسخ به پیام‌ها
# async def echo(update: Update, context: CallbackContext):
#     user_message = update.message.text
#     await update.message.reply_text(f'شما گفتید: {user_message}')

# def main():
#     # توکن ربات رو اینجا وارد کنید
#     application = Application.builder().token("7569285769:AAEvKY0KhSqDVS-myc-dOs8jPj6RK2w_ghE").build()

#     # دستور /start
#     application.add_handler(CommandHandler("start", start))

#     # پاسخ به پیام‌های کاربر
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

#     # شروع ربات
#     application.run_polling()

# if __name__ == '__main__':
#     main()

############################# New Bot #####################

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# تابع شروع
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("خرید اشتراک", callback_data='buy_subscription')],
        [InlineKeyboardButton("تماشای فیلم", callback_data='watch_movie')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به ربات ما خوش اومدی! لطفا یک گزینه انتخاب کن:", reply_markup=reply_markup)

# تابع مدیریت Callback Query
async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'buy_subscription':
        await query.edit_message_text("اشتراک شما با موفقیت خریداری شد!")
    elif query.data == 'watch_movie':
        # نمایش دسته‌بندی فیلم‌ها
        keyboard = [
            [InlineKeyboardButton("فیلم‌های اکشن", callback_data='action_movies')],
            [InlineKeyboardButton("فیلم‌های کمدی", callback_data='comedy_movies')],
            [InlineKeyboardButton("بازگشت به منوی اصلی", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("لطفا یک دسته‌بندی انتخاب کنید:", reply_markup=reply_markup)
    elif query.data == 'action_movies':
        await query.edit_message_text("فیلم‌های اکشن:\n1. فیلم ۱\n2. فیلم ۲\n3. فیلم ۳")
    elif query.data == 'comedy_movies':
        await query.edit_message_text("فیلم‌های کمدی:\n1. فیلم ۱\n2. فیلم ۲\n3. فیلم ۳")
    elif query.data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("خرید اشتراک", callback_data='buy_subscription')],
            [InlineKeyboardButton("تماشای فیلم", callback_data='watch_movie')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("به منوی اصلی خوش اومدی! لطفا یک گزینه انتخاب کن:", reply_markup=reply_markup)

def main():
    # توکن ربات تلگرام
    application = Application.builder().token("Y7862915660:AAEloHMe6r1uqpuLZjslaTqcbrXmElaNnyo").build()

    # دستور /start
    application.add_handler(CommandHandler("start", start))

    # مدیریت Callback Query
    application.add_handler(CallbackQueryHandler(button_click))

    # شروع ربات
    application.run_polling()

if __name__ == '__main__':
    main()
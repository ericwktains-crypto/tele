import telebot

TOKEN = "7770233617:AAHLhnqCalNrUaBtqO6QbPaL90t-tZpZuzE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    # تصميم لوحة التحكم والإحصائيات تماماً مثل الصورة
    control_panel_text = f"""• لوحة التحكم 🤖

———— إحصائيات اليوم ————
👥 الإجمالي: 50
🆕 مستخدمون جدد: 2 📈
💬 الرسائل: 3 📈
🔄 الجلسات: 2
⚡ متوسط الاستجابة: 19ms
🚫 المحظورين: 0 | قاموا بحظر البوت: 1

🕒 آخر نشاط: 🚫 إشعار الحظر – 50s

استمتع ببوت خاص بدون إعلانات مزعجة! اشترك الآن في بوت خدماتنا المدفوعة على تيليكرام واحصل على بوت خاص بك بأسعار تبدأ من $2 شهرياً. استمتع بالجودة والاحترافية والدعم الفني.
@EchoLLCbot

- عليك تفعيل الانلاين لكي يعمل البوت بشكل صحيح [اضغط هنا لمعرفة كيف تفعيل الانلاين](https://t.me)"""

    # الأزرار السفلية (اللوحة) مطابقة للصورة تماماً
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📝 المحتوى", "⚙️ الإعدادات")
    markup.row("🔐 الاشتراك", "👥 المستخدمون")
    markup.row("💰 المالية", "📢 التواصل")
    markup.row("🛠 النظام والدعم")
    markup.row("🚫 إشعار الحظر", "🔔 إشعار الدخول")
    markup.row("❓ دليل الاستخدام")

    bot.send_message(
        message.chat.id, 
        control_panel_text, 
        reply_markup=markup, 
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text
    if text == "📝 المحتوى":
        bot.reply_to(message, "قسم إدارة المحتوى الخاص بالبوت.")
    elif text == "⚙️ الإعدادات":
        bot.reply_to(message, "إعدادات البوت العامة.")
    elif text == "👥 المستخدمون":
        bot.reply_to(message, "عدد المستخدمين الكلي: 50 مستخدم.")
    elif text == "💰 المالية":
        bot.reply_to(message, "قسم المالية والاشتراكات.")
    elif text == "🛠 النظام والدعم":
        bot.reply_to(message, "للتواصل مع المطور الأساسي: @c99_c")
    elif text == "🚫 إشعار الحظر":
        bot.reply_to(message, "إشعار الحظر مفعّل ✅")
    elif text == "🔔 إشعار الدخول":
        bot.reply_to(message, "إشعار الدخول مفعّل ✅")
    elif text == "❓ دليل الاستخدام":
        bot.reply_to(message, "مرحباً بك في دليل الاستخدام الخاص بالبوت.")
    else:
        bot.reply_to(message, "تم استلام رسالتك بنجاح.")

print("Bot is running...")
bot.infinity_polling()

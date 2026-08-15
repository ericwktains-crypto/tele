import telebot

# ضع توكن بوتك هنا بين علامتي التنصيص
TOKEN = "هنا_ضع_توكن_البوت_الخاص_بك"
bot = telebot.TeleBot(TOKEN)

# معرف المطور الخاص بك
DEV_USERNAME = "@c99_c"
DEV_ID = 0  # سيتم حفظه أو التحقق منه عبر المعرف في الرسائل

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = f"اهلا عزيزي ({user_name}) في بوت الجني الأزرق ❤️\n\nعليك التفكير بشخصية حقيقية او خيالية.\nانا ساحاول معرفة الشخصية التي فكرت بها."
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 العب .")
    
    # إذا كان المستخدم هو المطور، نثبت له أنه المطور
    if message.from_user.username == "c99_c":
        welcome_text += "\n\n🛠 أهلاً بك مطور البوت الأساسي (@c99_c)."

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(commands=['dev', 'admin'])
def dev_panel(message):
    # التحقق مما إذا كان المرسل هو المطور
    if message.from_user.username == "c99_c":
        bot.reply_to(message, "مرحباً بك يا مطوري العزيز 🖤\nالبوت يعمل بشكل سليم وبدون اشتراك إجباري.")
    else:
        bot.reply_to(message, "عذراً، هذا الأمر مخصص للمطور فقط 🚫")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "🎮 العب .":
        bot.reply_to(message, "حسناً، فكرت بالشخصية؟ اخبرني ببعض الصفات أو اطرح الأسئلة لنبدأ اللعبة!")
    else:
        bot.reply_to(message, "أنا أتنافس معك، فكر بشخصية وسأحاول تخمينها!")

print("Bot is running...")
bot.infinity_polling()

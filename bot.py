import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import threading

# =========================
# KONFIGURASI
# =========================

TOKEN = "8463563474:AAFkmlf3bj8znddlo9asuS4Y89XxKgERUNY"
GROUP_ID = -1003615340364 
IMAGE_URL = "https://i.postimg.cc/T1K1T2S0/photo-6070866295453846882-y.jpg" 
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

spam_running = False


# =========================
# WELCOME MESSAGE
# =========================

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🎁 CLAIM BONUS", url="https://mpo11baru.com/register/149B011E")
    btn2 = InlineKeyboardButton("🎰 DAFTAR SEKARANG", url="https://mpo11baru.com/register")
    markup.add(btn1)
    markup.add(btn2)

    caption = """
🎉🔥 WELCOME KE MPO11 VIP ROOM! 🔥🎉
Halo  👋
Selamat bergabung di tempat para pencari kemenangan 💎💰
Kamu sekarang sudah berada di platform dengan peluang terbaik & bonus melimpah 🎯
🎁 BONUS NEW MEMBER hingga 100%
🎰 Game update & siap dimainkan
⚡ Akses cepat & mudah
💸 Peluang cuan setiap hari
Jangan cuma jadi penonton…
Saatnya kamu yang rasakan sensasinya 😎🔥
👇 DAFTAR & MULAI DI SINI 👇
https://mpo11gacor.youware.app
REAL 100% ✅
"""

    bot.send_photo(message.chat.id, IMAGE_URL, caption=caption, reply_markup=markup)


# =========================
# SPAM BONUS FUNCTION
# =========================

def spam_bonus():
    global spam_running

    while spam_running:
        try:
            markup = InlineKeyboardMarkup()
            btn = InlineKeyboardButton("🎁 AMBIL BONUS SEKARANG", url="https://mpo11baru.com/register/149B011E")
            markup.add(btn)

            caption = """
🚨 INFO PENTING BUAT KAMU YANG MAU CUAN BESAR! 🚨

Masih nonton orang lain WD tiap hari? 😏
Sekarang waktunya kamu yang rasain sensasinya! 💸🔥

🎯 MPO11 lagi bagi-bagi BONUS BESAR untuk New Member!

🎁 BONUS NEW MEMBER hingga 100%
🎰 Game Gacor update setiap hari
⚡ Proses daftar super cepat
💰 Deposit & WD aman tanpa ribet
📈 Banyak member sudah buktiin hasilnya

Jangan tunggu sampai rame dan slotnya berubah pola!
Kesempatan emas itu datangnya cuma sekali 😎

Kalau mau serius cari tambahan cuan,
ini saat yang tepat buat mulai 🚀

💎 Gak perlu modal besar
💎 Gak perlu ribet
💎 Tinggal daftar & langsung main

👉 DAFTAR & JOIN SEKARANG DI SINI:
Pesan ini REAL 100% ✅
Bukan janji kosong, bukan PHP ❌

Yang cepat dia dapat!
Yang ragu cuma jadi penonton 😌🔥

Gas sekarang sebelum nyesel! 💥💰
Klik tombol di bawah sebelum terlambat!
"""

            bot.send_photo(GROUP_ID, IMAGE_URL, caption=caption, reply_markup=markup)

            time.sleep(3600)  # spam setiap  1 jam

        except Exception as e:
            print("Error spam:", e)
            break


# =========================
# COMMAND START SPAM
# =========================

@bot.message_handler(commands=['startspam'])
def start_spam(message):
    global spam_running

    if not spam_running:
        spam_running = True
        threading.Thread(target=spam_bonus).start()
        bot.reply_to(message, "🔥 Spam bonus dimulai!")

    else:
        bot.reply_to(message, "⚠️ Spam sudah berjalan!")


# =========================
# COMMAND STOP SPAM
# =========================

@bot.message_handler(commands=['stopspam'])
def stop_spam(message):
    global spam_running

    spam_running = False
    bot.reply_to(message, "🛑 Spam dihentikan.")


# =========================
# AUTO RESPON KATA BONUS
# =========================

@bot.message_handler(func=lambda message: True)
def auto_bonus(message):
    if "bonus" in message.text.lower():
        bot.reply_to(message, "🎁 Mau bonus? Ketik /startspam ya 🔥")


# =========================
# JALANKAN BOT
# =========================

print("Bot MPO11 sedang berjalan...")
bot.infinity_polling()
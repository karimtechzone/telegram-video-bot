from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

import os

BOT_TOKEN = os.environ.get("8307012125:AAGKffeIRGn3AjzDFFHyPMJMMaLN2pNjPSU")

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📢 Telegram Channel", url="https://t.me/social_workars4")],
        [InlineKeyboardButton("📺 YouTube Channel", url="https://youtube.com/@karim_tech_zone")],
        [InlineKeyboardButton("🤖 Official Bot", url="https://t.me/facebokidsellbd_bot")],
        [InlineKeyboardButton("👤 Agent Bot", url="https://t.me/social_workars1_bot")],
        [InlineKeyboardButton("📦 Backup Channel", url="https://t.me/+vmH9kgowHUI3NzI1")],
        [InlineKeyboardButton("🆘 Report Channel", url="https://t.me/+p3hGmxzd5gY1YzI1")],
        [InlineKeyboardButton("👑 Admin Contact", url="https://t.me/MD_Rezual_Karim")]
    ]

    await update.message.reply_text(
        "✅ Welcome to Social Workars Bot\n\n👇 নিচের বাটনগুলো ব্যবহার করুন",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

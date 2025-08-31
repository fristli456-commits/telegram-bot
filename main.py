from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Твой токен
TOKEN = "7582081911:AAEfA2SM1zfBZGCkzlQmL-7N-xI4MpDIMZU"

# ID админа
ADMIN_ID = 7458977241

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот 🤖")

# Ответ на любое сообщение
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")

    # Лог для админа
    if ADMIN_ID:
        await context.bot.send_message(ADMIN_ID, f"✉️ {user.username} ({user.id}) написал: {text}")

# Панель админа
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:
        await update.message.reply_text("⚙ Панель админа:\n1. Посмотреть логи\n2. Отправить сообщение")
    else:
        await update.message.reply_text("⛔ У тебя нет доступа!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Бот запущен!")
    app.run_polling(poll_interval=0.1)

if __name__ == "__main__":
    main()

import telebot

API_TOKEN = 'YOUR_API_TOKEN'
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! Use /help to see available commands.")

# Set webhook
@bot.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])

if __name__ == '__main__':
    bot.remove_webhook()  # Remove existing webhook
    bot.set_webhook(url=WEBHOOK_URL)  # Set new webhook
    bot.polling()  # Start polling for messages
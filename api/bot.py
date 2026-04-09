import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

@app.route('/api/bot', methods=['POST'])
def webhook():
    update = request.get_json()
    
    if 'message' in update:
        message = update['message']
        if 'text' in message:
            chat_id = message['chat']['id']
            text = message['text']
            
            if text == '/start':
                response_text = 'Привет! Это твой автоматический ответ на /start команду 👋'
                send_message(chat_id, response_text)
    
    return 'OK', 200

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run()
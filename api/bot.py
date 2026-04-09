import json
import urllib.request
import urllib.parse
import os

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = json.dumps({'chat_id': chat_id, 'text': text}).encode()
    req = urllib.request.Request(url, data=data,
          headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

def handler(request, context):
    # Vercel передаёт request как dict с телом
    body = request.get('body') or {}
    
    if isinstance(body, str):
        body = json.loads(body)
    
    if 'message' in body:
        msg = body['message']
        if 'text' in msg:
            chat_id = msg['chat']['id']
            text = msg['text']
            if text == '/start':
                send_message(chat_id, 'Привет! Это автоматический ответ на /start 👋')
    
    return {
        'statusCode': 200,
        'body': 'OK'
    }
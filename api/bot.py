import json
import urllib.request
import os
import sys

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

print(f"🔧 Бот загружен, TOKEN получен: {'ДА' if TOKEN else 'НЕТ'}", file=sys.stderr)

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = json.dumps({'chat_id': chat_id, 'text': text}).encode()
    req = urllib.request.Request(url, data=data,
          headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req)
    except Exception as e:
        print(f"❌ Ошибка: {e}", file=sys.stderr)

# ВАЖНО: Vercel ищет переменную 'handler' на верхнем уровне
def handler(request, context):
    print("🚀 Получен запрос", file=sys.stderr)
    
    # Получаем тело
    if isinstance(request, dict):
        body = request.get('body', {})
    else:
        body = {}
    
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except:
            pass
    
    # Обработка сообщения
    if 'message' in body:
        msg = body['message']
        if 'text' in msg and msg['text'] == '/start':
            chat_id = msg['chat']['id']
            send_message(chat_id, 'Привет! Это автоматический ответ на /start 👋')
    
    return {
        'statusCode': 200,
        'body': 'OK'
    }
import json
import urllib.request
import urllib.parse
import os
import sys

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

print(f"🔧 Бот загружен, TOKEN получен: {'ДА' if TOKEN else 'НЕТ'}", file=sys.stderr)
print(f"🔧 TOKEN начинается с: {TOKEN[:10] if TOKEN else 'None'}...", file=sys.stderr)

def send_message(chat_id, text):
    print(f"📤 Отправка сообщения в чат {chat_id}: {text[:50]}", file=sys.stderr)
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = json.dumps({'chat_id': chat_id, 'text': text}).encode()
    req = urllib.request.Request(url, data=data,
          headers={'Content-Type': 'application/json'})
    try:
        response = urllib.request.urlopen(req)
        print(f"✅ Сообщение отправлено, статус: {response.status}", file=sys.stderr)
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}", file=sys.stderr)

def handler(request, context):
    print("🚀 Вход в handler", file=sys.stderr)
    print(f"📨 Тип request: {type(request)}", file=sys.stderr)
    print(f"📨 request: {request}", file=sys.stderr)
    
    # Получаем тело запроса
    body = request.get('body') if isinstance(request, dict) else {}
    print(f"📦 Тело запроса (сырое): {body}", file=sys.stderr)
    
    if isinstance(body, str):
        try:
            body = json.loads(body)
            print(f"📦 Распарсено JSON: {body}", file=sys.stderr)
        except Exception as e:
            print(f"❌ Ошибка парсинга JSON: {e}", file=sys.stderr)
            return {'statusCode': 400, 'body': 'Invalid JSON'}
    
    print(f"📨 Содержит 'message'? {'Да' if 'message' in body else 'Нет'}", file=sys.stderr)
    
    if 'message' in body:
        msg = body['message']
        print(f"💬 message: {msg}", file=sys.stderr)
        
        if 'text' in msg:
            chat_id = msg['chat']['id']
            text = msg['text']
            print(f"💬 Чат {chat_id}, текст: '{text}'", file=sys.stderr)
            
            if text == '/start':
                print(f"🎯 Обнаружен /start! Отправляем приветствие", file=sys.stderr)
                send_message(chat_id, 'Привет! Это автоматический ответ на /start 👋')
            else:
                print(f"⚠️ Не /start, игнорируем", file=sys.stderr)
        else:
            print(f"⚠️ Нет текста в сообщении", file=sys.stderr)
    else:
        print(f"⚠️ Нет ключа 'message' в body", file=sys.stderr)
    
    print(f"✅ Возвращаем ответ 200", file=sys.stderr)
    return {
        'statusCode': 200,
        'body': 'OK'
    }
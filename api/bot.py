from http.server import BaseHTTPRequestHandler
import json, os, urllib.request, urllib.parse

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = json.dumps({'chat_id': chat_id, 'text': text}).encode()
    req = urllib.request.Request(url, data=data,
          headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length))

        if 'message' in body:
            msg = body['message']
            if 'text' in msg:
                chat_id = msg['chat']['id']
                text = msg['text']
                if text == '/start':
                    send_message(chat_id, 'Привет! Это автоматический ответ на /start 👋')

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def log_message(self, *args):
        pass
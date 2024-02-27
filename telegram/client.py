import os
import requests

from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TELEGRAM_BOT_TOKEN')

def send_message(chat_id, text):
    telegram_url = f'https://api.telegram.org/bot{token}/sendMessage'
    print(telegram_url)

    data = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.post(telegram_url, data=data)
    print(response.json())


if __name__ == '__main__':
    chat_id = 912697577
    text = "How Are you?"
    send_message(chat_id, text)

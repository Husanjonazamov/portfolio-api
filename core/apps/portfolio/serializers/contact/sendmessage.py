import requests
from config.env import env


def send_telegram_message(message):
    # token = env('BOT_TOKEN').split(",") 
    # chat_id = env('ADMIN').split(",")
    BOT_TOKEN = '7178118588:AAHr3QkdJxksP_xtCKgrMPNFLeOpkHJqNWc'
    ADMIN = '6415392394'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': ADMIN,
        'text': message,
    }
    response = requests.post(url, data=payload)
    return response.json()

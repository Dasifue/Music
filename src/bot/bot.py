from .bot_settings import TELEGRAM_TOKEN, TELEGRAM_CHATID
import requests

URL=f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHATID}&text='

def send_message(author, text, rating, object):
    message = f"""
    created new comment to {object}
    from: {author}
    rating: {rating}
    text: {text}
    """
    requests.get(URL+message)


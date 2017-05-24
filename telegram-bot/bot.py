import urllib


BOT_TOKEN = 'YOUR_TOKE_HERE'
SEND_MESSAGE_URL = 'https://api.telegram.org/bot{}/sendMessage'


def send_message(message, chat_id):
    url = SEND_MESSAGE_URL.format(BOT_TOKEN)
    data = urllib.urlencode({'chat_id': chat_id, 'text': message})
    urllib.urlopen(url, data)


def lambda_handler(event, context):
    chat_id = event['message']['chat']['id']
    text = event['message']['text']
    user = event['message']['from']['first_name']

    message = '{} said: "{}"'.format(user, text)
    send_message(message, chat_id)

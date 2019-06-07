import logging
from telegram.ext import Updater,  MessageHandler, Filters
from urllib3 import make_headers
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
request_kwargs = {
    'proxy_url': 'http://80.152.210.221:3128',
    'urllib3_proxy_kwargs': {
        'proxy_headers': make_headers(proxy_basic_auth='username:password')
    }
}
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='714985193:AAGRTr1nYeOB2Hf1v0SkVs8xR3yrwyQ_tEg', use_context=True, request_kwargs=request_kwargs)


def handle_message(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    if text[0:8] == "Зашифруй":
        print(text.split("("))
        count = text.split("(")[1]
        count = count[0:-1]
        text_to_cipher = text.split("(")[2]
        text_to_cipher = text_to_cipher[0:-1]
        result = cipher(text_to_cipher, count)
        context.bot.send_message(chat_id, result)
    elif text[0:9] == "Расшифруй":
        print(text.split("("))
        count = text.split("(")[1]
        count = count[0:-1]
        text_to_un_cipher = text.split("(")[2]
        text_to_un_cipher = text_to_un_cipher[0:-1]
        result = un_cipher(text_to_un_cipher, count)
        context.bot.send_message(chat_id, result)


handler = MessageHandler(Filters.text | Filters.command, handle_message)
updater.dispatcher.add_handler(handler)
updater.start_polling()


def cipher(text, counter):
    text.lower()

    res = []
    for i in text:
        if i == " ":
            res.append(" ")
        else:
            res.append(alphabet[(alphabet.index(i) + int(counter)) % 33])
    return "".join(res)


def un_cipher(text, counter):
    text.lower()
    res = []
    for i in text:
        if i == " ":
            res.append(" ")
        else:
            res.append(alphabet[(alphabet.find(i) - int(counter)) % 33])
    return "".join(res)
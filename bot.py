import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
session = requests.Session()
vk_session = vk_api.VkApi(token='370afd337d846f58deb813810ae22a2b9f756c28155593c48496e4d691d176176a8d03f28b0ae5161f047')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'r' or event.text == 'Второй вариант фразы':
            if event.from_user:

                vk.messages.send(
                    random_id=123456,
                    user_id=event.user_id,
                    message='Ваш текст')
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Ваш текст')
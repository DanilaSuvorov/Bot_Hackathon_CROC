import vk_api
import requests
import matplotlib.pyplot as plt

from vk_api.longpoll import VkLongPoll, VkEventType
session = requests.Session()
vk_session = vk_api.VkApi(token='370afd337d846f58deb813810ae22a2b9f756c28155593c48496e4d691d176176a8d03f28b0ae5161f047')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == '/start':
            if event.from_user:
                vk.messages.send(
                    random_id=187823456,
                    user_id=event.user_id,
                    message='Сколько раз в день мне спрашивать ваше настроение?')
        if event.text != '/start':
            if event.from_user:
                count = event.text
                print(count)
                vk.messages.send(
                    random_id=187823456,
                    user_id=event.user_id,
                    message='Когда вы просыпаетесь?')
        if event.text.:
            if event.from_user:
                count = event.text
                print(count)
                vk.messages.send(
                    random_id=187823456,
                    user_id=event.user_id,
                    message='Когда вы просыпаетесь?')
time = []

def time():
    if count == 1:
        time.append((y - x) / 2 + x)
    elif count == 2:
        time.append(x + 2)
        time.append(y - 1)
    elif count == 3:
        time.append((y - x) / 2 + x)
        time.append(x + 2)
        time.append(y - 1)
    elif count >= 4:
        many = (y - x) / count
        for i in range(x, y):
            time.append(x + many)




def graphic():
    fig, ax = plt.subplots(1, 1)
    ax.plot(time[], vkapi['likes'])
    fig.set_size_inches(22, 10)
    plt.title('Статистика по максимальному значению лайков за год', fontsize=18)
    plt.savefig('likes.png')

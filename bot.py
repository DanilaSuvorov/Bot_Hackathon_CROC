import random
import time

import bs4 as bs4
import vk_api
import matplotlib.pyplot as plt
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
session = requests.Session()
vk_session = vk_api.VkApi(token='370afd337d846f58deb813810ae22a2b9f756c28155593c48496e4d691d176176a8d03f28b0ae5161f047')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def _clean_all_tag_from_str(string_line):
    """
    Очистка строки stringLine от тэгов и их содержимых
    :param string_line: Очищаемая строка
    :return: очищенная строка
    """
    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result


def _get_time():
    request = requests.get("https://my-calend.ru/date-and-time-today")
    b = bs4.BeautifulSoup(request.text, "html.parser")
    return _clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]
counter = 0
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if counter == 0 and event.text == "Шалом":
            if event.from_user:
                vk.messages.send(random_id=random.randint(a=10000, b=100000), user_id=event.user_id, message="Сколько раз тебя спрашивать?")
                counter += 1
        elif event.from_user and counter == 1:
            count = event.text
            print(count)
            vk.messages.send(random_id=random.randint(a=10000, b=100000), user_id=event.user_id,message="Во сколько ты просыпаешься")
            counter += 1
        elif event.from_user and counter == 2:
            x = event.text
            print(x)
            vk.messages.send(random_id=random.randint(a=10000, b=100000), user_id=event.user_id,message="Во сколько ты ложишься")
            counter += 1
        elif event.from_user and counter == 3:
            y = event.text
            print(y)
            counter += 4
        else:
            vk.messages.send(random_id=random.randint(a=10000, b=100000), user_id=event.user_id,
                             message="Я украинский не понимаю")






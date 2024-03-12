import random
import string
import requests

from data import API, ingredients


def random_string():
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters)[:10] for i in range(10))
    return random_str


def valid_creds():
    creds = {
        'email': f'{random_string()}@yandex.ru',
        'password': random_string(),
        'name': random_string()
    }
    return creds


def create_order(headers):
    order = requests.post(API.ORDERS, headers=headers, data=ingredients)
    return order.json()['order']['number']
